#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<string.h>

using namespace std;

#define INF 1000000000;

int cnt[5][5];
int vis[5][5];
int r,c;
int dfs(int i, int j){
	if(vis[i][j]) return 0;
	vis[i][j] = 1;
	for(int p=-1; p <=1; p++){
		for(int q=-1; q<=1; q++){
			if(i+p >= 0 && i+p < r && j+q>=0&&j+q<c){
				if(cnt[i+p][j+q] == 0){
					dfs(i+p,j+q);
				}
			}
		}
	}
	return 0;
}			
int main()
{
	freopen("c.txt","r",stdin);
	int T;cin>>T;
	for(int cn=1;cn<=T;cn++){
		vector<int> vec;
		int m;cin>>r>>c>>m;
		int _min=min(r,c);
                int dots=r*c - m - 1;
                if(dots==0){
			cout << "Case #"<<cn<<":\n";
                        for(int i=0;i<r;i++){
                                for(int j=0;j<c;j++){
                                        if(j==0&&i==0){
                                                cout<<"c";
                                        }else cout<<"*";
                                }
                                cout<<endl;
                        }
			continue;
                }
		bool found = 0;
		int cells=r*c;
		for(int i=0;i<(1<<cells);i++){
			if(__builtin_popcount(i) == m){
				vec.push_back(i);
			}
		}
		
		// prepare grid
		for(int w =0; w < vec.size();w++){
			int n = vec[w];
			char arr[r][c];
                	for(int i = 0; i < r; i++){
                                for(int j=0; j < c; j++){
                                        arr[i][j] = '.';
                                }
                	}
			for(int j=0; j < cells; j++){
				int rn = j/c;
				int cn = j%c;
				if((1<<j) & n){
					arr[rn][cn] = '*';
				}
			}
			// grid with numbers
		//	int cnt[5][5];
                        memset(cnt, 0, sizeof cnt);
                        for(int i = 0; i < r; i++){
                                for(int j=0; j < c; j++){
                                        if(arr[i][j] == '.') {
                                                for(int p=-1; p <=1; p++){
                                                        for(int q=-1;q<=1;q++){
                                                                if(i+p >= 0 && i+p < r && j+q>=0&&j+q<c){
                                                                        cnt[i][j]+=arr[i+p][j+q]=='*';
                                                                }
                                                        }
                                                }
                                        }
                                }
                        }
			
				
			// is this config. good
			bool super_ok = 1;
			//0s connected?
			int flag=1;
			memset(vis, 0, sizeof vis);
			for(int i=0;i<r && flag==1;i++) {
                        	for(int j=0;j<c;j++){
                                	if(arr[i][j] != '*' && cnt[i][j] == 0){
                                        	dfs(i,j);
						flag=0;
                        			break;
					}
				}
			}

			for(int i = 0; i < r; i++){
                                for(int j=0; j < c; j++){
					if(arr[i][j] != '*' && cnt[i][j] == 0){
						if(!vis[i][j]) super_ok = false;
					}
				}
			}

                        for(int i = 0; i < r; i++){
                                for(int j=0; j < c; j++){
                                        if(cnt[i][j] != 0) {
                                                bool all_ok = 0;
                                                for(int p=-1; p <=1; p++){
                                                        for(int q=-1;q<=1;q++){
                                                                if(i+p >= 0 && i+p < r && j+q>=0&&j+q<c){
                                                                        if(arr[i+p][j+q] != '*' && cnt[i+p][j+q] == 0){
                                                                                all_ok=true;
                                                                        }
                                                                }
                                                        }
                                                }
                                                if(!all_ok){
                                                        super_ok = false;
                                                }
                                        }
                                }
                        }
			
			if(super_ok){
				bool first_time=1;
				found = true;
				cout<<"Case #" << cn << ":\n";
				for(int i=0;i<r;i++) {
					for(int j=0;j<c;j++){
						if(arr[i][j] != '*' && cnt[i][j] == 0 && first_time){
							cout<<"c";first_time=0;
						}else
						cout<<arr[i][j];
					}
					cout<<endl;
				}
				break;				
			}

		}
		
		if(!found){
			cout<<"Case #" << cn << ":\n"; cout<<"Impossible\n";
		}
		
	}
}
