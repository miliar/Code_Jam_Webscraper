#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;
    set <long> BB;
    set <long>::iterator BBi;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    long A;
    long N;
    long Aa;
    int RR;
    int RR2;
    int A2;
    cin >> T;
    int iN;
    int found;
    
    char Used[1000000];
    long NNN[100];
    
    for (int i=0; i<T ;i++){
        BB.clear();
        
        for (int j=0; j<1000000; j++){
            Used[j]='o';
        }
        
        cin >> A>> N;
        iN = 0;
        for (int j=0; j < N;j++){
            cin >> Aa;
            NNN[iN] = Aa;
            iN++;
//            BB.insert(Aa);
            Used[Aa] = 'x';
        }
        Used[A] = 'x';
        for (int j=0; j< N-1;j++){
            for (int k=j+1;k<N;k++){
                if (NNN[j]>NNN[k]) {Aa= NNN[j];NNN[j]=NNN[k];NNN[k]=Aa;}
            }
        }
        
        
        RR = 0;
        
        for (int BBi= 0; BBi < N && iN !=0 ; BBi++){
            if (NNN[BBi] < A) {A=A+ NNN[BBi]; iN --;}
            else {
                 RR2 = 0;
                 A2 = A;
                 while ((A2 <= NNN[BBi]) && (iN > RR2)) {
                              A2=A2 + A2-1;
                              RR2++;
                 }           
                 if (RR2 < iN) {
                    A=A2 + NNN[BBi];
                    RR = RR + RR2;
//                    for (int k=0; k < A; k++) if (Used[k]=='a') Used[k]=='x';
                 } else {
                    iN--;
//                    for (int k=0; k < A; k++) if (Used[k]=='a') Used[k]=='o';
                    RR++;
                 }
            }            
        }
        
        
        cout << "Case #" << (i+1) << ": "<< RR << endl;
    }
    
    return EXIT_SUCCESS;
}
