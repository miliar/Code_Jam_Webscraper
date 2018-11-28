#include <cstdio>
#include <cstring>
#include <algorithm>
#include <math.h>
using namespace std;

int p[10000001] = {0};

int main(void){

    for(int i=1;i<10000001;i++){
        char q[50];
        sprintf(q,"%d",i);
        int qn = strlen(q);
        p[i] = 1;
        for(int j=0,k=qn-1;j<k && p[i];j++,k--)
            if(q[j] != q[k])
                p[i] = 0;
        if(p[i]){
            sprintf(q,"%lld",(long long)i*i);
            qn = strlen(q);
            for(int j=0,k=qn-1;j<k && p[i];j++,k--)
                if(q[j] != q[k])
                    p[i] = 0;
        }
        //if(p[i]) printf("%d ",i);
        p[i] += p[i-1];
    }

    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        char sa[100],sb[100];
        long long a, b;
        scanf("%s%s",&sa,&sb);
        a = atoll(sa);
        b = atoll(sb);
        a = ceil(sqrt(a));
        b = floor(sqrt(b));
        
        printf("Case #%d: %d\n", tt, p[b]-p[a-1]);
    }
    return 0;
}

