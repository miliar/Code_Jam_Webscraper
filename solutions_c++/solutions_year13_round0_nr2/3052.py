#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int nTestCases;
	ifstream in("B-large.in");
	ofstream out("out");
	in>>nTestCases;
	for(int t=0; t<nTestCases; t++) {
		int n, m;
		in>>n>>m;
		int targetH[n][m];
		for(int r=0; r<n; r++) {
			for(int c=0; c<m; c++) {
				in>>targetH[r][c];
			}
		}
		bool possible=true;
		for(int r=0; r<n && possible; r++) {
			for(int c=0; c<m && possible; c++) {
				bool rowPossible=true, columnPossible=true;
				for(int i=0; i<m; i++)
					if(targetH[r][i]>targetH[r][c]) {
						rowPossible=false;
						break;
					}
				for(int i=0; i<n; i++)
					if(targetH[i][c]>targetH[r][c]) {
						columnPossible=false;
						break;
					}
				possible&=(rowPossible||columnPossible);
			}
		}
		out<<"Case #"<<(t+1)<<": "<<(possible?"YES":"NO")<<endl;
	}
	in.close();
	out.close();
}