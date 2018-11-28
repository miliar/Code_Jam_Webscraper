#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cstring>
FILE *in = fopen("a-large.in", "r");
FILE *out = fopen("a-large.out", "w");
using namespace std;
int T=0;
int t;
int main(){
    char audi[1111];
    int maxshy;
    int invitation;
    int thresholdAudi;
    int len;
    fscanf(in, "%d", &T);
    t = T;
    while(T--){
        invitation = thresholdAudi = 0;
        fscanf(in, "%d%s", &maxshy, audi);
        len = strlen(audi);
        for(int i=0; i<len; i++){
            if(thresholdAudi < i) {
                invitation += (i - thresholdAudi);
                thresholdAudi = i;
            }
            thresholdAudi += (audi[i] - '0');
        }
        fprintf(out, "Case #%d: %d\n", t - T, invitation);
    }
    return 0;
}
