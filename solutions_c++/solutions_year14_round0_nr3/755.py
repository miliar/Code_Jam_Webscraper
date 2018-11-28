#include <cstdlib>
#include <iostream>
#include "set"
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    
    int R,C,M;
    int XX[50][50];


	int y;
    for (int T_i=0; T_i<T;T_i++){
        cin >> R >> C >> M;
        
        if (R*C-M==1)
        {
        cout << "Case #" << T_i+1 << ": " << endl;
                      for (int j=0; j < R; j++) {
                          for (int i=0; i < C; i++) {
                                  if ((j== R-1) && (i == C-1)) cout << "c"; else cout << "*";
                          }
                          cout << endl;
                      }
        }
        else 
        if ((R==1) || (C==1)) {
        if (R*C - M <2) {
        cout << "Case #" << T_i+1 << ":" << endl << "Impossible"<< endl;
                } else {
        cout << "Case #" << T_i+1 << ": " << endl;
                      for (int j=0; j < R; j++) {
                          for (int i=0; i < C; i++) {
                              if (M>0) {
                                 cout << "*";
                                 M--;
                              } else {
                                  if ((j== R-1) && (i == C-1)) cout << "c"; else cout << ".";
                              }
                          }
                          cout << endl;
                      }
                }
        
        } 
        else {

        int MM;
        if (R*C - M <4) {
        cout << "Case #" << T_i+1 << ":" << endl << "Impossible"<< endl;
                } else {
        cout << "Case #" << T_i+1 << ": " << endl;
                    
                if (((C ==2) || (R==2)) && (((C*R)-M) % 2 == 1))  {
                       cout <<"Impossible"<< endl;
                } else if (((C*R)-M <9) and (((C*R)-M) % 2 == 1)) {
                       cout <<"Impossible"<< endl;
                } else {

             for (int j=0; j < R-3;j ++) {
             if (M >= C) MM = C; else {
                   if (M < C-2) MM = M; else MM=C-2;
                }
             for (int i=0;i < C;i++){
                 if (MM >0) {
                       cout << "*";
                       MM--;
                       M--;
                    } else {
                       cout << ".";
                           }
             } 
             cout << endl;
             }

             if (R>=3) {
             if (M >= C) MM = C; else {
                   if (M < C-2) MM = M; else MM=C-2;
                }
             if ((M-MM)%2 != 0) if (MM==C) MM=MM-3; else MM--;
             
             for (int i=0;i < C;i++){
                 if (MM >0) {
                       cout << "*";
                       MM--;
                       M--;
                    } else {
                       cout << ".";
                           }
             } 
             cout << endl;
             }


             MM = (int)ceil(M/2);
             for (int i=0;i < C;i++){
                 if (MM >0) {
                       cout << "*";
                       MM--;
                       M--;
                    } else {
                       cout << ".";
                           }
             } 
             cout << endl;
             for (int i=0;i < C;i++){
                 if (M >0) {
                       cout << "*";
                       M--;
                    } else {
                       if (i==C-1) 
                       cout << "c"; else cout << ".";
                           }
             } 
             cout << endl;

                       
             
                    
             }

                }
             }
        
    }
    return EXIT_SUCCESS;
}
