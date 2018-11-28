#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

string a, prev;
bool k = false;

int f(int res){
    if(prev == "="){
        prev = a;
        return res;
    }
    if(prev != a){
        if(prev == "-"){
            if(k) res += 2;
            else res += 1;
        }
        prev = a;
        k = true;
    }
    return res;
}

int main(){
    ifstream in("input.in");
    ofstream out("output.out");
    int n;
    string c;
    in >> n;
    for(int i = 0; i < n; i++){
        prev = "=";
        int res = 0;
        a = "a";
        in >> c;
        c += "+";
        k = false;
        for(int j = 0; j < c.size(); j++){
            a = c.substr(j, 1);
            res = f(res);
        }
        out << "Case #" << i + 1 <<": " << res << endl;
    }
    return 0;
}
