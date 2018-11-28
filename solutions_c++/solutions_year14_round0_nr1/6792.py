#include <iostream>
using namespace std;

int main(){
	int tc;
	cin>>tc;
	int cas=1;
	while (tc--){
		int a1, a2;
		int p[4][4]; int pp[4][4];
		cin>>a1;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>p[i][j];
		cin>>a2;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>pp[i][j];
		int pos=0; int ans;
		a1--; a2--;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				//cout<<">>"<<p[a1][i]<<" "<<pp[a2][j]<<endl;
				if (p[a1][i]==pp[a2][j]) pos++, ans=p[a1][i];
			}
		}
		cout<<"Case #"<<cas<<": ";
		if (pos==0){
			cout<<"Volunteer cheated!\n";
		} else if (pos==1){
			cout<<ans<<endl;
		} else {
			cout<<"Bad magician!\n";
		}
		cas++;
	}
	return 0;
}