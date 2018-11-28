#include <cstdio>
#include <cstring>
using namespace std;

int a[5][5];
bool b[20];

void solve (int test){
     int res1, res2;
     scanf ("%d",&res1);
     for (int i=0;i<4;++i){
         for (int j=0;j<4;++j){
             scanf ("%d",&a[i][j]);
             if ( i+1 == res1 ) b[ a[i][j] ] = 1;
         }
     }
     
     scanf ("%d",&res2);
     int cnt = 0;
     int sol;
     
     for (int i=0;i<4;++i){
         for (int j=0;j<4;++j){
             scanf ("%d",&a[i][j]);
             if ( i+1 == res2 ){
                if ( b[ a[i][j] ] == 1 ){
                   ++cnt;
                   sol = a[i][j];     
                }
             }
         }
     }
     
     printf ("Case #%d: ",test);
     if (cnt == 0) printf ("Volunteer cheated!\n");
     else if (cnt>1) printf ("Bad magician!\n");
     else printf ("%d\n",sol);
     
     memset( b, 0 , sizeof(b) );
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve (i+1);
    }
    return 0;
}
