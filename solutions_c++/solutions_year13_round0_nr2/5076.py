#include<stdio.h>
#include<stdlib.h>

struct vect{
int x,y;
int s[100][100];
};

int linie(int x,int y,int v[100][100],int a,int b){
    int i;
for (i=0;i<y;i++){
    if (v[a][i]>v[a][b]) return 1;
}
  return 0;
}

int coloana(int x,int y,int v[100][100],int a,int b){
    int i;
for (i=0;i<x;i++){
    if (v[i][b]>v[a][b]) return 1;
}
  return 0;
}

int main()
{


    vect v;
    int i,j,k;

    FILE *f,*fo;
f=fopen("input.txt","r");
    fo=fopen("output.txt","w");

    int n;
    fscanf(f,"%d ",&n);

    for (i=0;i<n;i++){
        fscanf(f,"%d ",&v.x);
        fscanf(f,"%d ",&v.y);

        for (j=0;j<v.x;j++){
            for (k=0;k<v.y;k++){
                fscanf(f,"%d",&v.s[j][k]);
            }
        }
            int ct=0;
        for (j=0;j<v.x;j++){
            for (k=0;k<v.y;k++){
                 if ((linie(v.x,v.y,v.s,j,k)==1) &&  (coloana(v.x,v.y,v.s,j,k)==1)) {ct=1;break;}
            }
            if (ct==1) break;
        }
       if (ct==1) fprintf(fo,"Case #%d: NO\n",i+1);
       else fprintf(fo,"Case #%d: YES\n",i+1);
    }

}
