#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);

	int T,N,M,arr[101][101];
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		cin>>N>>M;
		for(int i=0 ; i<N ; i++)
		{
			for(int j=0 ; j<M ; j++)
			{
				cin>>arr[i][j];
			}
		}
		bool fail=false;
		for(int i=0 ; i<N && !fail ; i++)
		{
			for(int j=0 ; j<M && !fail; j++)
			{
				
					int r=0,c=0;
					for(int k=0 ;c==0 && k<N ; k++)
					{
						if(arr[k][j]>arr[i][j])
							c++;
					}
					for(int k=0 ;r==0 && k<M ; k++)
					{
						if(arr[i][k]>arr[i][j])
							r++;
					}
					if(r>0 && c>0)
						fail=true;
				
			}
		}
		cout<<"Case #"<<CASE<<": ";
		if(!fail)
			cout<<"YES\n";
		else
			cout<<"NO\n";

	}

	return 0;
}