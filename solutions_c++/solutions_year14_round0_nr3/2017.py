#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int R[241],C[241],M[241];
bool A[51][51];
int counter = 0;

void GoPrint(int R2, int C2, int M2, bool full) {
    for ( int i = 0; i <= R2 ; i++ ){
        for ( int j = 0; j <= C2 ; j++ ){
            if( full ) {
                A[i][j] = false;
            }
            else {
                A[i][j] = true;
            }
        }   
    } 
    int freeSpace = (R2 * C2 ) - M2;
    if( freeSpace >= 1 ) {
        freeSpace -= 1;
        A[1][1] = false;
        if( R2 > 1 && freeSpace >= 1) {
            freeSpace -= 1;
            A[2][1] = false;
        }
        if( C2 > 1 && freeSpace >= 1) {
            freeSpace -= 1;
            A[1][2] = false;
            if( R2 > 1 && freeSpace >= 1) {
                freeSpace -= 1;
                A[2][2] = false;
            }
        }
    }
    if ( full ) {
        freeSpace = 0;
    }
    int fx = 1, fy = 1;
    int limit = 10000000;
    while( freeSpace > 0 && limit-- > 0) {
        //printf("checking at root-1,%d,%d,%d\n",fx,fy,freeSpace);
        if( freeSpace > 3 ) {
            //printf("checking at >3-1,%d,%d,%d\n",fx,fy,freeSpace);
            int setPlace = false;
            while( ( R2 - fx ) >= 1 && limit-- > 0 ){
                if( A[fx][fy] ) { 
                    A[fx][fy] = false;
                    A[fx + 1][fy] = false;
                    freeSpace -= 2;
                    fy++;
                    setPlace = true;
                }
                while( !A[fx][fy] && fy <= C2 && !setPlace && limit-- > 0 ) {
                    if( ( A[fx][fy + 1] ) && ( fy + 1 <= C2 ) ) { 
                        A[fx][fy + 1] = false;
                        A[fx + 1][fy + 1] = false;
                        freeSpace -= 2;
                        fy++;
                        setPlace = true;
                        break;
                    }
                    fy++;
                }
                if( setPlace ) {

                    if( freeSpace <= 3  ) {
                        fx = 1;
                        fy = 1;
                    }
                    break;
                }
                else {
                    fy = 1;
                    fx += 2;
                }
            }
            //printf("checking at >3-3,%d,%d,%d,%d\n",fx,fy,freeSpace,limit);
            if( !setPlace ) {
                while( ( R2 - fx ) == 0 && limit-- > 0 ){
                    //printf("checking at >3-6,%d,%d,%d,%d\n",fx,fy,freeSpace,limit);
                    if( A[fx][fy] ) { 
                        A[fx][fy] = false;
                        freeSpace--;
                        fy++;
                        setPlace = true;
                    }
                    while( !A[fx][fy] && fy <= C2 && !setPlace && limit-- > 0 ) {
                        if( !A[fx][fy + 1] ) {
                            fy++;
                            continue;
                        }
                        else { 
                            A[fx][fy + 1] = false;
                            freeSpace--;
                            fy++;
                            setPlace = true;
                            break;
                        }
                    }
                    if( setPlace ) {

                        if( freeSpace <= 3  ) {
                            fx = 1;
                            fy = 1;
                            break;
                        }
                        fy++;
                        if( fy > C2 )
                        {
                            fy = 1;
                            fx++;
                        }
                    }
                    else {
                        fy = 1;
                        fx++;
                    }
                }
            }
            else {
                if( freeSpace <= 3  ) {
                    fx = 1;
                    fy = 1;
                }
            }
            //printf("checking at >3-2,%d,%d,%d,%d\n",fx,fy,freeSpace,limit);
        } // end of free >= 3
        else if( freeSpace == 3 ) {
            //printf("checking at 3-1,%d,%d,%d\n",fx,fy,freeSpace);
            int setPlace = false;
            while( fx <= R2 && fy <= C2 && !setPlace && limit-- > 0 ) {
                //printf("checking at 3-1,%d%d%d",fx,fy,freeSpace);
                if( !A[fx][fy] ) {
                    fy++;
                }
                else {
                    if( !A[fx + 1][fy - 1]  && fx + 1 <= R2 && fy - 1 > 0 ) {
                        if( ( fy + 1 ) <= C2 && fx != 1 ) {
                            A[fx][fy] = false;
                            A[fx + 1][fy] = false;
                            A[fx][fy + 1] = false;
                            freeSpace -= 3;

                            setPlace = true;
                        }
                        else if ( fx + 1 <= R2 && fy > 3 && A[fx + 1][1] ) {
                            A[fx + 1][1] = false;
                            A[fx + 1][2] = false;
                            A[fx + 1][3] = false;
                            
                            freeSpace -= 3;

                            setPlace = true;
                        }
                        else if ( fx + 2 <= R2 && fy > 3 && A[fx + 2][1] ) {
                            A[fx + 2][1] = false;
                            A[fx + 2][2] = false;
                            A[fx + 2][3] = false;
                            
                            freeSpace -= 3;

                            setPlace = true;
                        }
                        else {
                            A[fx][fy] = false;
                            if( A[fx + 1][1] ) {
                                A[fx + 1][1] = false;
                                A[fx + 1][2] = false;
                                freeSpace -= 2;
                            }
                            else if( fx + 2 <= R2 && A[fx + 2][1] ) {
                                A[fx + 2][1] = false;
                                A[fx + 2][2] = false;
                                freeSpace -= 2;
                            }
                            freeSpace -= 1;

                            setPlace = true;
                        
                        }
                    }
                    else if( fy + 2 <= C2 ) {
                        A[fx][fy] = false;
                        A[fx][fy + 1] = false;
                        A[fx][fy + 2] = false;
                        
                        freeSpace -= 3;

                        setPlace = true;
                    }
                    else if( fx + 2 <= R2 ) {
                        A[fx][fy] = false;
                        A[fx + 1][fy] = false;
                        A[fx + 2][fy] = false;
                        
                        freeSpace -= 3;

                        setPlace = true;
                    }
                    if( setPlace ) {
                        break;
                    }
                    else {
                        fy++;
                    }
                }
                if( fy > C2 ) {
                    fx++;
                    fy = 1;
                }
            }
            if( !setPlace && freeSpace != 0 ) {
                printf("Impossible\n");
                return;
            }
            else {
                fx = 1;
                fy = 1;
            }
        }
        else if( freeSpace <= 2 ) {
            //printf("checking at 2-1,%d,%d,%d,%d\n",fx,fy,freeSpace,limit);
            int setPlace = false;
            while( fx <= R2 && fy <= C2 && !setPlace && limit-- > 0 ) {
                //printf("checking at 2-2,%d,%d,%d,%d\n",fx,fy,freeSpace,limit);
                if( !A[fx][fy] ) {
                    fy++;
                }
                else {
                    if( freeSpace == 2 ) {
                        if( fx == 1 ) {
                            A[fx][fy] = false;
                            if( fx + 1 <= R2 ) {
                                A[fx+1][fy] = false;
                                freeSpace --;
                            }

                            freeSpace -= 1;
                        }
                        else {
                            if( !A[fx + 1][fy - 1]  && fx + 1 <= R2 && fy - 1 > 0 ) {
                                A[fx][fy] = false;
                                A[fx + 1][fy] = false;
                                freeSpace -= 2;
                            }
                            else if( A[fx][fy] ) {
                                A[fx][fy] = false;
                                freeSpace -= 1;
                                if( A[fx][fy + 1] && fy + 1 <= C2 ) {
                                    A[fx][fy + 1] = false;
                                    freeSpace -= 1;
                                }
                                else if( A[fx + 1][fy] && fx + 1 <= R2 ) {
                                    A[fx + 1][fy] = false;
                                    freeSpace -= 1;
                                }
                            }
                        }
                    }
                    else {
                        A[fx][fy] = false;
                        freeSpace -= 1;
                    }
                    setPlace = true;
                    break;
                }
                if( fy > C2 ) {
                    fx++;
                    fy = 1;
                }
            }
        }
    }
    if( freeSpace > 0 ) {
        //error checking
        printf("asdasdasdasfbasdbjkasdkjadjbaskjdbasjkdbkbasdadsbjaskd");
    }
    //printf("free%d\n", freeSpace);
    int R3 = R2;
    while( R3-- ) {
        int x1 = R3 + 1;
        int C3 = C2;
        while( C3-- ) {
            int y1 = C3 + 1;
            if( x1 == 1 && y1 == 1 ) {
                printf("c");
            }
            else if( A[x1][y1] ) {
                printf("*");
                //printf("%d",y1);
            }
            else {
                printf(".");
            }
        }
        printf("\n");
    }
}

void Process(int R1, int C1, int M1) {
    int remain = ( R1 * C1 ) - M1;
    if ( ( R1 * C1 ) - 1 == M1 ) {
        GoPrint(R1, C1, M1, false);
    }
    else if ( M1 == 0) {
        GoPrint(R1, C1, M1, true);
    }
    else if( ( ( R1 == 2 || C1 == 2 ) && M1 % 2 == 1 ) ||
            ( ( remain == 5 || remain == 7 ) && ( R1 > 1 && C1 > 1 ) )
        ) {
        printf("Impossible\n");
        return;
    }
    else if( R1 <= 2 && C1 <= 2 && M1 > 0 ) {
        printf("Impossible\n");
        return;
    }
    else if( ( ( R1 > 2 || C1 > 2) && R1 * C1 >= 6 ) &&  ( ( R1 * C1 ) - M1   ) < 4 ) {
        printf("Impossible\n");
        return;
    }
    else if( ( ( R1 > 2 || C1 > 2) && R1 * C1 < 6 ) &&  ( ( R1 * C1 ) - M1   ) < 2 ) {
        printf("Impossible\n");
        return;
    }
    else {
        GoPrint(R1,C1,M1, false);
    }
    return;
}
void make1( int nt ) {
    scanf("%d %d %d", &R[nt], &C[nt], &M[nt]);
}
void make() {
    ++counter;
    printf("Case #%d:\n", counter);
    Process(R[counter - 1],C[counter - 1],M[counter - 1]);
    //printf("%10.7f\n", T);
}

int main() {
    int t,t2; scanf("%d", &t);
    t2 = 0;
    while(t2 < t) {
        make1(t2);
        t2++;
    }
    while(t--) {
        make();
    }
    return 0;
}
