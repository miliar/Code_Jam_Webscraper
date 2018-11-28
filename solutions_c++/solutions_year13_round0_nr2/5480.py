#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VII;
typedef vector<VS> VSS;

#define PB push_back
	
void findmax(const VII& pattern, VI& rowmax, VI& colmax) {
	int m=pattern.size(), n=pattern[0].size();
	for(int i=0; i<m; i++) {
		rowmax[i]=pattern[i][0];
		for(int j=1; j<n; j++) rowmax[i]=max(rowmax[i], pattern[i][j]);
	}
	for(int j=0; j<n; j++) {
		colmax[j]=pattern[0][j];
		for(int i=0; i<m; i++) colmax[j]=max(colmax[j], pattern[i][j]);
	}
}

bool bfs(queue<pair<VI, char> >& q, const VII& pattern, int m, int n, set<int>& row, set<int>& col) {
		while(!q.empty()) {
			pair<VI, char> node=q.front();
		       	q.pop();
			VI v=node.first;
			int i=v[0], j=v[1];
			if (node.second=='c' && col.find(v[1])==col.end()) {
				int val=pattern[i][j];
				for(int k=0; k<m; k++) {
					if(pattern[k][j]>val) return false;
					else if(pattern[k][j]<val) {
						VI v2(2, 0);
						v2[0]=k;
						v2[1]=v[1];
						q.push(make_pair(v, 'r'));
					}
				}
				col.insert(v[1]);
			}
			if (node.second=='r' && row.find(v[0])==row.end()) {
				int val=pattern[v[0]][v[1]];
				for(int k=0; k<n; k++) {
					if(pattern[v[0]][k]>val) return false;
					else if(pattern[0][k]<val) {
						VI v2(2, 0);
						v2[0]=v[0];
						v2[1]=k;
						q.push(make_pair(v, 'c'));
					} 
				}
				row.insert(v[0]);
			}	
		}
		return true;
}

bool iswork(const VII& pattern, int m, int n) {
	queue<pair<VI, char> > q;
       	set<int> row;
	set<int> col;
	VI rowmax(m, 0);
	VI colmax(n, 0);
	findmax(pattern, rowmax, colmax);
	for (int i=0; i<m; i++) {
		int maxh=rowmax[i];
		if (row.find(i)!=row.end()) continue;
		for(int j=0; j<n; j++) {
			if(pattern[i][j]<maxh) {
				VI v(2, 0);
				v[0]=i;
				v[1]=j;
				q.push(make_pair(v, 'c'));
			}
		}	
		row.insert(i);
		bool check=bfs(q, pattern, m, n, row, col);
		if(!check) return false;
	}

	for (int j=0; j<n; j++) {
		int maxh=colmax[j];
		if (col.find(j)!=row.end()) continue;
		for(int i=0; i<m; i++) {
			if(pattern[i][j]<maxh) {
				VI v(2, 0);
				v[0]=i;
				v[1]=j;
				q.push(make_pair(v, 'r'));
			}
		}	
		col.insert(j);
		bool check=bfs(q, pattern, m, n, row, col);
		if(!check) return false;
	}
	return true;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int n;
	fin >> n;
	for(int k=1; k<=n; k++) {
		int m, n;
		fin >> m >> n;
		VII pattern(m, VI(n, 0));
		for (int i=0; i<m; i++) {
			for(int j=0; j<n; j++) 
				fin >> pattern[i][j];	
		}
		bool result=iswork(pattern, m, n);
		if(result) fout<<"Case #"<< k <<": YES"<<endl;
		else fout<<"Case #"<< k <<": NO"<<endl;
	}
		
	fin.close();
	fout.close();
	return 0;
}













