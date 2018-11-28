#include <iostream>

using namespace std;

int mat1[4][4], mat2[4][4];
int r1, r2;

int main(){
	int tc, matchcounter, card, cs=0;
	cin>>tc;
	while(tc--){
		cin>>r1;r1--;
		for(int i=0; i< 4; ++i)
			for(int j=0; j< 4; ++j)
				cin>>mat1[i][j];
		cin>>r2;r2--;
		for(int i=0; i< 4; ++i)
			for(int j=0; j< 4; ++j)
				cin>>mat2[i][j];
		matchcounter=0;
		for(int i=0; i< 4; ++i)
			for(int j=0; j< 4; ++j)
				if (mat1[r1][i]==mat2[r2][j]){
					card=mat1[r1][i];
					matchcounter++;
				}
		cout<<"Case #"<<++cs<<":";
		if (matchcounter==1) cout<<" "<<card<<endl;
		else if (matchcounter>1) cout<<" Bad magician!"<<endl;
		else cout<<" Volunteer cheated!"<<endl;
	}


}
