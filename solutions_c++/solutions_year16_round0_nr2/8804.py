#include <iostream>
#include <fstream>
using namespace std;
#define b(x) bool((int(str[x])+1)%11==0)
int main(){
    freopen("B-large.in","r",stdin);
    freopen("pan.out","w",stdout);
    int caseof;
    cin>> caseof;
    for (int cas = 1 ; cas <= caseof ; cas++){
        string str;
        cin>> str;
        bool signe =b(0);
        int nb=!b(str.length()-1);
        for (int i = 1 ; i < str.length() ; i ++){
            nb+= b(i)!=signe;
            signe=b(i);
        }
        cout<<"Case #" <<cas<<": "<<nb<<endl;
    }

}
