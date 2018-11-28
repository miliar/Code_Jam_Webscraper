#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int n; cin>>n;
	int cse=1;
	while (cse<=n) {
		int r1,r2; cin>>r1;
		int f[4][4];
		int memo1[4],memo2[4];
		int ans=0,cnt=0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin>>f[i][j];
				if(i+1==r1) memo1[j]=f[i][j];
			}
		}
		cin>>r2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin>>f[i][j];
				if(i+1==r2) memo2[j]=f[i][j];
			}
		}

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if(memo1[i]==memo2[j])
				{
					cnt++;
					ans=memo1[i];
				}
			}
		}

		cout<<"Case #"<<cse<<": ";
		cse++;
		if(cnt==1) cout<<ans;
		else if(cnt==0) cout<<"Volunteer cheated!";
		else cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}
