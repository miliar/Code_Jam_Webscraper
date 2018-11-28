#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>
#include <limits.h>
#include <time.h>
#include <iterator>
 
#pragma comment(linker, "/STACK:167772160")
 
using namespace std;
 
int main(){
        ifstream cin("D-large.in");
        ofstream cout ("out.txt");
        double x[1111], y[1111];
        int T;
        cin >> T;
        for(int t=1; t<=T; t++) {
                int n;
                cin >> n;
                for(int i=0; i<n; i++) cin >> x[i];
                for(int i=0; i<n; i++) cin >> y[i];
                sort(x, x+n);
                sort(y, y+n);
                int ans1 = 0, ans2 = 0;
                int p = 0;
                for(int i=0; i<n; i++)
                        if(x[i] > y[p]) ans1++, p++;
 
                for(int i=0; i<n; i++) {
                        bool was = 0;
                        for(int j=0; j<n; j++)
                                if(y[j] > x[i]) {
                                        was = 1;
                                        y[j] = -1;
                                        break;
                                }
                        ans2 += !was;
                }
                cout << "Case #" << t << ": ";
                cout << ans1 << " " << ans2 << endl;
        }
    return 0;
}