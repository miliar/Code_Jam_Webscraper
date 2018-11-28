#include<bits/stdc++.h>
using namespace std;

int solve() {
	int N;
	cin >> N;
	vector<string> input(4);
	int init = 0;
	for(int i=0; i<N; i++) {
		cin >> input[i];
		for(int j=0; j<N; j++)
			init += input[i][j]-'0';
	}
	int field[4][4];
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			field[i][j] = 0;
	int ans = N*N;
	for(int bit=0; bit<(1<<(N*N));  bit++) {
		bool ok = true;
		int cnt = 0;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++) {
				if(!((bit>>(i*N+j))&1) && input[i][j]=='1')
					ok = false;
				field[i][j] = (bit>>(i*N+j))&1;
				cnt += field[i][j];
			}
		if(!ok) continue;
		
		vector<int> row,col;
		for(int i=0; i<N; i++) {
			int c = 0;
			for(int j=0; j<N; j++) {
				if(field[i][j]==1) c++;
			}
			if(c==0) ok = false;
			row.push_back(c);
		}
		for(int i=0; i<N; i++) {
			int c = 0;
			for(int j=0; j<N; j++) {
				if(field[j][i]==1) c++;
			}
			if(c==0) ok = false;
			col.push_back(c);
		}
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				if(field[i][j])
					if(row[i] != col[j])
						ok = false;
		for(int i=0; i<N; i++) 
			for(int j=0; j<N; j++)
				for(int k=0; k<N; k++)
					for(int l=0; l<N; l++)
						if(field[i][k]==1 && field[i][l]==1 && field[j][k]==1 && field[j][l]==0) {
							ok = false;
						}
		if(!ok) continue;
		ans = min(ans, cnt - init);
		
		if(cnt<0)
		for(int i=0; i<N; i++, cout << endl)
			for(int j=0; j<N; j++)
				cout << field[i][j] ;
		
		
	}
	return ans;
	
}

int main() {
	int T;
	cin >> T;
	for(int _=0; _<T; _++) {
		int ans = solve();
		cout << "Case #" << _+1 << ": " << ans <<endl;
		
	}
	
	return 0;
	
}

