#include<cstdio>
#include<cstring>

using namespace std;


int main(void){
    int i,j,x=1,y,z,t,n,m;
    char ss[200];

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    while(x<=t){
        scanf("%s",ss);
        m=strlen(ss);
        n=1;
        for(i=1;i<m;i++){
            if(ss[i]!=ss[n-1])    ss[n++]=ss[i];
        }

        y=n-1+((ss[n-1]!='-')?0:1);
        printf("Case #%d: %d\n",x,y);
        x++;
    }
    return 0;
}
