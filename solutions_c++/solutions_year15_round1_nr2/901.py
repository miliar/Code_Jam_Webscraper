#include<stdio.h>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
vector<long long int> Pole;
vector<long long int> presne;
int main(void){
    FILE *fin=fopen("B-large.in", "r");
    FILE *fout=fopen("B-large-output.out", "w");
    int i;
    int T;
    int stav;
    long long int N;
    long long int B;
    long long int c;
    long long int u;
    long long int t;
    long long int v;
    long long int j;
    long long int k;
    long long int kolik;
    long long int pocitej;
    long long int res;
    fscanf(fin, "%i", &T);
    for(i=0;i<T;i++){
        Pole.clear();
        presne.clear();
        stav=1;
        fscanf(fin, "%lld %lld", &B, &N);
        for(j=0;j<B;j++){
            fscanf(fin, "%lld", &c);
            Pole.push_back(c);
            presne.push_back(0);
        }
        //printf("%lld\n", N);
        u=100000*N;
        t=0;
        k=0;
        pocitej=0;
        while(t<u){
            k++;
            //if(t!=5||u!=6)printf("%lld %lld %lld\n", t, u,kolik);
            v=(t+u)/2;
            kolik=0;
            pocitej=0;
            stav=1;
            for(j=0;j<B;j++){
                kolik+=(v)/Pole[j]+1;
                if(v%Pole[j]==0) {presne[j]=k; pocitej++;}
            }
            if(kolik<N-1) t=v;
            else if(kolik<N+pocitej){
                for(j=0;j<B;j++){
                    if(pocitej==0) break;
                    if(presne[j]==k&&kolik-pocitej==N-1){
                        fprintf(fout, "Case #%i: %lld\n", i+1, j+1);stav=0; break;
                    }
                    if(presne[j]==k) pocitej--;
                }
                t=v;
            }
            else {
                u=v;
            }
            if(stav==0) break;
        }
    }
    return 0;
}
