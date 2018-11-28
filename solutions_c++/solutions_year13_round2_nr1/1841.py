#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>


#define MAX 110

using namespace std;

typedef long long int ll;


int t,N,aux;
ll A;
ll v[MAX];

int main(){

    freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);

    scanf("%d",&t);

    for(int caso=1;caso<=t;caso++){

        scanf("%I64d %d",&A,&N);

        for(int i=0;i<N;i++){
            scanf("%I64d",&v[i]);
        }
        sort(v,v+N);

        int resp=0;
        for(int i=0;i<N;i++){

            if(v[i] < A){
                A=A+v[i];
            }
            else {

                if(2*A-1 > v[i]){
                    A=2*A-1;
                    A+=v[i];
                    resp++;
                    continue;
                }

                int menor=N-i;
                int cont=0;
                int prox=i;

                for(int j=i;j<N;j++){
                    cont++;
                    A=2*A-1;
                    int k;
                    for(k=prox;k<N;k++){
                        if(A > v[k]){
                            A+=v[k];
                        }else break;
                    }

                    prox=k;

                    for(k=N-1;k>=j;k--){
                        if(  v[k] < A){
                            menor=min(menor,cont+(N-1-k));
                            break;
                        }
                    }
                }
                resp+=menor;
                break;
            }
        }

        printf("Case #%d: %d\n",caso,resp);

    }

    return 0;
}
