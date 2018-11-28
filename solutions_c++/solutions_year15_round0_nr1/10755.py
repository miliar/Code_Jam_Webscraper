#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long t,n,sum,count,a,j,i;
    string s;
    cin>>t;
    for(j=0;j<t;j++)
    {
        cin>>n>>s;
        sum=0;
        count=0;
        for(i=0;i<=n;i++)
        {
            if(sum<i)
            {
                count=count+(i-sum);
                sum=i;
            }
            a=s[i]-'0';
            sum=sum+a;
            //cout<<i<<" "<<sum<<" "<<count<<endl;
        }
        cout<<"Case #"<<j+1<<": "<<count<<endl;
    }

	return 0;
}
