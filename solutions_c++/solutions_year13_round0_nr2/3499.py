# include <iostream>
# include <fstream>
# include <string>

using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

# define MAXN 101
# define MAXM 101

int lawn [MAXN][MAXM];
int m,n;

bool valid (int i,int j,int x){
	// vertical
	bool vertical = true;
	for (int k=0;k<n;k++){
		if (lawn[k][j] > x)
			vertical = false;
	}

	if (vertical)
		return true;

	// horizontal
	for (int k=0;k<m;k++)
		if (lawn[i][k] > x)
			return false;

	return true;
}

int main (){

	int T;

	fin >> T;
	for (int i=0;i<T;i++){
		fin >> n >> m;
		int maxH = 0;
		for (int j=0;j<n;j++){
			for (int k=0;k<m;k++){
				fin >> lawn[j][k];
				maxH = max(maxH,lawn[j][k]);
			}
		}

		bool ok = true;
		for (int j=0;j<n;j++){
			for (int k=0;k<m;k++){
				if (lawn[j][k] < maxH)
					if (!valid(j,k,lawn[j][k]))
						ok = false;
			}
		}
		if (ok)
			fout << "Case #" << i+1 << ": YES\n";
		else
			fout << "Case #" << i+1 << ": NO\n";
	}

	return 0;
}
