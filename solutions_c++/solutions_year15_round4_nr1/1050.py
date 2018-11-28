#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
	
int main(){
	int TT;
	cin>>TT;
	int ans=0;

	char map[200][200];
	int rc[200];
	int cc[200];
	for(int T=1;T<=TT;++T){
		int r,c;
		cin>>r>>c;
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				cin>>map[i][j];
			}
		}
		for(int i=0;i<r;++i){
			rc[i]=0;
			for(int j=0;j<c;++j){
				if(map[i][j]!='.')
					rc[i]+=1;
			}
		}
		for(int j=0;j<c;++j){
			cc[j]=0;
			for(int i=0;i<r;++i){
				if(map[i][j]!='.')
					cc[j]+=1;
			}
		}
		ans=0;
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				if(map[i][j]!='.'){
					if(map[i][j]=='<'){
						++ans;
					}
					break;
				}
			}
			for(int j=c-1;j>=0;--j){
				if(map[i][j]!='.'){
					if(map[i][j]=='>'){
						++ans;
					}
					break;
				}
			}
		}
		for(int j=0;j<c;++j){
			for(int i=0;i<r;++i){
				if(map[i][j]!='.'){
					if(map[i][j]=='^'){
						++ans;
					}
					break;
				}
			}
			for(int i=r-1;i>=0;--i){
				if(map[i][j]!='.'){
					if(map[i][j]=='v'){
						++ans;
					}
					break;
				}
			}
		}
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				if(map[i][j]!='.'&&rc[i]<=1&&cc[j]<=1){
					ans=-1;
					break;
				}
			}
		}
		
		if(ans>=0)
		cout<<"Case #"<<T<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<"\n";


	}
	return 0;
}
