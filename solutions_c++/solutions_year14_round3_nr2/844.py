#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

string S[15];
bool Alph[26];
int N,Ans;
void Dfs(int a, int b){
	if(a==b){
		memset(Alph,false,sizeof(Alph));
		for(int i=0; i<N; ++i){
			int Len=S[i].length();
			for(int j=0; j<Len; ++j){
				int X=S[i][j]-'a';
//				printf("%d ",X);
				if(Alph[X]){
					if(j==0){
						int X2=S[i-1][S[i-1].length()-1];
						if(X!=X2-'a') return;
					}
					else if(X!=S[i][j-1]-'a') return;
				}
				else Alph[X]=true;
			}
		}
		++Ans;
		return;
	}
	for(int i=a; i<=b; ++i){
		string tmp=S[a];
		S[a]=S[i]; S[i]=tmp;
		Dfs(a+1,b);
//		for(int i=0; i<N; ++i) cout << S[i] << ' '; cout << endl;
		tmp=S[a];
		S[a]=S[i]; S[i]=tmp;
	}
}

int main(){
	int T; scanf("%d",&T);
	for(int Case=1; Case<=T; ++Case){
		scanf("%d",&N);
		Ans=0;
		for(int i=0; i<N; ++i){
			string tmp;
			cin >> tmp;
			S[i]="";
			S[i]+=tmp[0];
			int Len=tmp.length();
			for(int j=1; j<Len; ++j){
				if(tmp[j]!=tmp[j-1]) S[i]+=tmp[j];
			}
		}
		Dfs(0,N-1);
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
