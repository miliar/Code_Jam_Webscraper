#include <iostream>
using namespace std;

int main() {
	int t,ar[4][4],br[4][4],a,b,count=0,ans;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>a;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
			cin>>ar[i][j];
		}
		cin>>b;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
			cin>>br[i][j];
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
			if(ar[a-1][i]==br[b-1][j]){
			count++;
			ans=ar[a-1][i];
			}
			}
			
			}
			if(count==1)
			cout<<"Case #"<<i<<": "<<ans<<endl;
			if(count>1)
			cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
			if(count==0)
			cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
			count=0;
	}
	return 0;
}