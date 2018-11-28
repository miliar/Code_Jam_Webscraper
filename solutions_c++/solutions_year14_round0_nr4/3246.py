#include <iostream>
#include <vector>
#include <fstream>
#include <limits>
#include <algorithm>

using namespace std;
const int MAXN = 1005;
const double oo = numeric_limits<double>::max();
int T, dydis;
int suma = 0,save1=0;
double skaicius;
double masL[MAXN],masL1[MAXN], masP[MAXN], masP1[MAXN];

int main()
{
    ifstream input("inP.txt");
    ofstream out ("outK.txt");
    input >> T;
    for(int t = 1; t<=T; t++){
        input >> dydis;
        for(int i = 0; i < dydis; i++){
                input >> skaicius;
                masL[i]=skaicius;
                masL1[i]=skaicius;
        }
        for(int i = 0; i < dydis; i++){
                input >> skaicius;
                masP[i]=skaicius;
                masP1[i]=skaicius;
        }
        sort(masP, masP+dydis);
        sort(masL, masL+dydis);
        for(int i =0; i < dydis; i++){
            for(int y = 0; y < dydis; y++){
                if(masL[i]<masP[y]){
                    suma+=1;
                    masP[y]=-oo;
                    break;
                }
            }
        }

        sort(masP1, masP1+dydis);
        sort(masL1, masL1+dydis);
        int st=0, fn=dydis-1;
        int stL=0, stP=0, fnP=dydis-1;
        while(stL<dydis){
                if(masL1[stL]>masP1[stP]){
                    stL+=1;
                    stP+=1;
                    save1+=1;
                }else{
                    stL+=1;
                    fnP-=1;
                }
        }
        out << "Case #" << t << ": " << save1 <<  " " << dydis - suma << endl;
    suma = save1 = 0;
    }
    return 0;
}
