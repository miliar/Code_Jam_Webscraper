#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int n;
	cin>>n;
	for(int ll=0;ll<n;ll++)
	{
		int k,c,s;
		cin>>k>>c>>s; 
			printf("Case #%d:",ll+1);
			for(int i=1;i<=s;i++)
			printf(" %d",i);
			printf("\n");
	}
	
	return 0;
}

