#include <bits/stdc++.h>
using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
	long long t,n,temp,li,prev;
	cin>>t;
	for(long long i=1;i<=t;i++)
	{
	    long long sum=45;
	    bitset<10> flag;
	    cin>>n;
	    if(n==0)
	    cout<<"Case #"<<i<<": INSOMNIA\n";
	    else
	    {
	        prev=0;
	        while(sum||(flag[0]==0))
	        {
	            prev+=n;
	            temp=prev;
	            while(temp)
	            {
	               li=temp%10;
	               temp/=10;
	               if(flag[li]==0)
	               {
	                   flag[li]=1;
	                   sum-=li;
	               }
	            }
	        }
	     cout<<"Case #"<<i<<": "<<prev<<"\n";   
	    }
	}
	return 0;
}