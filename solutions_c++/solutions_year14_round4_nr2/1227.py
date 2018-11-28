#include <bits/stdc++.h>
using namespace std;

int a[1111] , p[1111] , c[1111];
int main(){

 freopen("in.c","r",stdin);
 freopen("salida.c","w",stdout);

    int tc , n , nc = 1;
    cin >> tc;

    while(tc--){
        cin >> n;
        int maxi = 0;
        for(int i = 0; i < n; ++i)
            scanf("%d",&a[i]) , maxi = max(maxi,a[i]);

        for(int i = 0; i < n; ++i)
            p[i] = i;

        int res = 1<<30;
        do{     int pos = -1;
                for(int i = 0; i < n; ++i)
                    if(a[p[i]] == maxi) pos = i;

                bool valid = 1;
                for(int i = 0; i < pos; ++i)
                    if( a[p[i]] > a[p[i+1]] ) valid = 0;
                for(int i = pos + 1; i < n; ++i )
                    if( a[p[i]] > a[p[i-1]]) valid = 0;

                if(valid){
                      map<int,int> idx;
                      for(int i = 0; i < n; ++i)
                        c[i] = 0;
                      for(int i = 0; i < n; ++i)
                            idx[a[p[i]]] = i;

                      int parcial = 0;
                      for(int i = 0; i < n; ++i)
                      {
                          for(int j = idx[a[i]]; j < n; ++j)
                            parcial += c[j];
                        c[idx[a[i]]] = 1;
                      }

                    res = min(res,parcial);
                }

        }while(next_permutation(p,p+n));

        printf("Case #%d: %d\n",nc++,res);
    }






    return 0;
}

