#include<fstream>

using namespace std;

void main(){
	ifstream ulaz;
	ofstream izlaz;

	ulaz.open("lawnmower.in");
	izlaz.open("lawnmower.out");


	int T;
	ulaz>>T;
	for(int counter = 1; counter<=T; counter++){
		
		int n,m;
		int i,j;
		ulaz>>n>>m;
		int a[100][100];
		int maxvrsta[100] = {0};
		int maxkolona[100] = {0};
		for(i = 0; i<n; i++){
			for(j = 0; j<m; j++){
				ulaz>>a[i][j];
				if(a[i][j]>maxvrsta[i]) maxvrsta[i] = a[i][j];
				if(a[i][j]>maxkolona[j]) maxkolona[j] = a[i][j];
			}
		}
		for(i = 0; i<n; i++){
			for(j = 0; j<m; j++){
				if(a[i][j]!= maxvrsta[i] && a[i][j]!=maxkolona[j]) {izlaz<<"Case #"<<counter<<": NO\n"; break;}
			}
			if(j<m) break;
		}
		if(i == n) izlaz<<"Case #"<<counter<<": YES\n";

	}



	ulaz.close();
	izlaz.close();

}