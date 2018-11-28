#include<cstdio>
#define N 1000

int n,a[N+5];
int cnt;


int is_ok(int x){
    int i;
    cnt=0;
    for(i=0;i<n;i++){
        cnt +=a[i]/x;
        if(a[i]%x==0) cnt--;
    }
    return cnt;
}

int main(void){
    int i,j,x,y,z;
    int t;
    FILE *in,*out;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&t);
    for(i=1;i<=t;i++){
        fscanf(in,"%d",&n);
        z=0;
        for(j=0;j<n;j++) {
            fscanf(in,"%d",&a[j]);
            z=z>a[j]?z:a[j];
        }

        y=20000;
        for(j=1;j<=z;j++){
            x=is_ok(j);
            if(j+x<y) y=j+x;
        }
        fprintf(out,"Case #%d: %d\n",i,y);
    }

    return 0;

}

