#include<iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int d1[4][4],d2[4][4];
		int r1,r2,ans=-1;
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>d1[i][j];
		cin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>d2[i][j];
		r1--;
		r2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++) {
				if(d1[r1][i]==d2[r2][j]&&ans==-1)
					ans=d1[r1][i];
				else if(d1[r1][i]==d2[r2][j]&&ans>0&&ans!=d1[r1][i])
					ans=-2;
			}
		cout<<"Case #"<<tt<<": ";
		if(ans==-1)cout<<"Volunteer cheated!";
		else if(ans==-2)cout<<"Bad magician!";
		else cout<<ans;
		cout<<endl;
	}
	return 0;
}
