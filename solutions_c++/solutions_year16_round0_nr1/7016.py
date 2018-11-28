#include<bits/stdc++.h>
using namespace std;
#define ll long long
long long int mod=1000000007;

bool covered(bool *p)
{
   int count=0;
   for(int i=0;i<10;i++)
   {
       if(*(p+i)==true)
        count++;
   }
   if(count==10)
        return true;
   return false;
}
int main()
{
    ios::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int tc=1;
    while(tc<=t)
    {
        int n;
        cin>>n;

        if(n==0)
            cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
        else
        {
            bool a[10];

            for(int i=0;i<10;i++)
                a[i]=false;

            int i=n;
            while(covered(a)==false)
            {
               int x=i;

               while(x)
               {
                   a[x%10]=true;
                   x/=10;
               }
               i+=n;
            }
            i-=n;
            cout<<"Case #"<<tc<<": "<<i<<endl;

        }

        tc++;
    }
    return 0;
}
