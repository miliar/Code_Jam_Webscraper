#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I=0;I<N;I++){

        int NC;
        scanf("%d",&NC);
        double Nao[NC],Ken[NC],Rest=0.0000001,Bought[NC*2];

        for(int J=0;J<NC;J++){
            scanf("%lf",&Nao[J]);
            Bought[J]=Nao[J];
        }
        for(int J=0;J<NC;J++){
            scanf("%lf",&Ken[J]);
            Bought[J+NC]=Ken[J];
        }

        sort(Nao,Nao+NC);
        sort(Ken,Ken+NC);
        int i=0,j=0,sum1=0,sum2=0;
        for(int J=0;J<NC;J++){
            if(Nao[i]<Ken[j]){
                i++;
            }
            else{
                if(Nao[i]>Ken[j]){
                    i++;j++;sum1++;
                }
            }
        }
        i=NC-1;
        j=NC-1;
        for(int J=0;J<NC;J++){
            if(Nao[i]>Ken[j]){
                i--;
                sum2++;
            }
            else{
                if(Ken[j]>Nao[i]){
                    j--;
                    i--;
                }
            }
        }
        printf("Case #%d: %d %d\n",I+1,sum1,sum2);
    }
    fclose(stdout);
}
