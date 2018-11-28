#include <cstdio>
#include <algorithm>
using namespace std;
int numR,numP,numS,cnt;
char s[1<<13];
void init()
{
    numR = numP = numS = cnt = 0;
}
void dfs(int dep, int c) {
    //printf("###%d %d\n",dep, c);
    if(dep == 0) {
        if(c == 0) {
            ++numR;
            s[cnt++] = 'R';
        }
        else if(c == 1){
            ++numP;
            s[cnt++] = 'P';
        }
        else {
            ++numS;
            s[cnt++] = 'S';
        }
        return;
    }
    if(c == 0) {
        dfs(dep - 1, 0);
        dfs(dep - 1, 2);
    }
    else if(c == 1) {
        dfs(dep - 1, 1);
        dfs(dep - 1, 0);
    }
    else {
        dfs(dep - 1, 1);
        dfs(dep - 1, 2);
    }
}
int cmp(int l,int r)
{
    int d = r - l;
    for(int i = l; i < r; ++i) {
        if(s[i] > s[i+d])
            return 1;
    }
    return 0;
}
void adjust(int x, int N) {
    for(int i = 0; i < 1 << N; i += 1 << (x + 1)) {
        if(cmp(i, i + (1 << x))) {
            for(int j = i; j < (i + (1 << x)); ++j)
                swap(s[j],s[j+(1<<x)]);
        }
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,N,R,P,S;
    scanf("%d",&T);
    for(int casei = 1; casei <= T; ++casei) {
        scanf("%d%d%d%d",&N,&R,&P,&S);
        s[1<<N] = '\0';
        init();
        dfs(N, 0);
        if(numR == R && numP == P && numS ==S) {
            for(int i = 0; i < N; ++i)
                adjust(i, N);
            printf("Case #%d: %s\n",casei,s);
            continue;
        }
        init();
        dfs(N, 1);
        //printf("@@@ %d %d %d\n",numR,numP,numS);
        if(numR == R && numP == P && numS ==S) {
            for(int i = 0; i < N; ++i)
                adjust(i, N);
            printf("Case #%d: %s\n",casei,s);
            continue;
        }
        init();
        dfs(N, 2);
        if(numR == R && numP == P && numS ==S) {
            for(int i = 0; i < N; ++i)
                adjust(i, N);
            printf("Case #%d: %s\n",casei,s);
            continue;
        }
        printf("Case #%d: IMPOSSIBLE\n",casei);
    }
    return 0;
}
