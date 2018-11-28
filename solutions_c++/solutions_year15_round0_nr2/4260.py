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
int p[N], n, ans[N];

int main() {
    int tcase , step = 0 ;
    int max1, res , sum ;
    fstream fin("B-large.in", ios::in) ;

    fin >> tcase;
    for (int t = 1; t <= tcase; t ++){
        fin >> n ;
        for(int i = 0 ; i < n ; i++) {
            fin >> p[i];
            max1 = max(max1, p[i]) ;
        }
        res = max1 ;
        for (int i = 1 ; i <= max1 ; i++)
        {
            sum = i ;
            for(int j = 0 ; j < n ; j++)
            {
                if (p[j] > i)
                {
                    if (p[j] % i == 0)
                        sum += (p[j] / i - 1) ;
                    else
                        sum += (p[j]/i) ;
                }
            }
            res = min(res, sum) ;
        }
        ans[t] = res;
    }

    fin.close();
    fstream fout("result.txt", ios::out);
    for(int i = 1; i <= tcase; i ++)
        fout << "Case #" << i << ": " << ans[i] << endl;
    fout.close();

    return 0 ;
}
