
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream cout ("B-large.out");
	ifstream cin ("B-large.in");
	int t=0;
	int n,m;
	while(cin>>t){
	for(int cnt=0;cnt<t;cnt++){
		cin>>n>>m;
		int grass[n][m];
		int ans=1;
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>grass[i][j];
			}
		}
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				int bl0=0,bl1=0;
				for(int k=0;k<n;k++){
					if(grass[k][j]>grass[i][j]){
					bl0=1;
					break;
					}
				}
				for(int k=0;k<m;k++){
					if(grass[i][k]>grass[i][j]){
					bl1=1;
					break;
					}
				}
				if(bl0&&bl1)ans=0;
			}
		}
		cout<<"Case #"<<cnt+1<<": "<<(ans?"YES":"NO")<<endl;
	}
	}
    return 0;
}
