#include <iostream>
#include <map>
using namespace std;
int main()
{
    int t,tt;
    string s;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>s;
        int cnt[10]={0};
        map<char,int> m;
        for (int i=0;i<s.size();i++)
        {
            m[s[i]]++;
        }
        cnt[0]=m['Z'];
        cnt[2]=m['W'];
        cnt[4]=m['U'];
        cnt[6]=m['X'];
        cnt[8]=m['G'];
        cnt[3]=m['H']-cnt[8];
        cnt[5]=m['F']-cnt[4];
        cnt[7]=m['S']-cnt[6];
        cnt[9]=m['I']-cnt[5]-cnt[6]-cnt[8];
        cnt[1]=m['N']-cnt[7]-cnt[9]*2;
        cout<<"Case #"<<tt<<": ";
        for (int i=0;i<10;i++)
        {
            if (cnt[i]) for (int j=0;j<cnt[i];j++) cout<<(char)(i+'0');
        }
        cout<<endl;
    }
    return 0;
}
