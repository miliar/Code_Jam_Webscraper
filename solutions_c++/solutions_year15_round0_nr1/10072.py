#include<iostream>
using namespace std;
int main()
{
    int t,l,i,sum,count,n,j;
    char str[1002];
    cin>>t;
    for(i=1;i<=t;++i)
    {
        cin>>n;
        cin>>str;
        sum=0;
        count=0;
        for(j=0;j<n;++j)
        {
            sum=sum+str[j]-'0';
            if(sum+count<(j+1))
            {
                count=(j+1)-sum;
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
}
