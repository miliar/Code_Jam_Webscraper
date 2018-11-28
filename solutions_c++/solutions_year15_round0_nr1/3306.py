#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

const int MAXN = 100004;

int tnum, n;
char s[1005];

int main(){
    scanf("%d", &tnum);
    
    for (int t=1; t<=tnum; t++){
        scanf("%d%s", &n, s);
        
        int ct = 0, ans = 0;
        for (int i=0; i<=n; i++){
            if (s[i]!='0'){
                if (i>ct){
                    ans += i-ct;
                    ct=i;
                    ct+=s[i]-'0';
                }
                else
                    ct+=s[i]-'0';
            }
        }
        
        printf("Case #%d: %d\n", t, ans);
    }
	return 0;
}
