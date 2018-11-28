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
#include <istream>

using namespace std;

const int MAX = 7654321;

//      panc  day in
int pre[1001][1001];

int ar[6][10] = { 0, };
int start[6] = { MAX, };

void main() {
    for (int i = 1; i < 1001; i++) {    // pan
        for (int j = 1; j < 1001; j++) {    // day
            int res = 0;
            if (i % j == 0) {
                res = i / j - 1;
            }
            else {
                res = i / j;
            }
            pre[i][j] = res;
        }
    }
    
    int T;
    cin >> T;
    ofstream out;
    out.open("output.txt");

    for (int testc = 1; testc <= T; testc++) {
        int num;
        cin >> num;
        
        for (int i = 0; i < num; i++) {
            cin >> start[i];
        }

        int minhour = MAX;
       
        for (int restDay = 1; restDay < 1001; restDay++) {
            int hour = 0;
            for (int i = 0; i < num; i++) {
                hour += pre[start[i]][restDay];
            }
            minhour = min(minhour, hour + restDay);
        }
        out << "Case #" << testc << ": " << minhour << endl;
    }
}