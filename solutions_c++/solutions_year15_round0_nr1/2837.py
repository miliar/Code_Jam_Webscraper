#include<iostream>
#include<stdio.h>
#include<set>
using namespace std;
char s[10000];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,n;
    int sMax;
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>sMax>>s;
        int minPeo=0,curPeo=0;
        for(j=0;j<=sMax;++j)
        {
            if(curPeo<j&&s[j]!='0')
            {
                minPeo+=j-curPeo;
                curPeo=j;
            }
            curPeo+=s[j]-'0';
        }
        cout<<"Case #"<<i+1<<": "<<minPeo<<endl;
    }
}
