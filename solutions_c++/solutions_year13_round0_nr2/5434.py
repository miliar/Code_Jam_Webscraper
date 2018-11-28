// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;
#define ll long long
int main(){

	int T;
	cin>>T;

	for(int _t=1;_t<=T;++_t){

		int N,M;
		cin>>N>>M;

		vector <vector <int> > a;
		a.resize(N);

		for(int i=0;i<N;++i){
			a[i].resize(M);
			for(int j=0;j<M;++j){
				cin>>a[i][j];
			}
		}

		vector <int> hr[101],hc[101];
	
		for(int i=0;i<N;++i){
			for(int j=0;j<M;++j){
				hr[a[i][j]].push_back(i);
				hc[a[i][j]].push_back(j);
			}
		}

		int visited[N][M];
		memset(visited,0,sizeof(visited));

		bool ok=true;
		for(int h=1;h<=100;++h){
			for(int i=0;i<hr[h].size();++i){
				int r=hr[h][i];
				int c=hc[h][i];
				if(visited[r][c])continue;
			
				bool vok=true,hok=true;
				for(int j=0;j<N;++j){
					if(a[j][c]>h)vok=false;
				}
				for(int j=0;j<M;++j){
					if(a[r][j]>h)hok=false;
				}
				
				if(vok){
					for(int j=0;j<N;++j)visited[j][c]=1;
				}
				if(hok){
					for(int j=0;j<M;++j)visited[r][j]=1;
				}
			
				if(!vok&&!hok){
					ok=false;
					break;
				}
			}
			if(!ok)break;
		}
		if(ok){
			cout<<"Case #"<<_t<<": YES"<<endl;
		}else{
			cout<<"Case #"<<_t<<": NO"<<endl;
		}
	}
	
}



