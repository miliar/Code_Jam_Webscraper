#include <iostream>
#include <string>

using namespace std;

int grid1[4][4],grid2[4][4],r1,r2,ec1[16],ec2[16];

int main() {
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;++testcase) {
		cin>>r1;
		r1--;
		for(int i=0;i<16;++i) ec1[i]=0,ec2[i]=0;
		for(int i=0;i<4;++i) for(int j=0;j<4;++j) cin>>grid1[i][j],((i==r1)?ec1[grid1[i][j]-1]=1:r1=r1);
		cin>>r2;
		r2--;
		for(int i=0;i<4;++i) for(int j=0;j<4;++j) cin>>grid2[i][j],((i==r2)?ec2[grid2[i][j]-1]=1:r1=r1);
		for(int i=0;i<4;++i) for(int j=0;j<4;++j) grid1[i][j]--,grid2[i][j]--;
		int badness=0,ans;
		for(int i=0;i<16;++i) {
			if(ec1[i]&&ec2[i]) ans=i;
			badness+=(ec1[i]&&ec2[i]);
		}
		if(!badness) cout<<"Case #"<<testcase<<": Volunteer cheated!";
		else if(badness>1) cout<<"Case #"<<testcase<<": Bad magician!";
		else cout<<"Case #"<<testcase<<": "<<ans+1;
		cout<<"\n";
	}
	return 0;
}
