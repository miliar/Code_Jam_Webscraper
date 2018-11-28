#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;

bool checkPalin(int n)
{
	string tmp;
	while(n)
	{
		int s=n%10;
		n/=10;
		tmp+='0'+s;
	}

	int l=0,r=tmp.size()-1;
	while(l<r)
	{
		if(tmp[l]!=tmp[r]) return false;
		l++; r--;
	}

	return true;
}


int main()
{
	int isPalin[1001];
	fill(isPalin,isPalin+1001,0);
	isPalin[0]=0;
	isPalin[1]=1;
	for(int i = 2; i < 1001; ++i)
	{
		for(int j = 2; j < 36; ++j)
		{
			if(i==j*j)
			{
				if(checkPalin(i)&&checkPalin(j)) isPalin[i]=isPalin[i-1]+1;
			}
		}
		if(isPalin[i]==0) isPalin[i]=isPalin[i-1];
	}

	int t; cin>>t;
	for(int out = 1; out <= t; ++out)
	{
		int a,b; cin>>a>>b;
		printf("Case #%d: ",out); cout<<isPalin[b]-isPalin[a-1]<<endl;	
	}
  return 0;
}
