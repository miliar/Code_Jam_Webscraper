// Coded by HACKER_J

#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <fstream>

using namespace std;

unsigned long long int convert_base(string vstr, int L, int b){
    int i;
    unsigned long long int inc = 1;
    unsigned long long int num = 0;
    
    for (i = L - 1; i >= 0; i--) {
        if (vstr[i] == '1') {
            num += inc;
        }
        inc *= b;
    }
    
    return num;
}

string convert_bit(int N, int L) {
    string midstr (L-2, '0');
    string jamstr = "1";
    int i = 0;
    
    while (N >= 2) {
        (N % 2 == 0) ? midstr[i] = '0' : midstr[i] = '1';
        N = N / 2;
        i++;
    }
    
    (N % 2 == 0) ? midstr[i] = '0' : midstr[i] = '1';
    midstr = string(midstr.rbegin(), midstr.rend());
    
    jamstr.append(midstr);
    jamstr.append("1");
    
    return jamstr.c_str();
}

unsigned long long int findDiv(unsigned long long int num)
{
    unsigned long long int N = num;
    
    if (N < 2) {
        return 1;
    }
    int minloop;
    if (N > 1000) {
        minloop = 1000;
    } else {
        minloop = (int)N;
    }
    
    unsigned long long int i;
    
    for (i = 2; i < minloop; i++) {
        if (N % i == 0) {
            return i;
        }
    }
    
    return 1;
}

int main() {
    ifstream fin;
    ofstream fout;
    
    int T, N, J, plen, i, j, k, j_count = 0;
    
    string ntemp;
    string divstr;
    
    fin.open("C-small-attempt0.in");
    if(fin.fail()) {
        cout << "File failed to open." << endl;
    }
    
    fout.open("C-small.out");
    
    cout << "Running.." << endl;
    T = 1;
    N = 16;
    J = 50;
    
    //fin >> T;
    //fin >> N >> J;
    //scanf("%d", &T);
    //scanf("%d%d", &N, &J);
    
    //printf("Case #%d:\n", 1);
    fout << "Case #1:" << endl;
    plen = pow(2, N-2);
    
    unsigned long long int narr[N-1];
    // unsigned long long int nbasearr[N-1];
    
    for (i = 0; i < plen; i++) {
        cout << "next loop.." << to_string(i) << endl;
        
        ntemp = convert_bit(i, N);
        
        for (j = 2; j <= 10; j++) {
            cout << "base.." << to_string(j) << endl;
            //nbasearr[j-2] = convert_base(ntemp, N, j);
            narr[j-2] = findDiv(convert_base(ntemp, N, j));
            
            if (narr[j-2] == 1) {
                break;
            }
            
            if (j == 10) {
                fout << ntemp << " ";
                for (k = 0; k < 8; k++) {
                    fout << narr[k] << " ";
                    //fout << nbasearr[k] << " ";
                }
                fout << narr[k] << endl;
                //fout << nbasearr[k] << endl;
                j_count++;
            }
        }
        
        if (j_count >= J) {
            fout.close();
            cout << "ok, done" << endl;
            return 0;
        }
    }
    fout.close();
    cout << "ok, done" << endl;
    return 0;
}