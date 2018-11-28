#include <iostream>
#include <string>
#include <fstream>
#include <vector>
typedef long long ll;
using namespace std;

int r,c;
char ds[100][100];

ifstream inf("in.txt");
ofstream of("out.txt");

void doit(int q){
	int x=0;
	for (int i=0; i<r; ++i)
		for (int j=0; j<c; ++j){
			if (ds[i][j]!='.'){
				bool up=false, down=false, right=false, left=false;
				//down:
				for (int k=i+1; k<r; ++k) if (ds[k][j]!='.'){down=true; break;}
				//up:
				for (int k=i-1; k>=0; --k) if (ds[k][j]!='.'){up=true; break;}
				//left:
				for (int k=j-1; k>=0; --k) if (ds[i][k]!='.'){left=true; break;}
				//right:
				for (int k=j+1; k<c; ++k) if (ds[i][k]!='.'){right=true; break;}
				if (!up && !down && !right && !left){
					of<<"Case #"<<q+1<<": "<<"IMPOSSIBLE"<<endl;
					return;
				}
				if (!(ds[i][j]=='^' && up || 
					ds[i][j]=='v' && down ||
					ds[i][j]=='<' && left ||
					ds[i][j]=='>' && right))
					++x;
			}
		}
	of<<"Case #"<<q+1<<": "<<x<<endl;
}

int main(){
	int qN;
	inf>>qN;

	for(int q=0; q<qN; ++q){
		inf>>r>>c;
		
		for(int i=0; i<r; ++i)
			for(int j=0; j<c; ++j)
				inf>>ds[i][j];
		doit(q);

	}
}