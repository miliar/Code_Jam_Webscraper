#include <iostream>
#include <cmath>

int main(){
    using namespace std;
    std::ios_base::sync_with_stdio(false);
    int z,k,n,caseSize,left,right,center,time,timevip;
    int *tab;
    cin >> z;
    for(k=1;k<=z;k++){
        cin >> caseSize;
        tab = new int[caseSize];
        left=1;
        right=tab[0];
        for(int i=0; i<caseSize; i++){
            cin >> tab[i];
            if(right<tab[i]){
                right = tab[i];
            }
            if(left>tab[i]){
                left = tab[i];
            }
        }
        time=right;
        center=right;
        while(center>=left){
            timevip=center;
            for(int i = 0; i<caseSize; i++){
                if(tab[i]>center){
                    timevip+=(int) ceil( (double) tab[i] / (double) center) - 1;
                }
                if(timevip>time){
                    break;
                }
            }
            if(timevip<time){
                time=timevip;
            }
            center--;
        }
        delete[] tab;
        cout << "Case #" << k << ": " << time << endl;
    }
    return 0;
}
