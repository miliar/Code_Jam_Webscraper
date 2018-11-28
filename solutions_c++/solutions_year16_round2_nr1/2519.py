#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream f1("A-large (2).in");
    ofstream f2("large.out");
    int T;
    string s;
    int length;
    f1>>T;
    int a[10]={0};
    int letter[28]={0};
    for(int i=0;i<T;i++)
    {
        f1>>s;
        length=s.size();
        for(int j=0;j<10;j++)
        {
            a[j]=0;
        }
        for(int j=0;j<28;j++)
        {
            letter[j]=0;
        }
        for(int j=0;j<length;j++)
        {
            letter[s[j]-'A']++;
        }
        a[0]=letter['Z'-'A'];
        letter['R'-'A']=letter['R'-'A']-a[0];
        letter['O'-'A']=letter['O'-'A']-a[0];
        a[2]=letter['W'-'A'];
        letter['O'-'A']=letter['O'-'A']-a[2];
        a[4]=letter['U'-'A'];
        letter['R'-'A']=letter['R'-'A']-a[4];
        letter['O'-'A']=letter['O'-'A']-a[4];
        letter['F'-'A']=letter['F'-'A']-a[4];
        a[6]=letter['X'-'A'];
        letter['S'-'A']=letter['S'-'A']-a[6];
        letter['I'-'A']=letter['I'-'A']-a[6];
        a[8]=letter['G'-'A'];
        letter['H'-'A']=letter['H'-'A']-a[8];
        letter['I'-'A']=letter['I'-'A']-a[8];
        a[1]=letter['O'-'A'];
        a[3]=letter['H'-'A'];
        a[5]=letter['F'-'A'];
        a[7]=letter['S'-'A'];
        a[9]=letter['I'-'A']-a[5];

        f2 <<"Case #"<<i+1<<": ";
        for(int j=0;j<10;j++)
        {
            while(a[j])
            {
                f2<<j;
                a[j]--;
            }
        }
        f2<<endl;
    }
    return 0;
}
