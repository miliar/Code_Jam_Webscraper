#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 1010
double Nao[MAXN],Ken[MAXN];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
  //  freopen("test.txt","r",stdin);
    int T;scanf("%d",&T);
    for(int cas = 1; cas <= T;cas++){
        int N;scanf("%d",&N);
        for(int i = 0; i < N; i++)
            scanf("%lf",&Nao[i]);
        for(int i = 0; i < N; i++)
            scanf("%lf",&Ken[i]);
        sort(Nao, Nao + N);
        sort(Ken, Ken + N);
//        for(int i = 0; i < N;i++)
//            cout<<Nao[i]<<' ';
//        cout<<endl;
//        for(int i = 0; i < N;i++)
//            cout<<Ken[i]<<' ';
//        cout<<endl;
        int p = 0,s1 = 0;
        for(int i = 0; i < N; i++){
            while(p < N && Ken[p] < Nao[i]) p++;
            if(p < N){
                s1++;
                p++;
            }
            else break;
        }
        int s2 = 0;p = 0;
        for(int i = 0; i < N; i++){
            while(p < N && Nao[p] < Ken[i]) p++;
            if(p < N){
                s2++;
                p++;
            }
            else break;
        }
        printf("Case #%d: ",cas);
        printf("%d %d\n",s2,N - s1);
    }

    return 0;
}
