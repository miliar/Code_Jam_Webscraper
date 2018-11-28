#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        int n,c=0,sum=0;
        char str[1010];
        cin>>n>>str;
        for(int j=0; j<n+1; j++)
        {
            if(sum<j)
            {
                c+=(j-sum);
                sum+=(j-sum);
            }
            sum+=str[j]-48;
        }
        cout<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0;
}
