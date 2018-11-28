#include <fstream>
using namespace std;

ifstream f("B-large.in"); ofstream g("B-large.out");

int i, j, k, n, m, ii, t, mn;
int v[105][105];
int lines[105], cols[105];
bool no;

int main(){
	f>>t;
	for (ii=1; ii<=t; ii++){
		f>>n>>m;
		for (i=1; i<=n; i++) for (j=1; j<=m; j++) f>>v[i][j];
		for (i=1; i<=n; i++) {
			mn = 0;
			for (j=1; j<=m; j++) if (v[i][j]>mn) mn = v[i][j];
			lines[i]=mn;
		}
		for (i=1; i<=m; i++) {
			mn = 0;
			for (j=1; j<=n; j++) if (v[j][i]>mn) mn = v[j][i];
			cols[i]=mn;
		}
		no = 0;
		for (i=1; i<=n; i++) for (j=1; j<=m; j++) if (v[i][j]!=min(lines[i], cols[j])) no = 1;
		if (no) g<<"Case #"<<ii<<": NO\n";
		else g<<"Case #"<<ii<<": YES\n";
	}

}
