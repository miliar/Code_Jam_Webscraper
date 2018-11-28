#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int love[17][2];
int t, T, n;
int R, C;
int status;
int cubemax;
int numcube[35];
int numdir[35];

bool check( int j ) {
    int curcube = numcube[love[j][0]];
    int curdir = numdir[love[j][0]];
    int k;
    while(1) {
            //printf("%d %d\n",curcube,curdir);
    //system("pause");
        if( ((1<<curcube)&(status)) == 0 ) { // 0
            if ( curdir == 1 ) {
                curdir = 2;
            }
            else if ( curdir == 2 ) {
                curdir = 1;
            }
            else if ( curdir == 3 ) {
                curdir = 4;
            }
            else if ( curdir == 4 ) {
                curdir = 3;
            }
        } else { // 1
            if ( curdir == 1 ) {
                curdir = 4;
            }
            else if ( curdir == 2 ) {
                curdir = 3;
            }
            else if ( curdir == 3 ) {
                curdir = 2;
            }
            else if ( curdir == 4 ) {
                curdir = 1;
            }
        }
        //printf("%d %d\n",curcube,curdir);
        for ( k = 1 ; k <= (R+C)*2 ; ++k ) {
            if (curcube == numcube[k] && curdir == numdir[k] ) {
                if ( love[j][1] != k ) {
                    return false;
                }
                else return true;;
            }
        }
        if ( curdir == 1 ) {
            curcube = curcube -C;
            curdir = 3;
        }
        else if ( curdir == 2 ) {
            curcube = curcube +1;
            curdir = 4;
        }
        else if ( curdir == 3 ) {
            curcube = curcube +C;
            curdir = 1;
        }
        else if ( curdir == 4 ) {
            curcube = curcube -1;
            curdir = 2;
        }
    }
}


bool solve() {
    cubemax = (1<<(R*C));
    int i, j, k;

    for ( i = 1 ; i <= C ; ++i ) {
        numcube[i] = i-1;
        numdir[i] = 1;
    }
    numcube[C+1] = numcube[C];//C-1;
    numdir[C+1] = 2;
    for ( i = C+2; i <= C+R ; ++i ) {
        numcube[i] = numcube[i-1]+C;
        numdir[i] = 2;
    }
    numcube[C+R+1] = numcube[C+R];//R*C-1;
    numdir[C+R+1] = 3;
    for ( i = C+R+2 ; i <= C*2+R ; ++i ) {
        numcube[i] = numcube[i-1]-1;
        numdir[i] = 3;
    }
    numcube[C*2+R+1] = numcube[C*2+R];
    numdir[C*2+R+1] = 4;
    for ( i = C*2+R+2 ; i <= (C+R)*2 ; ++i ) {
        numcube[i] = numcube[i-1]-C;
        numdir[i] = 4;
    }

    for ( i = 1 ; i <= (R+C)*2 ; ++i ) {
        //printf("i = %d, %2d %2d\n",i,numcube[i],numdir[i]);
    }

    for ( status = 0 ; status < cubemax ; ++status ) {
        //printf("status = %d\n",status);
        for ( j = 0 ; j < R+C ; ++j ) {
            //printf("j = %d\n",j);
            if ( check(j) == false ) {
                break;
            }
        }
        if ( j == R+C ) return true;
    }
    return false;
}



int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
    int i, j, k;
    for ( t = 1 ; t <= T; ++ t ) {
        printf("Case #%d:\n",t);
        scanf("%d %d",&R,&C);
        n = (R+C)*2;
        for ( i = 0 ; i < (R+C) ; ++i ) {
            scanf("%d %d",&love[i][0],&love[i][1]);
        }
        if ( solve() == true ) {
            for ( i = 0 ; i < R ; ++i ) {
                for ( j = 0 ; j < C ; ++j ) {
                    k = i*C+j;
                    if ( ((1<<k)&(status)) == 0 ) {
                        printf("\\");
                    }
                    else printf("/");
                }
                printf("\n");
            }
        }
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
