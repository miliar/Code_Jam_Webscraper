#include <iostream>
#include <set>
using namespace std;
int fin[1000001];
int main()
{

    for (int unsigned k=1; k < 1000001  ;k++){
    int i=1;
    set<int> myset;
    int aux;
    int result;
    while (myset.size() <10){
        aux=k*i ;
        result = aux;
        while (aux){
            myset.insert(aux%10);
            aux/=10;
        }
        i++;
    }
    fin[k] =result;
    }
    int m,z;
    cin >> m;
    for (int q=1 ; q<=m ; q++){
        cin >> z;
        if (z){
            cout << "Case #" << q <<": "<<fin[z]<<endl;
        } else {
              cout << "Case #" << q <<": INSOMNIA"<<endl;
        }

    }
    return 0;
}
