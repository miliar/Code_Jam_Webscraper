#include <cstdio>
#include <cstdlib>
#include <cstring>

int main(void){
    int t;
    scanf("%d",&t);
    for(int s=1;s<=t;s++){
        char u[11111], v[11111];
        int pt = 5000, pt2 = 5000;
        memset(u,0,sizeof u);
        scanf("%s",v);
        for(int i=0;v[i];i++) if(u[pt] > v[i]) u[pt2++] = v[i]; else u[--pt] = v[i];
        printf("Case #%d: %s\n",s, u+pt);
    }
    return 0;
}

