#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
    int tt;
    int N;
    long int ans;
    int i,j,k;
    int A,B,K;
    int temp;
    cin>>tt;
    for(int i=1;i<=tt;i++)
    {
        ans=0;
        cin>>A>>B>>K;
        for(k=0;k<A;k++)
        {
                for(j=0;j<B;j++)
                {

                    temp=k&j;
                    if(temp<K)
                    ans++;
                }
        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
	return 0;
}
