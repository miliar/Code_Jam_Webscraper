#include <iostream>
#include <cstring>
#include <cmath>
#define N 10000001
using namespace std;
int f[N];
int dig[15];

void getArray(){
    long long y;
    int len;
    for (int i=0; i<N; i++){
        f[i] = 1;
        y = i;
        len = 0;
        while (y>0){
            dig[len++] = y%10;
            y/=10;
        }
        for (int j=0; j<len; j++){
            if (dig[j]!=dig[len-1-j]) f[i]=0;
            break;
        }
        if (f[i]==0) continue;
        y = (long long) i * (long long) i;
        len = 0;
        while (y>0){
            dig[len++] = y%10;
            y/=10;
        }
        for (int j=0; j<len; j++)
            if (dig[j]!=dig[len-1-j]){
                f[i] = 0;
                break;
            }
    }
    for (int i=1; i<N; i++) f[i] = f[i]+f[i-1];
  //  for (int i=0; i<33; i++) cout<<i<<' '<<f[i]<<endl;
}

int getCnt(long long A){
    long long mid, l, r;
    l = 0; r = N-1;
    if (r*r<=A) return f[N-1];
    while (l<r){
        mid = (l+r)/2;
        if (mid*mid > A) r = mid;
        else l = mid+1;
    }
    return f[r-1];
}

int main(){
    int tc;
    int A, B;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    getArray();
    scanf("%d", &tc);
    for (int tt=1; tt<=tc; tt++){
        printf("Case #%d: ", tt);
        cin>>A>>B;
        A = A-1;
        int y = getCnt(B);
        int x = getCnt(A);
        printf("%d\n", y-x);
    }
    return 0;
}
        
    
    
