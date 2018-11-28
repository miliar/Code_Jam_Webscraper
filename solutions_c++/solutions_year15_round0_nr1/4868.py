#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <fstream>
using namespace std;

const int N = 1005;
char shy[N];
int smax;
int res[N];

int main()
{

    fstream fin("A-small-attempt2.in", ios::in);
    int tcase, cas = 1;
    fin >> tcase;
    while(tcase --)
    {
        fin >> smax >> shy;

        int cnt = shy[0] - '0';
        int tRes = 0;
        for(int i = 1; i <= smax; i ++)
        {
            int tmp = shy[i] - '0';
            if(i > cnt) {
                tRes += (i - cnt);
                cnt += (i - cnt);
            }
            cnt += shy[i]-'0';
        }
        res[cas ++] = tRes;
    }
    fin.close();
    fin.open("result.txt", ios::out);
    for(int i = 1; i < cas; i ++)
        fin << "Case #" << i << ": " << res[i] << endl;
    return 0;

}
