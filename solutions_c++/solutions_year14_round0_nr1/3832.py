#include<fstream>
#include<iostream>

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int c1[4][4],c2[4][4];

int main(){

	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	int ntc,a,b;
	cin >> ntc;

	for (int tc=1;tc<=ntc;tc++){

		cin >> a;a--;
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) cin >> c1[i][j];
		cin >> b;b--;
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) cin >> c2[i][j];

		cout << "Case #" << tc << ": ";

		int find = 0;
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				if (c1[a][i]==c2[b][j]){
					if (find){
						cout << "Bad magician!" << endl;
						goto end;
					}
					find = c1[a][i];
				}
			}
		}
		if (find) cout << find << endl;
		else cout << "Volunteer cheated!" << endl;
end:;

	}

	return 0;
}