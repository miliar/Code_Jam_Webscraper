#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    long long int n,t,c,i,j;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    string s;
    for(j=1;j<=t;j++)
    {
        cin>>n;
        cin>>s;
        c = 0;
        long long int sum[n+1];
        if(s[0] == '0'){
            c = 1;
        }
        sum[0] = (s[0] - '0') + c;
        for(i=1;i<=n;i++)
        {
            if( i <= sum[i-1])
            {
                sum[i] = sum[i-1] + (s[i] - '0');
            }
            else
            {
                c += (i-sum[i-1]);
                sum[i] = sum[i-1] + (i-sum[i-1]) + (s[i]-'0');
            }
        }
        cout<<"Case #"<<j<<": "<<c<<endl;
    }
    return 0;
}
