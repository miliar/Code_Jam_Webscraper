#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

void solve()
{
	int A[4][4],B[4][4],m,n;
	cin>>m;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>A[j][k];

		cin>>n;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>B[j][k];
				
		int ret = -1;
		int cnt = 0;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(A[m-1][j]==B[n-1][k]){
						cnt++;
						ret=A[m-1][j];
					}
		if(cnt==1)cout<<ret<<endl;
		else if(cnt>1)cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;
}
int main()
{
	freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdin);
	int ca;
	cin>>ca;
	for(int i=0;i<ca;i++)
	{
		cout<<"Case #"<<i+1<<": ";solve();
	}
	return 0;
}
