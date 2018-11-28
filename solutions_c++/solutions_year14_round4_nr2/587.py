#include <cstdio>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

int A[1005], E[1005], casos, ctos, van, izq, der, res;
map<int, int> M;

int main()
{
    freopen("ji.in","r",stdin);
    freopen("jo.out","w",stdout);
    scanf("%d",&casos);
    for(int v=1; v<=casos; v++){
        M.clear();
        res=0;
        scanf("%d",&ctos);
        for(int i=1; i<=ctos; i++){
            scanf("%d",&A[i]);
            M[A[i]]=i;
        }
        van=0;
        for(map<int, int>::iterator it=M.begin(); it!=M.end(); it++){
            ++van;
            A[it->second]=van;
            E[van]=it->second;
        }
        izq=1;
        der=ctos;
        for(int i=1; i<=van; i++){
            if(E[i]-izq<der-E[i]){
                for(int e=E[i]; e!=izq; e--){
                    swap(E[A[e-1]], E[A[e]]);
                    swap(A[e-1], A[e]);
                    ++res;
                }
                ++izq;
            }
            else {
                for(int e=E[i]; e!=der; e++){
                    swap(E[A[e+1]], E[A[e]]);
                    swap(A[e], A[e+1]);
                    ++res;
                }
                --der;
            }

        }
        printf("Case #%d: %d\n",v,res);
    }
    return 0;
}
