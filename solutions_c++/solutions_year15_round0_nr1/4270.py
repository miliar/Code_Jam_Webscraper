#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int t,smax,sum,i=0,cnt;
    char c[1002];
    for(cin>>t,i=0; i<t ; i++)
    {
        cin>>smax; cin>>c;
        sum=0; cnt=0; //getchar_unlocked();
        for(int j=0;j<=smax;j++)
        {
            sum+=c[j]-'0';//getchar_unlocked() - '0';
            if(sum<=j)
            {
                sum++; cnt++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
}
