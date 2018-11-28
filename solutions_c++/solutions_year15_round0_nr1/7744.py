#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull; 

int main()
{
    int t, n, tmp, ans, sum;
    string dat;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        dat.clear();
        sum=ans=0;
        cin>>n>>dat;        
        for(int i=0;i<=n;i++)
        {
            //cout<<dat[i];
            if(sum<i)
            {
                //cout<<i<<" : "<<sum<<endl;
                ans = ans+(i-sum);
                sum=i;
            }    
            sum+=(dat[i]-'0');
        }
        //cout<<dat.size()<<" : "<<dat[6]<<endl;
        printf("Case #%d: %d\n", (j+1), ans);
    }
    return 0;
}
