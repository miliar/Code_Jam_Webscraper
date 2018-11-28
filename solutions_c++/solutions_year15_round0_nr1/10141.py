#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("input1.txt");
    ofstream out("outpur.txt");
    int t;
    in>>t;
    int a[t];
    for(int i=0;i<t;i++)
    {
        int s,no_standing=0,frnd=0;
        in>>s;
        char c[s+1];
        int c1[s+1];
        in>>c;
        for(int j=0;j<=s;j++)
            c1[j]=c[j]-'0';
        no_standing=c1[0];
        for(int j=1;j<=s;j++)
        {
            if(j>no_standing)
            {
                frnd+=j-no_standing;
                no_standing+=c1[j]+j-no_standing;
            }
            else no_standing+=c1[j];
        }
        a[i]=frnd;
    }
    for(int i=0;i<t;i++)
        out<<"Case #"<<(i+1)<<": "<<a[i]<<"\n";
    return 0;
}
