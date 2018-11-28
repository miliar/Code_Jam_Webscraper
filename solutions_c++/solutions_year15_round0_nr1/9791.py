#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
        c++;
        int n,num=0,sum=0,i,j;
        char mk[10002];
        cin>>n;
        cin>>mk;
        sum=(mk[0]-48);
        for(i=1;i<=n;i++)
        {
            if(sum<i)
            {
                num+=i-sum;
                sum=i;
            }

            sum+=(mk[i]-48);

        }
        cout<<"Case #"<<c<<": "<<num<<endl;

    }
    return 0;
}
