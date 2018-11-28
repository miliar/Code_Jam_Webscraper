#include<cstdio>

int T,t;
int N,M;
int i,j,k;
int arr[105][105];
bool ok;

int main(){
 FILE *fin,*fout;
 fin = fopen("B-large.in","r");
 fout = fopen("B-large.out","w");
 fscanf(fin,"%d",&T);
 for(t=1;t<=T;t++){
    fscanf(fin,"%d%d",&N,&M);
    for(i=0;i<N;i++) for(j=0;j<M;j++) fscanf(fin,"%d",&arr[i][j]);
    ok = true;
    for(i=0;i<N && ok;i++){
        for(j=0;j<M && ok;j++){
            ok = false;
            for(k=0;k<N;k++) if(arr[k][j]>arr[i][j]) break;
            if(k==N) ok=true;
            for(k=0;k<M;k++) if(arr[i][k]>arr[i][j]) break;
            if(k==M) ok=true;
        }
    }
    if(ok) fprintf(fout,"Case #%d: YES\n",t);
    else fprintf(fout,"Case #%d: NO\n",t);
 }


 return 0;
}
