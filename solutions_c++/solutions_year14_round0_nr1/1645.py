#include <cstdlib>
#include <fstream>

using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("out.txt");

int main() {
	int t;
	fin>>t;
	int a[4][4], row[4], k, n, ans;
	for(int i=0;i<t;i++) {
		k=0;
		ans=0;
		fin>>n;
		n--;
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
				fin>>a[x][y];
		for(int j=0;j<4;j++)
			row[j]=a[n][j];
		fin>>n;
		n--;
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
				fin>>a[x][y];
		for(int j=0;j<4;j++)
			for(int x=0;x<4;x++)
			if(row[x]==a[n][j]) {
				if (k==0) ans=row[x];
				k++;
			}
		if(k==1) fout<<"Case #"<<i+1<<": "<<ans<<endl; else
		if(k!=0) fout<<"Case #"<<i+1<<": Bad magician!"<<endl; else
			fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	}
	return 0;
}