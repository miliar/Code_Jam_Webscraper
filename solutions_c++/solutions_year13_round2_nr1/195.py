//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9
#define INF 1023456789

typedef long long ll;
typedef pair<int, int> pii;

int n, a;
int M[200];

int extra(){
    scanf("%d %d",&a,&n);
    For(i,n) scanf("%d",M+i);
    sort(M, M+n);
    M[n] = INF;
    
    if (a == 1) {
        printf("%d\n",n);
        return 0;
    }
    int best = n;
    For(m,n+1){
        int s = a;
        int pos = 0;
        int c = 0;
        while(pos<m){
            if (s>M[pos]) {
                s+=M[pos];
                pos++;
                continue;
            }
            c+=1;
            s+=(s-1);
        }
        best = min(best, n-m+c);
    }
    printf("%d\n",best);    
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
