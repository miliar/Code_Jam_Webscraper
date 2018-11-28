#include<stdio.h>
#include<algorithm>
#include<cstring>

using namespace std;

int ap[20];

int main () {
    
    int tests;
    scanf("%d",&tests);
    
    for ( int ii = 1 ; ii <= tests ; ++ii ){
        
        int row,x;
        scanf("%d",&row);
        for ( int i = 1 ; i <= 4 ; ++i ){
            for ( int j = 1 ; j <= 4 ; ++j ){
                scanf("%d",&x);
                if ( i == row ){
                    ++ap[x];
                }
            }
        }
        scanf("%d",&row);
        for ( int i = 1 ; i <= 4 ; ++i ){
            for ( int j = 1 ; j <= 4 ; ++j ){
                scanf("%d",&x);
                if ( i == row ){
                    ++ap[x];
                }
            }
        }

        int sol = 0,multiplesol = 0;
        for ( int i = 1 ; i <= 16 ; ++i ){
            if ( ap[i] == 2 ){
                if ( !sol ) sol = i;
                else        multiplesol = 1;
            }
        }
        
        printf("Case #%d: ",ii);
        if ( !sol ){
             printf("Volunteer cheated!\n");
        }
        else{
            if ( multiplesol ){
                printf("Bad magician!\n");
            }
            else{
                printf("%d\n",sol);
            }
        }

        memset(ap,0,sizeof(ap));
    }
}
