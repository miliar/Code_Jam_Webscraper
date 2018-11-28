#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int N,M,K,Q,T;
int R,C;
char map[103][103];

int main(){
	cin>>T;
	for(int cs=1;cs<=T;++cs){
		int res=0;

		cin>>R>>C;
		for(int i=0;i<R;++i)
			cin>>map[i];
		bool rb[103];
		bool cb[103];
		memset(rb, 0, sizeof(rb));
		memset(cb, 0, sizeof(cb));
			
		for(int i=0;i<R;++i){
			int cnt=0;
			for(int j=0;j<C; ++j){
				if(map[i][j]!='.'){
					++cnt;
				}
			}
			if(cnt>1)
				rb[i]=1;
		}
		for(int i=0;i<C;++i){
			int cnt=0;
			for(int j=0;j<R;++j){
				if(map[j][i]!='.')
					++cnt;
			}
			if(cnt>1)
				cb[i]=1;
		}

		for(int i=0;i<R;++i){
			for(int j=0;j<C;++j){
				if(map[i][j]!='.' && !rb[i] && !cb[j]){
					goto wrong;
				}
				switch(map[i][j]){
					case '^':
						for(int k=i-1;k>=0;--k){
							if(map[k][j]!='.')
								goto nxt;
						}
						++res;
						//cout<<i<<' '<<j<<endl;	
						break;
					case 'v':
						for(int k=i+1;k<R;++k){
							if(map[k][j]!='.')
								goto nxt;
						}
						//cout<<i<<' '<<j<<endl;	
						++res;
						break;
    					case '>':
						for(int k=j+1;k<C;++k){
							if(map[i][k]!='.')
								goto nxt;
						}
						//cout<<i<<' '<<j<<endl;	
						++res;
						break;
					case '<':
					    for(int k=j-1;k>=0;--k){
						    if(map[i][k]!='.')
							    goto nxt;
					    }
						//cout<<i<<' '<<j<<endl;	
					    ++res;
					    break;
				}
				nxt:;
			}
		}

		cout<<"Case #"<<cs<<": "<<res<<endl;
		continue;
wrong:
		cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}


