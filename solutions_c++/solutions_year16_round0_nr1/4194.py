#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    ios_base::sync_with_stdio(0);
    ll n,sum=0,count=0,t;
    ifstream f("A-large.in");
    ofstream o("Aout.out");
    f>>t;
    int z=t;
    while(t--)
    {
        f>>n;
        if(n==0)
        {
            o<<"Case #"<<z-t<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int b[11]={0};
        ll p=1;
        ll flag=0;
        while(1){
            int k=p*n;

            while(k)
        {
            b[k%10]++;
            k=k/10;
        }
        flag=0;
        //cout<<p*n<<" ";
        for(int i=0;i<10;i++)
        {
            if(b[i]==0)
            {
                flag=1;
                break;
            }
            //cout<<b[i]<<" ";
        }
        //cout<<endl;
        if(flag==0)
        {
                o<<"Case #"<<z-t<<": "<<p*n<<endl;
                break;
        }
        p++;
        }
    }
	return 0;
}


