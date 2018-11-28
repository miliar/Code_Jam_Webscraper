#include<bits/stdc++.h>
using namespace std;
int mat[5][5];
int r1[5],r2[5];
int main(){
	int t;
	cin >> t;
	int row;
	for(int ii=1;ii<=t;ii++){
		cout << "Case #" << ii<<": " ;
		cin >> row;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) cin >> mat[i][j];
		for(int i=1;i<=4;i++) r1[i]=mat[row][i];
		cin >> row;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) cin >> mat[i][j];
		for(int i=1;i<=4;i++) r2[i]=mat[row][i];
		int res,cont=0;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) if(r1[i]==r2[j]) { cont++; res=r1[i];}
		if(cont==1) cout << res << endl;
		else if(cont == 0) cout << "Volunteer cheated!"<<endl;
		else if(cont >1) cout << "Bad magician!"<<endl;
	}
}