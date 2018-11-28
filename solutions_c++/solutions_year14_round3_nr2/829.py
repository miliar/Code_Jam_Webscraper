#include <algorithm>
#include <iostream>
#include <fstream>
#include <cctype>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstring>

#define MIN(a,b) (a < b ? (a) : (b))
#define MAX(a,b) (a > b ? (a) : (b))

using namespace std;

int main()
{
    ifstream fin("in.in");
    ofstream fout("out.out");

    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        fout << "Case #" << t << ": ";
        string cars[10];
        int N;
        fin >> N;
        for (int i = 0; i < N; i++) fin >> cars[i];
        int perm[] = {0,1,2,3,4,5,6,7,8,9};
        int count = 0;
        int sum = 0;
        do {
            bool seen[26] = {0};
            stringstream ss;
            for (int i = 0; i < N; i++) ss << cars[perm[i]];
            string s = ss.str();
            char prev = s[0];
            seen[prev-'a'] = 1;
            bool flag = true;
            for (int i = 1; i < s.size() && flag; i++) {
                if (seen[s[i]-'a'])
                    flag = prev == s[i];
                else {
                    seen[s[i]-'a'] = 1;
                    prev = s[i];
                }
            }
            count += flag;
        } while(next_permutation(perm, perm+N));
        fout << count << endl;
    }
}