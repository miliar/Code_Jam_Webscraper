#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char arr[10009];
int main()
{
    int t;
    cin>>t;
    ll z=1;
    while(t--)
    {
        ll s,sum=0,ans=0,temp,i;
        cin>>s;
        cin>>arr;
        for(i=0;i<strlen(arr);i++)
        {
            if(sum>=i && arr[i]!='0')
            {
                temp= arr[i]- '0';
                sum+=temp;
            }
            else if(sum<i && arr[i]!='0')
            {
                temp= i-sum;
                ans+=temp;
                sum+=temp;
                temp= arr[i]-'0';
                sum+=temp;
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
        z++;
    }
    return 0;
}
