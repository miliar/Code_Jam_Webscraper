#include<fstream>
using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	fin>>t;
	int ans;
	for(int kk=1;kk<=t;kk++){
		int r,c;
		char m[100][100];
		fin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				fin>>m[i][j];
			}
		}
		ans=0;
		int rn[100],cn[100];
		for(int i=0;i<100;i++){
			rn[i]=0;
			cn[i]=0;
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(m[i][j]!='.'){
					rn[i]++;
					cn[j]++;
				}
			}
		}
		bool can=true;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(m[i][j]!='.'&&rn[i]<2&&cn[j]<2){
					can=false;
					break;
				}
				if(can){
					if(m[i][j]=='^'){
						int k=0;
						for(k=0;k<i;k++){
							if(m[k][j]!='.')break;
						}
						if(k==i){
							ans++;
						}
					}
					else if(m[i][j]=='v'){
						int k=0;
						for(k=i+1;k<r;k++){
							if(m[k][j]!='.')break;
						}
						if(k==r){
							ans++;
						}
					}
					else if(m[i][j]=='<'){
						int k=0;
						for(k=0;k<j;k++){
							if(m[i][k]!='.')break;
						}
						if(k==j){
							ans++;
						}
					}
					else if(m[i][j]=='>'){
						int k=0;
						for(k=j+1;k<c;k++){
							if(m[i][k]!='.')break;
						}
						if(k==c){
							ans++;
						}
					}
				}
			}
		}
		if(can)
			fout<<"Case #"<<kk<<": "<<ans<<endl;
		else
			fout<<"Case #"<<kk<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}