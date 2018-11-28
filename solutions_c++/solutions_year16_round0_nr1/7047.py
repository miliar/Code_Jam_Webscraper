#include<bits/stdc++.h>
using namespace std;
bool a[10];
bool check()
{
    if(a[0]&&a[1]&&a[2]&&a[3]&&a[4]&&a[5]&&a[6]&&a[7]&&a[8]&&a[9])
        return true;
    else
        return false;
}
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
int t,i,z;
cin>>t;
for(int x=1;x<=t;x++)
{
    for( i=0;i<=9;i++)
        a[i]=false;
    long long int n;
    cin>>n;
    if(n==0)
        cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
    else
    {
           for( z=n;!check();z+=n)
            {
                long long int dummy=z;
                while(dummy)
                {
                    a[(dummy%10)]=true;
                    dummy=dummy/10;

                }
            }
         cout<<"Case #"<<x<<": "<<z-n<<"\n";

    }
}
return 0;
}
