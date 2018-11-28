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
		char t[105];
		cin>>t;
		int con=0;
		int len=strlen(t);
		for(int i=1;i<len;i++)
		if(t[i]!=t[i-1])
		con++;
		if(t[len-1]=='+')
			printf("Case #%d: %d\n",ll+1,con);
		else
			printf("Case #%d: %d\n",ll+1,con+1);
	}
	
	return 0;
}

