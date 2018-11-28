#include<stdio.h>
int minusu;
int krat(int a, int b){
    minusu=0;
    if(a>=4){a-=4; minusu++;}
    if(b>=4){b-=4; minusu++;}
    if(minusu==2) minusu=0;
    if(a==0) return (4*minusu+b);
    if(b==0) return (4*minusu+a);
    if(a==b) return (4*(1-minusu));
    if(a>b) minusu++;
    if(minusu==2) minusu=0;
    if(a+b==3) return (4*minusu+3);
    if(a+b==5) return (4*minusu+1);
    if(a+b==4) return (4*(1-minusu)+2);
}
int main(void){
    FILE *fin=fopen("codejam-3.in", "r");
    FILE *fout=fopen("codejam-3.out", "w");
    char Pole[10006];
    char prefixy[10005];
    int T;
    int stav;
    int i; int j;
    long long int L;
    long long int X;
    /*for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%i ", krat(i,j));
        }
        printf("\n");
    }
    return 0;
    */
    //printf("%i\n\n", krat(7,2));
    int obsazene[8];//1, i, j, k, -1, -i, -j, -k
    fscanf(fin,"%i", &T);
    int zrovna;
    int minusy;
    long long int k;
    long long int nejdrivi=1000000000000000000;
    for(i=0;i<T;i++){
        stav=1;
        nejdrivi=1000000000000000000;
        zrovna=0;
        minusy=0;
        for(j=0;j<8;j++){
            obsazene[j]=0;
        }
        fscanf(fin,"%lld %lld",&L, &X);
        fscanf(fin,"%c", &Pole[0]);
        for(j=0;j<L;j++){
            fscanf(fin,"%c", &Pole[j]);
            if(Pole[j]=='i'&&zrovna==1) {zrovna=0;minusy=1-minusy;}
            else if(Pole[j]=='i'&&zrovna==2) {zrovna=3;minusy=1-minusy;}
            else if(Pole[j]=='i'&&zrovna==3) {zrovna=2;}
            else if(Pole[j]=='j'&&zrovna==1) {zrovna=3;}
            else if(Pole[j]=='j'&&zrovna==2) {zrovna=0; minusy=1-minusy;}
            else if(Pole[j]=='j'&&zrovna==3) {zrovna=1;minusy=1-minusy;}
            else if(Pole[j]=='k'&&zrovna==1) {zrovna=2;minusy=1-minusy;}
            else if(Pole[j]=='k'&&zrovna==2) {zrovna=1;}
            else if(Pole[j]=='k'&&zrovna==3) {zrovna=0; minusy=1-minusy;}
            else zrovna=Pole[j]-'i'+1;
            prefixy[j]=4*minusy+zrovna;
            obsazene[4*minusy+zrovna]++;
        }
        /*for(j=0;j<L;j++){
            printf("%i ", prefixy[j]);
        }*/
        //printf("\n");
        if(prefixy[L-1]==0) {fprintf(fout,"Case #%i: NO\n",i+1); }
        else if(prefixy[L-1]!=0&&prefixy[L-1]!=4&&X%4!=2) {fprintf(fout,"Case #%i: NO\n", i+1);}
        else if(prefixy[L-1]==4&&X%2!=1){fprintf(fout,"Case #%i: NO\n",i+1);}
        else{
            for(j=0;j<L;j++){
                zrovna=prefixy[j];
                for(k=0;k<8&&k<X;k++){
                    if(zrovna==1&&k*L+j<nejdrivi) nejdrivi=k*L+j;
                    zrovna=krat(prefixy[L-1], zrovna);
                }
            }
            //printf("nejdrivi%i\n", nejdrivi);
            for(j=0;j<L;j++){
                zrovna=prefixy[j];
                for(k=0;k<8&&k<X;k++){
                    if(k+8<X&&zrovna==3&&(k+8)*L+j>nejdrivi) {fprintf(fout,"Case #%i: YES\n", i+1);stav=0;}
                    if(stav==0) break;
                    if(zrovna==3&&k*L+j>nejdrivi) {fprintf(fout,"Case #%i: YES\n", i+1);stav=0;}
                    zrovna=krat(prefixy[L-1], zrovna);
                    if(stav==0) break;
                }
                if(stav==0) break;
            }
            if(stav==1) fprintf(fout,"Case #%i: NO\n", i+1);
        }
    }
    return 0;
}
