#include<bits/stdc++.h>

using namespace std;

char s[1007];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int tc;
    scanf("%d",&tc);

    for( int cas=1; cas<=tc; cas++ ){

         scanf("%s",s);

         int len = strlen( s );

         int flag = 0;
         char pre = 'A';
         int cnt = 0;


         for(int i=len-1;i>=0;i--){

             if( s[i]=='-' ){
                 flag = 1;
             }

             if( flag ){
                if( pre!=s[i] ) cnt++;
             }

             pre = s[i];
         }
         printf("Case #%d: %d\n",cas,cnt);
    }


    return 0;
}
