#include <iostream>

int main(){
    using namespace std;
    std::ios_base::sync_with_stdio(false);
    int z,k,n,sMax,add,sum;
    char *tab;
    cin >> z;
    for(k=1;k<=z;k++){
        cin >> sMax;
        tab = new char[sMax+2];
        cin >> tab;
        sum=0;
        add=0;
        for(int i=0; i<=sMax; i++){
            if(sum<i){
                add+=(i-sum);
                sum=i;
            }
            sum+= tab[i] - '0';
        }
        delete[] tab;
        cout << "Case #" << k << ": " << add << endl;
    }
    return 0;
}
