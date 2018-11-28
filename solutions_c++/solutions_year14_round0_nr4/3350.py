#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    int T,N,legal = 0,illegal = 0,i,j,k;
    double naomi[1005], ken[1005];

    freopen("D-large.in", "r", stdin);
    freopen("2.out", "w", stdout);

    cin>>T;
    for(i = 1 ; i <= T ; i++) {

        cin>>N;

        for(k = 0 ; k < N ; k++) {
            cin>>naomi[k];
        }

        for(k = 0 ; k < N ; k++) {
            cin>>ken[k];
        }

        sort(ken,ken+N);
        sort(naomi,naomi+N);
        legal = 0;
        for(k = N-1 ,j = N-1; k >= 0 ; k--) {
            if(naomi[k] > ken[j]) {
                legal++;
            } else {
                j--;
            }
          }

        illegal = 0;
        for(k = 0 ,j=0; k < N ; k++) {
            if(naomi[k] > ken[j]) {
                j++;
                illegal++;
            }
        }

       printf("Case #%d: %d %d\n",i,illegal,legal);
    }
    return 0;
}
