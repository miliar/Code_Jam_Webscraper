#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int main()
{
	int t,i,j,a[5][5],b[5][5],cnt,ans1,ans2,val,tc;
	freopen("D:\\input.txt","r",stdin);
	freopen("D:\\output.txt","w",stdout);
	cin>>tc;
	for(t=1;t<=tc;t++){
		cnt=0;
		cin>>ans1;
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				cin>>a[i][j];
		cin>>ans2;
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				cin>>b[i][j];
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				if(a[ans1][i]==b[ans2][j]){
					cnt++;
					val=a[ans1][i];
				}
		cout<<"Case #"<<t<<": ";
		if(cnt==0) cout<<"Volunteer cheated!\n";
		else if(cnt>1) cout<<"Bad magician!\n";
		else cout<<val<<endl;
	}
	return 0;
}
