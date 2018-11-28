#include <bits/stdc++.h>
using namespace std;
void increment(bitset<16> &a)
{
	int i=0;
	while(a[i])
	a[i++]=0;
	a[i]=1;
}

int main() {
    std::ios::sync_with_stdio(false);
	long long t,n,j,J,ans,div[11],k,l,count=0;
	cin>>t;
	bitset<16> val(string("1000000000000001"));
	for(long long i=1;i<=t;i++)
	{
	    cin>>n>>J;
	    cout<<"Case #1:";
	    while(count<J)
	    {
	    	
	    	long long res=0;
	    	for(k=2;k<=10;k++)
	    	{
	    		ans=0;
	    		for(j=0;j<16;j++)
	    	  		ans+=val[j]*pow(k,j);	
			for(l=2;l<sqrt(ans);l++)
			if(ans%l==0)
			{
			div[k]=l;
			break;
			}
			if(l<sqrt(ans))
				res++;
			}
			if(res==9)
			{
			cout<<"\n"<<val<<" ";
			for(l=2;l<=10;l++)
			cout<<div[l]<<" ";
			count++;
		}
		increment(val);
		increment(val);
	    }
	}
	return 0;
}