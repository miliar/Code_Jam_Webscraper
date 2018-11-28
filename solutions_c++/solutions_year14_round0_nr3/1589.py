#include<fstream>
#include<iostream>

using namespace std;

ifstream fin("C-small-attempt2.in");
ofstream fout("C-small-attempt2.out");

int r,c;
char mp[51][51];

void print(){
	for (int i=0;i<r;i++){
		for (int j=0;j<c;j++)
			cout << mp[i][j];
		cout << endl;
	}
}

int main(){

	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	int ntc,m;
	cin >> ntc;

	for (int tc=1;tc<=ntc;tc++){

		cout << "Case #" << tc << ": " << endl;
		cin >> r >> c >> m;


		for (int i=0;i<r;i++) for (int j=0;j<c;j++) mp[i][j] = '.';
		//if (r==5 && c==5 && m==16){
		//	for (int i=0;i<r;i++) mp[i][0] = mp[i][c-1] = '*';
		//	for (int i=0;i<c;i++) mp[0][i] = mp[r-1][i] = '*';
		//	mp[2][2] = 'c';
		//	print();
		//	continue;
		//}
		int a = 0,b = 0;
		for (int kk=0;kk<m;kk++){
			if (b==c){
				a++;
				b=0;
			}
			mp[a][b++] = '*';
		}
		mp[r-1][c-1] = 'c';

		if (m==r*c-1){
			print();
			continue;
		}

		if (r==1 || c==1){
			print();
			continue;
		}

		int k = 1;
		while(k<=r && mp[r-k][0]!='*') k++;

		if (k==2 || k==1){
			m = m%c;
			if (m==0) m = c;
			if (k==1) m += c;
			if (m%2==0 && m<=2*c-4){
				for (int j=0;j<m/2;j++)
					mp[r-1][j] = mp[r-2][j] = '*';
				for (int j=m/2;j<c;j++)
					mp[r-1][j] = mp[r-2][j] = '.';
				mp[r-1][c-1] = 'c';
				print();
				continue;
			}
			if (r>2 && k==2 && m%2==1){
				if (c>3 && (m+3)/2<=c-3){
					for (int j=c-3;j<c;j++)
						mp[r-3][j] = '.';
					for (int j=0;j<(m+3)/2;j++)
						mp[r-1][j] = mp[r-2][j] = '*';
					for (int j=(m+3)/2;j<c;j++)
						mp[r-1][j] = mp[r-2][j] = '.';
					mp[r-1][c-1] = 'c';
					print();
					continue;
				}
			}

			cout << "Impossible" << endl;
			continue;			
		}
		if (k==3){
			m = m%c;
			if (m==0) m = c;
			if (m==c-1){
				if (c==2 || c==3){
					cout << "Impossible" << endl;
					continue;			
				}
				mp[r-3][m-1] = mp[r-3][m-2] = '.';
				mp[r-2][0] = mp[r-1][0] = '*';
				print();
				continue;
			}
			print();
			continue;
		}
		m = m%c;
		if (m==0) m = c;
		if (m==c-1){
			if (c==2){
				cout << "Impossible" << endl;
				continue;			
			}
			mp[r-k][m-1] = '.';
			mp[r-k+1][0] = '*';
			print();
			continue;
		}
		print();
		continue;

	}

	return 0;
}