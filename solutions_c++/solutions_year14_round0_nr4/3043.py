#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
    int t,N;
    double f;
    scanf("%d",&t);
    for(int t1=1;t1<=t;t1++) {
        scanf("%d",&N);
        vector<double> n(N),k(N);
        for(int i=0;i<N;i++) {
            scanf("%llf",&f);
            n[i]=f;
        }
        for(int i=0;i<N;i++) {
            scanf("%llf",&f);
            k[i]=f;
        }
        sort(n.begin(),n.end());
        sort(k.begin(),k.end());
        int i=0,j=0;
        int cnt1=0;
        while((i<N) && (j<N)) {
            if(n[i]<k[j]) {
                i++;
            } else {
                i++;j++;
                cnt1++;
            }
        }
        i=0;
        j=0;
        while((i<N) && (j<N)) {
            if(n[i]<k[j]) {
                i++;j++;
            } else {
                j++;
            }
        }
        printf("Case #%d: %d %d\n",t1,cnt1,N-i);
    }
    return 0;

}
