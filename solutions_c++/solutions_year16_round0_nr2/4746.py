#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int n, ns, grupos;
string str;

int main(int argc, const char * argv[]) {

    ifstream in("in.txt");
    ofstream out("out.txt");
    
    in >> ns;
    getline(in, str);
    
    for (n = 0; n < ns; n++) {
        
        grupos = 1;
        getline(in, str);
        
        for (int c = 1; c < str.length(); c++) {
            
            if (str.at(c) != str.at(c - 1)) grupos++;
        }
        if (str.at(str.length() - 1) == '+') grupos--;
        
        out << "Case #" << n + 1 <<": " << grupos << "\n";
    }
    
    return 0;
}
