#include <bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
typedef long long ll;

int gcd(int a, int b)
{
    while(b) b ^= a ^= b ^= a %= b;
    return a;
}

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t,s,sum,i,n,tmp,ctr=1;
    string str;
    int arr[1010];
    cin>>t;
    while(t--)
    {
        cin>>s>>str;
        n = s+1;
        for(i=0;i<n;++i)
        {
            arr[i] = str[i]-'0';
        }
        sum = 0;

        //cout<<"arr is "<<arr[0]<<"\n";
        //cout<<"sum is "<<sum<<"\n";

        if(arr[0]<1)
        {
            tmp = (1-arr[0]);
            sum += tmp;
            arr[0] += tmp;
        }

        //cout<<"arr is "<<arr[0]<<"\n";
        //cout<<"sum is "<<sum<<"\n";

        for(i=1;i<n;++i)
        {
            arr[i] += arr[i-1];

            //cout<<"arr is "<<arr[i]<<"\n";
            //cout<<"sum is "<<sum<<"\n";

            if(arr[i]<i+1)
            {
                tmp = (i-arr[i]+1);
                sum += tmp;
                arr[i] += tmp;
            }
        }

        printf("Case #%d: %d\n",ctr++,sum);
    }
    return 0;
}
