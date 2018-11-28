#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;
char str[1007];

char flip(char c){
    if (c=='+')
        return '-';
    else
        return '+';
}

void solve(int testi){

    int K;
    scanf("%s%d", str, &K);
    int n = strlen(str);
    int flips = 0;
    for(int i=0; i<=n-K; i++){
        if (str[i]=='-'){
            flips++;
            for(int j=i; j<i+K; j++)
                str[j] = flip(str[j]);
        }
    }
    int ok = 1;
    for(int i=n-K+1; i<n; i++)
        ok &= str[i]=='+';

    if (ok)
        printf("Case #%d: %d\n",testi, flips);
    else
        printf("Case #%d: IMPOSSIBLE\n",testi);
}

int main(){
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++)
        solve(testi);
	return 0;
}
