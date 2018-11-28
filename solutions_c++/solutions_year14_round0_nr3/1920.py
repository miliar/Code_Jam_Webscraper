#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T,X=1;

    ifstream fin("C-small-attempt3.in");
    ofstream fout("C-small-attempt3.out");

    fin >> T;

    while(T-->0)
    {
        int R,C,M,nonM,countM=0;
        fin >> R >> C >> M;
        nonM = R*C-M-1;
        fout << "Case #" << X++ << ":\n";

        if( ( R*C==M+1 ) || ((R==1 || C==1) && M < R*C) ) { //ak je len jedno volne alebo jedna strana je 1
            for(int i=0;i<R;i++) {
                for(int ii=0;ii<C;ii++) {
                    if(i==0 && ii==0) {
                        fout << "c";
                    } else {
                        if(nonM>0) {
                            fout << ".";
                            nonM--;
                        } else {
                            fout << "*";
                            countM++;
                        }
                    }
                }
                fout << "\n";
            }
        } else {
            if( (R>2 && C>2) && ( (M == (R*C-4)) || (M == (R*C-6)) || (M < (R*C-7)) )) { //ak je kazda strana >2 a sucastne je 4,6,8 a viac volnych
                if(nonM % 2 == 0) { //ak je volnych neparne
                    if( ( (nonM+1)%C > 1 && (nonM+1)%C == 0 ) && nonM+1 > C*2 ) { // ak je volnych viac ako 2 riadky + 1
                        for(int i=0;i<R;i++) {
                            for(int ii=0;ii<C;ii++) {
                                if(i==0 && ii==0) {
                                    fout << "c";
                                } else {
                                    if(nonM>0) {
                                        fout << ".";
                                        nonM--;
                                    } else {
                                        fout << "*";
                                        countM++;
                                    }
                                }
                            }
                            fout << "\n";
                        }
                    } else {
                        int tempC = C;
                        while( !(tempC == 0 || ( ( (nonM+1)%tempC > 1 || (nonM+1)%tempC == 0) && nonM+1 > tempC*2 ))) {
                            tempC--;
                        }
                        if(tempC==1) {
                                for(int i=0;i<R;i++) {
                                    for(int ii=0;ii<C;ii++) {
                                        if(i==0 && ii==0) {
                                            fout << "c";
                                        } else {
                                            if( nonM>0 && !(ii==C-1 && nonM==2 ) ) {
                                                fout << ".";
                                                nonM--;
                                            } else {
                                                fout << "*";
                                                countM++;
                                            }
                                        }
                                    }
                                    fout << "\n";
                                }
                            } else {
                            for(int i=0;i<R;i++) {
                                for(int ii=0;ii<C;ii++) {
                                    if(i==0 && ii==0) {
                                        fout << "c";
                                    } else {
                                        if( nonM>0 && ii < tempC) {
                                            fout << ".";
                                            nonM--;
                                        } else {
                                            if(countM==M) {
                                                fout << ".";
                                                nonM--;
                                            } else {
                                                fout << "*";
                                                countM++;
                                            }
                                        }
                                    }
                                }
                                fout << "\n";
                            }
                        }
                    }

                } else { //ak je volnych parne
                    for(int i=0;i<R;i++) {
                        for(int ii=0;ii<C;ii++) {
                            if(i==0 && ii==0) {
                                fout << "c";
                            } else {
                                if( nonM>0 && (nonM>ii || i!=0) && !(ii==C-1 && nonM==2 ) ) {
                                    fout << ".";
                                    nonM--;
                                } else {
                                    fout << "*";
                                    countM++;
                                }
                            }
                        }
                        fout << "\n";
                    }
                }
            } else {
                if((R==2 || C==2) && nonM>2 && nonM % 2==1  ) {
                    for(int i=0;i<R;i++) {
                        for(int ii=0;ii<C;ii++) {
                            if(i==0 && ii==0) {
                                fout << "c";
                            } else {
                                if( nonM>0 && (nonM>ii || i!=0)) {
                                    fout << ".";
                                    nonM--;
                                } else {
                                    fout << "*";
                                    countM++;
                                }
                            }
                        }
                        fout << "\n";
                    }
                }
                else {
                    fout << "Impossible\n";
                    countM=M;
                }

            }
        }
       /* if(countM!=M) {
            fout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n";
        }*/
    }
    return 0;
}
