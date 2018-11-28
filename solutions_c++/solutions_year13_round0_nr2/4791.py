#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

const int MARK = 1000000;

void printable(const vector<vector<int>> & x) {
	cout << "DEBUG:" << endl;
	for (int i=0;i < x.size();++i) {
		for (int j=0;j < x[0].size();++j) {
			cout << x[i][j] << " ";
		}
		cout << endl;
	}
}

bool markat(vector< vector<int> > & table,int x,int y) {

	const int M = table.size();
	const int N = table[0].size();
	
	bool ok = true;
	for (int i=0;i < M;++i) {
		if ( table[i][y] != table[x][y] && table[i][y] != MARK) {ok = false; break;}
	}
	if (ok) {
		for (int i=0;i < M;++i) {
			table[i][y] = MARK;
		}
		return true;
	}
	
	ok = true;
	
	for (int i=0;i < N;++i) {
		if ( table[x][i] != table[x][y] && table[x][i] != MARK) {ok = false; break;}
	}
	if (ok) {
		for (int i=0;i < N;++i) {
			table[x][i] = MARK;
		}
		return true;
	}
	return false;	
}

bool solve(vector<vector<int> > & table) {
	for (int WHO=1;WHO <=100;++WHO) {
		int x = -1,y = -1;
		do {
			x = -1; y = -1;
			for (int i=0;i < table.size();++i)
				for (int j = 0; j < table[0].size();++j) {
					if (table[i][j] == WHO) {
						x = i;
						y = j;
					}
				}
			if (x != -1)
			{
				if (!markat(table,x,y)) return false;
// 				printable(table);
			}
		}
		while(x != -1);
	}
	bool DEBUG = true;
	for (int i=0;i < table.size();++i)
		DEBUG &=  std::all_of( table[i].begin(),table[i].end(),[](int n) {return n == MARK;});
	assert(DEBUG);
	return true;
}


int main ()
{
	int T;
	cin >> T;
	cin.ignore(1000,'\n');
	
	for (int i=0;i < T;++i) {
		vector<vector<int>> table;
		int M,N;
		cin >> N >> M;
		
		table.resize(N, vector<int>(M));
		for (int j=0;j < N;++j) {
			for (int k=0;k < M;++k) {
				cin >> table[j][k];
			}
			cin.ignore(1000,'\n');
		}
		
		cout << "Case #" << i+1 << ": " << (solve(table) ? "YES" : "NO") << endl;
	}
	return 0;
}