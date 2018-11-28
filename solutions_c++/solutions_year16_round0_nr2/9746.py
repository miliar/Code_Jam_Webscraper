#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int S = 200;
char in[S], curr;
int ans, n, i;

int tc, tcn;
int main(){
    scanf(" %d", &tc);
    while(tc--){
        scanf(" %s", in);
        n = strlen(in);
        ans = 0;
        for(int i=1;i<n;i++)
            ans += (in[i] != in[i-1]);
        if(in[n-1] == '-') ans++;
        printf("Case #%d: %d\n", ++tcn, ans);
    }
}
