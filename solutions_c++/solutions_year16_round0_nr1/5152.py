#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
bool vis[12];
bool check(long long value){
	while(value > 0){
		vis[value % 10] = 1;
		value /= 10;
	}
	rep(i, 0, 9)if(!vis[i]) return 0;
	return 1;
}
int main(){
	int cas;
	cin >> cas;
	rep(Cas, 1, cas){
		int n;
		cin >> n;
		memset(vis, 0, sizeof(vis));
		printf("Case #%d: ",Cas);
		if(!n)
			printf("INSOMNIA\n");
		else {
			for(int i = 1;;++i){
				long long value = (long long) i * n;
				if(check(value)){
					cout << value << "\n";
					break;
				}
			}		
		}
	}
	return 0;
} 
