#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("test.out","w",stdout);
    long long int t,n,temp,i=1;
    cin>>t;
    set<int>s;
    for(int j=1;j<=t;j++)
    {
        cin>>n;
        temp=n;
        if(temp==0)
           {
            printf("Case #%d: INSOMNIA\n", j);
           }
        else
        {
        while(s.size()!=10)
        {
           n=temp*i;
           while(n>0)
           {
               s.insert(n%10);
               n=n/10;
           }
           i++;
        }
        printf("Case #%d: %d\n", j,temp*(i-1));
        i=1;
        s.clear();
        }
    }

    return 0;
}
