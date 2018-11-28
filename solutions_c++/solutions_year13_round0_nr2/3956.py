#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main(int argc, char *argv[]) {
	
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		int f[110][110],n,m,b[110][110];
		bool h[100]; for(int i=0;i<100;i++) h[i]=false;
		fin>>n>>m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++) {
				fin>>f[i][j];
				h[f[i][j]]=true;
			}
		
		bool r=true;
		
		for(int a=0;a<100;a++) {
			if (!h[a]) continue;
			
			memset(b,0,sizeof(int)*110*110);
			for(int i=0;i<n;i++) {  
				for(int j=0;j<m;j++) { 
					if (f[i][j]==a && b[i][j]==0) {
						bool flag=true;
						for(int k=0;k<n;k++) if (f[k][j]>a) { flag=false; break; }
						if (flag) { 
							for(int k=0;k<n;k++) b[k][j]=true;
						} else {
							flag=true;
							for(int k=0;k<m;k++) if (f[i][k]>a) { flag=false; break; }
							if (flag) { 
								for(int k=0;k<m;k++) b[i][k]=true;
							} else {
								r=false;
								break;
							}
						}
					}
				}
				if (!r) break;
			}
			if (!r) break;
		}
		fout<<"Case #"<<I+1<<": "<<(r?"YES":"NO")<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

