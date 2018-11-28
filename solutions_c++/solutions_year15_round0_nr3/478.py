#include<stdio.h>
#include<string.h>
#include<algorithm>
#define SIZ 10100
using namespace std;
char left[SIZ*11], right[SIZ*11], c[SIZ*11];
char tonum[200], tochar[8]={'1','i','j','k',-'1',-'i',-'j',-'k'};
char table[4][4]={{'1','i','j','k'},
                {'i',-'1','k',-'j'},
                {'j',-'k',-'1','i'},
                {'k','j',-'i',-'1'}};
int l;
long long x;
char ab(char a){
    return a<0?-a:a;
}
int main(){
    tonum['1']=0;
    tonum['i']=1;
    tonum['j']=2;
    tonum['k']=3;
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int i, j, k;
        scanf("%d %lld %s", &l, &x, c);
        printf("Case #%d: ", tt);
        if(x>=12)x-=4*((x-12)/4+1);
        k=0;
        for(i=0; i<x; i++){
            for(j=0; j<l; j++){
                c[k++]=c[j];
            }
        }
        l=k;
        left[0]=c[0];
        for(i=1; i<l; i++){
            left[i]=table[tonum[ab(left[i-1])]][tonum[c[i]]]*(left[i-1]>0?1:-1);
        }
        right[l-1]=c[l-1];
        for(i=l-2; i>=0; i--){
            right[i]=table[tonum[c[i]]][tonum[ab(right[i+1])]]*(right[i+1]>0?1:-1);
        }
//        printf("\n");for(i=0; i<l; i++){
//            if(left[i]<0)printf("-");
//            printf("%c ",  ab(left[i]));
//        }printf("\n");
//        for(i=0; i<l; i++){
//            if(right[i]<0)printf("-");
//            printf("%c ",  ab(right[i]));
//        }printf("\n");
        for(i=0; i<l-2; i++){
            if(left[i]!='i')continue;
            for(j=i+2; j<l; j++){
                if(right[j]!='k')continue;
                for(k=-4; k<=4; k++){
                    if(k==0)continue;
                    char ss=table[tonum[ab(left[i])]][ab(k)-1]*(left[i]*k>0?1:-1);
                    if(ss==left[j-1])break;
                }
                if(k==3)goto pass;
            }
        }
        printf("NO\n");
        continue;
        pass:;
        printf("YES\n");
    }
    return 0;
}

