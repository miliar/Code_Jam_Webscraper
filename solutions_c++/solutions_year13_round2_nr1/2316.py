#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

typedef int type;

pair <type,type> napierdalaj (type mam, type trzeba){
    type wyn = 0, plus = 0;
    while (mam <= trzeba){
        plus = mam-1;
        mam += plus;
        wyn ++;
    } 
    return make_pair(wyn,plus);
}

int main(){
    vector <type> iletrzeba (1000005, 0); //po
    vector <type> ilejest (1000005, 0); //przed
    pair <type,type> zdr;
    type t, man, ile,a,i,j, tmp, licznikusuniec;
    type wynik;
    scanf ("%d", &t);
    for (a = 0; a < t; ++a){
        licznikusuniec = 0;
        wynik = 0;
        scanf ("%d", &man);
        scanf ("%d", &ile);
        vector <type> wej (ile+1, 0);
        wej [0] = man;
        ilejest[0] = 0;
        iletrzeba[0] =0;
        for (i = 1; i < ile+1; ++i){
            scanf("%d", &tmp);
            wej[i] = tmp;
            ilejest[i] = 0;
            iletrzeba[i] =0;
        }
        sort (wej.begin()+1, wej.end());
        ilejest[1] = man;
        iletrzeba[0] = 0;
        if (man != 1){
            for (i = 1; i <= ile; i++){
               zdr = napierdalaj(ilejest[i], wej[i]);
                j = i +1;
                ilejest[j] = zdr.second + wej[i] + ilejest[i];
                j = i -1 ;
                iletrzeba[i] = iletrzeba[j] + zdr.first;
             //   cout << zdr.first << "vd" << zdr.second << "\n";
            }
            //cout << iletrzeba[ile];
            wynik = iletrzeba[ile];
            licznikusuniec = 0;
            for (i = ile; i > 0; i--){
                licznikusuniec ++;
                 j = i -1;
                wynik = min (wynik, licznikusuniec + iletrzeba[j]);
                
            }
        }
        else {
            wynik = ile;
            }   
        printf("Case #%d: %d\n", a+1, wynik);
    }
    return 0;
}
