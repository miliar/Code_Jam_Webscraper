#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	    printf("Case #%d: ",k);
	    long long int n;
	    long long m;
	    cin>>n;
	    if(n==0)
	    {
	        printf("%s\n","INSOMNIA");
	        continue;
	    }
	    set<int>s;
	    for(long long int i=1;;i++)
	    {
	    	long long n2=i*n;
	    	m=n2;
	    	while(n2)
	    	{
	    		s.insert(n2%10);
	    		n2/=10;
	    	}
	    	if(s.size()==10)
	    	{
	    		printf("%lld\n",m);
	    		break;
	    	}
	    }
	}
	return 0;
}

