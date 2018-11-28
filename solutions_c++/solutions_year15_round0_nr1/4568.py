#define _CRT_SECURE_NO_WARNINGS

#include<stack>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <fstream>

using namespace std;


void main() {
    int T;
    cin >> T;
    ofstream out;
    out.open("output.txt");
    
    for (int testc = 1; testc <= T; testc++) {
        int len;
        string in;
        cin >> len >> in;
        len = in.size();
        int people = 0, need = 0;
        for (int i = 0; i < len; i++) {
            people += in[i] - '0';
            if (people < 1) {
                need++;
            }
            else {
                people--;
            }
        }
        out << "Case #" << testc << ": " << need << endl;
    }
}