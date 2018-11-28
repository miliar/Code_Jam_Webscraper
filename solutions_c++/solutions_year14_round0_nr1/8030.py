# include <fstream>
# include <iostream>
# define DIM 8
using namespace std;
int a[DIM][DIM], b[DIM][DIM], s, r;

int main()
{
	ifstream fin ("f.in");
	ofstream fout ("f.out");
	
	int T;
	fin>>T;
	for(int t=1;t<=T;++t) {
		fin>>s;
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				fin>>a[i][j];
		
		fin>>r;
		for(int i=1;i<=4;++i)
			for(int j=1;j<5;++j)
				fin>>b[i][j];
		
		int p, c=0;

		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				if (a[s][i]==b[r][j]) {
					++c;
					p=a[s][i];
					break;
				}
			
		fout<<"Case #"<<t<<": ";
		if (c==1) {
			fout<<p<<"\n";
		} else if (c>1) {
			fout<<"Bad magician!\n";
		} else {
			fout<<"Volunteer cheated!\n";
		}
	}
	
	return 0;
}
