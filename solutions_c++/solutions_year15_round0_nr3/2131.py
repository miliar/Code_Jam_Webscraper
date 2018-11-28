#include <iostream>
#include <fstream>
#include <string>

using namespace std;

inline char prod(char a, char b) {
    int sign_a = a > 0 ? 1 : -1;
    int sign_b = b > 0 ? 1 : -1;
    char res = ' ';
    a = a * sign_a;
    b = b * sign_b;
    if(a == '1') res = b;
    else if(b == '1') res = a;
    else if(a == b) res = -'1';
    else if(a == 'i' and b == 'j') res = 'k';
    else if(a == 'j' and b == 'i') res = -'k';
    else if(a == 'i' and b == 'k') res = -'j';
    else if(a == 'k' and b == 'i') res = 'j';
    else if(a == 'j' and b == 'k') res = 'i';
    else if(a == 'k' and b == 'j') res = -'i';
    else throw "undefined quaternion product.";
    return sign_a * sign_b * res; 
}

inline void print(char x) {
    if(x < 0) cout << "-" << char(-x) << endl;
    else cout << x << endl;
}

inline char prod_all(string str) {
    char a = '1';
    for(char ch : str) {
        a = prod(a, ch);
    }
    return a;
}

char cache_c[20000];

bool verify_c(const string& line, int j, int X, char whole) {
    char c = cache_c[j];
    if(X >= 1) {
        for(int x = 0; x < (X-1) % 4; x++) {
            c = prod(c, whole);
        }
    }
    return c == 'k';
}

int main() {
    ifstream file_in("C-small-attempt7.in");
    ofstream file_out("C-small-attempt7.out");
    int T;
    int C, X;
    string line;
    file_in >> T;
    for(int ti = 0; ti < T; ti++) {
        file_out << "Case #" << ti+1 << ": ";
        file_in >> C >> X;
        file_in.ignore();
        getline(file_in, line);
        cout << "line " << line << endl;
        char c = '1';
        cache_c[line.size()] = c;
        for(int k = line.size()-1; k >= 0; k--) {
            c = prod(line[k], c);
            cache_c[k] = c;
        }
        try {
            char whole = prod_all(line);
            char a = '1';
            for(int ri = 0; ri < min(4, X); ri++) {
                char a2 = '1';
                for(int i = 0; i <= line.size(); i++) {
                    if(prod(a, a2) == 'i') {
                        char b = '1';
                        for(int j = i; j < line.size(); j++) {
                            b = prod(b, line[j]);
                            if(b == 'j' and verify_c(line, j+1, X-ri, whole)) {
                                cout << "exit 1" << "ri: " << ri << endl;
                                throw "YES";
                            }
                        }
                        if(X-ri >= 2) {
                            int X2 = X-ri-1;
                            for(int rj = 0; rj < min(4, X2); rj++) {
                                char b2 = '1';
                                for(int j = 0; j <= line.size(); j++) {
                                    if(prod(b, b2) == 'j' and verify_c(line, j, X2-rj, whole)) {
                                        cout << "exit 2" << "ri: " << ri << ", rj: " << rj << endl;
                                        throw "YES";
                                    }
                                    if(j != line.size()) {
                                        b2 = prod(b2, line[j]);
                                    }
                                }
                                b = prod(b, whole);
                            }
                        }
                    }
                    if(i != line.size()) {
                        a2 = prod(a2, line[i]);
                    }   
                }
                a = prod(whole, a);
            }
        }catch(char const* msg) {
            file_out << "YES" << endl;
            continue;
        }
        file_out << "NO" << endl;
    }
    file_out.close();
    file_in.close();
}