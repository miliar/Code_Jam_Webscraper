#include<cstdio>
int a[110][110] ;
bool ch[110][110];
int main(){
    freopen ("B-large.in","r",stdin);
    freopen("2.sol","w",stdout);
    int t =1;
    scanf("%d",&t);
    for(int tt = 1 ; tt <= t ; tt ++){
        int n , m ;
        bool ans = true ;
        scanf("%d %d",&n,&m);
        for(int i = 0 ;  i < n ; i ++)
            for(int j = 0 ; j < m ; j ++)
                scanf("%d",&a[i][j]),ch[i][j] = false ;
        int num = 0 ;

        for(int k = 1 ; k <= 100 ; k ++){

            int x = 0 ,y = 0;
            for(int i = 0 ; i < n ; i ++)
                for(int j = 0 ; j < m ; j ++)
                    if(a[i][j] == k) ch[i][j] = true ,num ++;

            for(int i = 0 ; i < n ; i ++){
                int ct = 0 ;
                for(int j = 0 ; j < m ; j ++)
                    if(ch[i][j]) ct ++ ;
                if(ct == m) x ++;
            }

            for(int i = 0 ; i < m ; i ++){
                int ct = 0 ;
                for(int j = 0 ; j < n ; j ++)
                    if(ch[j][i]) ct ++ ;
                if( ct == n) y ++;
            }
          //  if(k <= 2)printf("!%d %d = %d %d %d\n",k,num,y*n + x*m -x*y,x,y);
            if(num != y*n + x*m -x*y) {
               // printf("%d",k);
                ans = false ;
            }
        }
            if(ans) printf("Case #%d: YES\n",tt);
            else printf("Case #%d: NO\n",tt);
    }
}
