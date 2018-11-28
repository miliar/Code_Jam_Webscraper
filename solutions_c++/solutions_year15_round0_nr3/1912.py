#include<cstdio>
#define N 10000

int n,m;
char s[N+5];
char t[N+5][N+5],t1[N+5][N+5];
int tt[N+5],tt1[N+5];

void trans(int i,int j,char x,char y){
    int w;

    if(x==1){
        t[i][j]=y;
        t1[i][j]=t1[i][j-1];
        return ;
    }

    if(x==y){
        t[i][j]=1;
        t1[i][j]=t1[i][j-1]*(-1);
    }
    if(x=='i' && y=='j'){
        t[i][j]='k';
        t1[i][j]=t1[i][j-1];
    }else if(x=='i' && y=='k'){
        t[i][j]='j';
        t1[i][j]=t1[i][j-1]*(-1);
    }else if(x=='j' && y=='i'){
        t[i][j]='k';
        t1[i][j]=t1[i][j-1]*(-1);
    }else if(x=='j' && y=='k'){
        t[i][j]='i';
        t1[i][j]=t1[i][j-1];
    }else if(x=='k' && y=='i'){
        t[i][j]='j';
        t1[i][j]=t1[i][j-1];
    }else if(x=='k' && y=='j'){
        t[i][j]='i';
        t1[i][j]=t1[i][j-1]*(-1);
    }
}

int main(void){
    int i,j,x,y,z,k;
    int test;
    char ss[N+5];
    FILE *in,*out;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&test);
    for(i=1;i<=test;i++){
        fscanf(in,"%d %d",&n,&m);
        fscanf(in,"%s",ss);
        x=0;
        for(j=0;j<m;j++){
            for(k=0;k<n;k++){
                s[x++]=ss[k];
            }
        }

        n=m*n;
        s[x]=0;
       // printf("%s : ",s);
        for(j=0;j<n;j++){
            t[j][j]=s[j];
            t1[j][j]=1;
            for(k=j+1;k<n;k++){
                trans(j,k,t[j][k-1],s[k]);
            }
        }

        //printf("%d %d\n",t[0][n-1],t1[0][n-1]);
        //continue;

        if(t[0][n-1]!=1 || t1[0][n-1]!=-1){
            fprintf(out,"Case #%d: NO\n",i);
            continue;
        }

        for(j=0;j<n;j++){
            if(t[0][j]=='i') break;
        }
        x=j;
        for(j=n-1;j>=0;j--){
            if(t[j][n-1]=='k') break;
        }
        y=j;

        if(x<y){
            fprintf(out,"Case #%d: YES\n",i);
        }else{
            fprintf(out,"Case #%d: NO\n",i);
        }

    }

    return 0;

}
