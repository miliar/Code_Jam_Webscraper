//#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream cin("A-large.in");
ofstream cout("A-large.out");

int gi(char z) {
return (int)(z-'A');
}

int main() {
    int T;
    cin >> T;
    for (int t=0; t<T; t++) {
       int A[26];
       int B[10];
       for (int i=0; i<26; i++) A[i] = 0;
       for (int i=0; i<10; i++) B[i] = 0;
       cout << "Case #" << t+1 << ": ";
       string s;
       cin >> s;
       for (int i=0; i<s.size(); i++) {
        A[(int)s[i]-'A']++;
       }
       string ret = "";
       B[0]+= A[gi('Z')]; A[gi('E')]-=B[0]; A[gi('R')]-=B[0]; A[gi('O')]-=B[0]; A[gi('Z')]-=B[0];
       B[6]+=A[gi('X')]; A[gi('S')]-=B[6]; A[gi('I')]-=B[6]; A[gi('X')]-=B[6];
       B[2]+=A[gi('W')]; A[gi('T')]-=B[2]; A[gi('W')]-=B[2]; A[gi('O')]-=B[2];
       B[4]+=A[gi('U')]; A[gi('F')]-=B[4]; A[gi('O')]-=B[4]; A[gi('U')]-=B[4]; A[gi('R')]-=B[4];
       B[7]+=A[gi('S')]; A[gi('S')]-=B[7]; A[gi('E')]-=B[7]; A[gi('V')]-=B[7]; A[gi('E')]-=B[7]; A[gi('N')]-=B[7];
       B[5]+=A[gi('V')]; A[gi('F')]-=B[5]; A[gi('I')]-=B[5]; A[gi('V')]-=B[5]; A[gi('E')]-=B[5];
       B[8]+=A[gi('G')]; A[gi('E')]-=B[8]; A[gi('I')]-=B[8]; A[gi('G')]-=B[8]; A[gi('H')]-=B[8]; A[gi('T')]-=B[8];
       B[3]+=A[gi('H')]; A[gi('T')]-=B[3]; A[gi('H')]-=B[3]; A[gi('R')]-=B[3]; A[gi('E')]-=B[3]; A[gi('E')]-=B[3];
       B[9]+=A[gi('I')]; A[gi('N')]-=B[9]; A[gi('I')]-=B[9]; A[gi('N')]-=B[9]; A[gi('E')]-=B[9]; 
       B[1] += A[gi('O')];
       for (int i=0; i<10; i++) {
        for (int j=0; j<B[i]; j++) {
          ret += (char)('0'+i);
        }
       }
       cout << ret << endl;
    }
return 0;
}
