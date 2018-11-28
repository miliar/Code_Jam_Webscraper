#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++)
	{
		int ans,ans1,ans2,a1[4][4],a2[4][4],cc=0;
		
		cin>>ans1;
		ans1--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a1[i][j];
		
		cin>>ans2;
		ans2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a2[i][j];
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a1[ans1][i] == a2[ans2][j])
				{
					ans=a1[ans1][i];
					cc++;
				}
		
		if(cc==1) 
			cout<<"Case #"<<tc<<": "<<ans<<endl; 
		else if(cc==0) 
			cout<<"Case #"<<tc<<": "<<"Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<tc<<": "<<"Bad magician!"<<endl;
		
		
	}
	return 0;
}