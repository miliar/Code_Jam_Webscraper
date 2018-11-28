#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<iomanip>
#include<stdlib.h>
#include<set>
#include<map>
#include<fstream>
using namespace std;
int main() {
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("salidaALarge.txt");
    
    int t,n, kase = 1;
    in >> t;
    while(t--) {
        bool mark[10];
        memset(mark, false, 10);
        int cont = 0, i=1;
        in >> n;
        if(n == 0)
            
            out << "Case #" << kase << ": INSOMNIA" << endl;
        else {
            while(cont < 10) {
                int aux = n*i;
                while(aux > 0) {
                    int d = aux%10;
                    aux/=10;
                    if(mark[d] == false) {
                        mark[d] = true;
                        cont++;
                    }
                }
                i++;
            }
            out << "Case #" << kase << ": " << n*(i-1) << endl;
        }
                    kase++;
    }
}