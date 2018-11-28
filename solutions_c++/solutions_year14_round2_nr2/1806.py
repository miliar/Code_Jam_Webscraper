/*
 *ID:   Cowboy
 *TASK:
 *Judge:
 */
#include <bits/stdc++.h>
#define INF 0x7fffffff
#define PI 2*acos(0.0)
using namespace std;

#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

int main( ){
    freopen("B-small.in","r",stdin);
    freopen("solution.out","w",stdout);
    int T, k = 0, A, B, C, aux;
    long long res;
    for( cin>>T; k<T; k++){

        cin>>A>>B>>C;
        res = 0;
        for( int i = 0 ; i < A ; i++) {
            for( int j = 0 ; j < B ; j++) {
                aux = i&j;
                if( aux < C )
                    res++;
            }
        }

        printf("Case #%d: ", k+1);
        cout<<res<<endl;
    }

return 0;
}
