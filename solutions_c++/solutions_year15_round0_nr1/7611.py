#include<iostream>
using namespace std;
int main()
{
    int i,sum,n,t=1,T,fr;
    char ara[1100];
    cin>>T;
    while(T--)
    {
        cin>>n;
        cin>>ara;
        sum=ara[0]-'0';
        fr=0;
        for(i=1;i<=n;i++)
        {
            if(sum>=i)
                sum = sum + ara[i]-'0';
            else
            {
                fr = fr + i - sum;
                sum = i+ ara[i]-'0';
            }
        }
        cout<<"Case #"<<t++<<": "<<fr<<endl;

    }
    return 0;
}
