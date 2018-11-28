#include <cstdio>
#include <cstdlib>
#include<iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int n, v[11];
		string s[11];
		cin >> n;
		for(int i=0;i<n;i++) {
			cin >> s[i];
			v[i]=i;
		}
		int cnt=0;
		do {
	  	bool ja[260], ok = true;
			char ult='#';
			memset(ja,0,sizeof(ja));
			for(int i=0;ok && i<n;i++) {
				for(int j=0;j<sz(s[v[i]]);j++) {
					char c = s[v[i]][j];
					if(ja[(int)c] && ult !=c) {
						ok=false;
						break;
					}
					ult=c;
					ja[c]=true;
				}
			}
			if(ok){
				/*
				for(int i=0;i<n;i++){
						for(int j=0;j<sz(s[v[i]]);j++)
							printf("%c",s[v[i]][j]);
						printf(" ");
				}
				printf("\n");
				*/
				cnt++;
			}
		} while (next_permutation(v,v+n));
		printf("Case #%d: %d\n",caso,cnt);
	}
	return 0;
}
