#include <iostream>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    int t , smax;
    cin >> t;
    string s;
    for(int q=0 ; q<t ; q++){
        cin >> smax;
        cin >> s;
        int suma=0;
        int add=0;
        for(int i=0;i<=smax;i++){
            if(suma<i){
                add += i-suma;
                suma=i;
            }
            suma+=s[i]-48;
        }
        cout << "Case #" << q+1 << ": " << add << "\n";
    }

}
