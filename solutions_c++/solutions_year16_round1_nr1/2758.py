#include <bits/stdc++.h>

using namespace std;

#define fr(i,_a,_b) for(int i = _a, __b = _b; i < __b; i++)
#define fe(i,_a,_b) for(int i = _a, __b = _b; i <= __b; i++)
#define sc1(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define st F
#define nd S
typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int, ii> i3; 
typedef vector<int> vi;
const int inf = 0x3f3f3f3f;
const ll linf = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-8, PI = acos(-1);


#define dbg(x) cerr << ">>> " << x << endl
#define _  << ", " << 


int freq[2566];
bool tem(char c){
	for(int i = c+1; i < 256; i++){
		if(freq[i] > 0) return 1;
	}
return 0;
}


char str[1005];
char ans[1005];
int main(int argc, char const *argv[]){
	int T;
	scanf("%d", &T);


	for(int t = 1; t <= T; t++){
		memset(freq, 0, sizeof freq);
		scanf("%s", str);
		int l = 0;
		for(int i = 0; str[i]; i++){freq[str[i]]++; l++;}
		ans[l] = '\0';
		int a = 0, b = l-1;
		for(int i = l-1; i >= 0; i--){
			if(tem(str[i])){
				ans[b--] = str[i];
			}
			else{
				ans[a++] = str[i];	
			}
			freq[str[i]]--;
		}
		printf("Case #%d: %s\n", t, ans);
	}



	return 0;
}