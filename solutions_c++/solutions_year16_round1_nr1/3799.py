#include<bits/stdc++.h>
using namespace std;
char inp[1005];


int t;

int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	int k = 1;
	while(t--)
	{
		cin>>inp;
		int ln = strlen(inp);
		int l = 1001; int r= l+1;
		char out[2010];
		out[l]=inp[0];
		l--;
		for(int i=1;i<ln;i++)
		{
			if(inp[i]>=out[l+1])
			   out[l] = (inp[i]), l--;
			else
			  out[r] = (inp[i]), r++;
		}
		cout<<"Case #"<<k<<": ";k++;
		for(int j=l+1;j<r;j++)
		  cout<<out[j];
		  cout<<endl;
	}
}
