#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ifstream f("p2.in");
ofstream g("p2.out");

string s;
int t, i, j, counter;
char currentSign;

int main(){
    f>>t;

    for(i=0; i<t;i++){
        f>>s;

        counter = 0;
        for(j=0; j < s.length()-1; j++){
            if(s[j] != s[j+1]){
                counter++;
            }
        }

        if(s[s.length()-1] == '-'){
            counter++;
        }

        g<<"Case #"<<i+1<<": "<<counter<<"\n";
    }
}

