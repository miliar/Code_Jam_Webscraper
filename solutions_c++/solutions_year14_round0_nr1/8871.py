#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#define INT_MAX 2147483647
#define INT_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL unsigned long long
using namespace std;

vector <int> igualdad(vector<int> a,vector<int>b){
 vector<int> igual;
 for (int i=0;i<a.size();i++){
    for (int j=0;j<b.size();j++){
        if (a.at(i)==b.at(j)) igual.push_back(a.at(i));
    }
 }
return igual;
}
int main ()
{
    int t;
    cin >> t;
    for (int i=1;i<=t;i++){
    vector < vector <int> > matriz,matriz2;

        int rpt1,rpt2;
        cin >> rpt1;
        for (int a=0;a<4;a++){
            vector <int> arreglo;
            for (int b=0;b<4;b++){
                int valor;
                cin >> valor;
                arreglo.push_back(valor);
            }
            matriz.push_back(arreglo);
        }
        vector <int> rpt1a,rpt2a;
        rpt1a=matriz.at(rpt1-1);

        cin >> rpt2;
        for (int a=0;a<4;a++){
            vector <int> arreglo;
            for (int b=0;b<4;b++){
                int valor;
                cin >> valor;
                arreglo.push_back(valor);
            }
            matriz2.push_back(arreglo);
        }
        rpt2a=matriz2.at(rpt2-1);

        vector <int> rpt = igualdad(rpt1a,rpt2a);

        if ((int)rpt.size()==1) cout << "Case #" <<i<<": "<<rpt.at(0)<<endl;
        else {
            if (rpt.size()>1) cout << "Case #" <<i<<": Bad magician!"<<endl;
            else cout << "Case #" <<i<<": Volunteer cheated!"<<endl;
        }
    }


    return 0;
}









