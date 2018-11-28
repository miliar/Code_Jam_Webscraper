#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#define N 100005
using namespace std;
int main()
{
    int t,m,u,v;
    double i,j,k,l,n,a,b,s,arr[N];
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    m=t;
    while(t--)
    {
        v=0;
        cin>>a>>b>>n;
        i=2.0;
        j=0.0;
        s=n;
        for(u=0;u<N;u++)
        {
            k=j+n/i;
            if(k<s)
                s=k;
            j+=a/i;
            i+=b;
            //cout<<arr[u-1]<<" ";
        }
        cout<<"Case #"<<m-t<<": ";
		printf("%.7lf\n",s);
    }
    return 0;
}
