#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

char Z[15];
int T[15], M[15], E[35], casos, ctos, ser, res, grande, formas, todas, m, mi, hay, va;
int L[35][500000];
string A[15], B[15][15];

void aslo(int dnde){
    if(dnde<=ctos){
        for(int i=1; i<=ser; i++){
            ++T[i];
            B[i][T[i]]=A[dnde];
            aslo(dnde+1);
            --T[i];
        }
    }
    else {
        for(int i=1; i<=ser; i++){
            if(T[i]==0)
                return ;
        }
        m=0;
        for(int i=1; i<=ser; i++){
            ++m;
            hay=1;
            for(int e=1; e<=T[i]; e++){
                va=1;
                for(int c=0; c<B[i][e].size(); c++){
                    if(L[B[i][e][c]-'A'][va]==0){
                        ++m;
                        ++hay;
                        L[B[i][e][c]-'A'][va]=hay;
                        va=hay;
                    }
                    else {
                        va=L[B[i][e][c]-'A'][va];
                    }
                }
            }
            for(int i=1; i<=hay; i++){
                for(int e=0; e<30; e++){
                    L[e][i]=0;
                }
            }
        }
        if(m>grande){
            grande=m;
            formas=1;
        }
        else if(m==grande)
            ++formas;
    }
}

int main()
{
    freopen("ji.in","r",stdin);
    freopen("jo.out","w",stdout);
    scanf("%d",&casos);
    for(int v=1; v<=casos; v++){
        grande=0;
        formas=0;
        todas=0;
        scanf("%d%d",&ctos,&ser);
        for(int i=1; i<=ctos; i++){
            scanf("%s",Z);
            A[i]=Z;
            todas+=A[i].size();
        }
        for(int i=1; i<=ser; i++){
            T[i]=0;
        }
        aslo(1);
        printf("Case #%d: %d %d\n",v,grande,formas);
    }
    return 0;
}
