#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <vector>
#include <limits>
#define MAXM 1000000
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, i;
    cin >> T;
    for (i=1; i<=T; i++)
    {
        int N, m;
        int A[MAXM];
        int maxi=0 , sum=0, sum2 = 0;
        cin >> N;
        cin >> A[0];
        for (int i=1; i<N; i++){
            cin >> A[i];
            if (A[i-1]-A[i]>=0){
                maxi = max(maxi, A[i-1]-A[i]);
                sum += A[i-1]-A[i];
            }
        }
        for (int i=0; i<N-1; i++){
            if (A[i]<=maxi)
                sum2+= A[i];
            else
                sum2+= maxi;
        }

        cout <<"Case #" << i << ": " << sum << " " << sum2<<endl;
    }
    return 0;
}
