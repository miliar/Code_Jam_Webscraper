#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <ctime>
#define INF 100000000
using namespace std;

long remlog[1002];

int main() {
//    for(long i=1; i<1002; i++){
//        long x = i;
//        remlog[i] =1;
//        while(x>1){
//            remlog[i]++;
//            x = (x+1)/2;
//        }
//    }
    //cout << remlog[13] << " " << remlog[4] << endl;
	int T; cin >> T;
	for(int _case = 1; _case <= T; _case++) {
        vector <int> p;
        long d, x;
        long ans = 0, t1, t2;
        long maxT = -1;
        cin >> d;
//        cout << "--------\n";
//        cout << d << endl;
        for(int i=0; i<d; i++){
            cin >> x;
            p.push_back(x);
            maxT = max(maxT, x);
//            cout << x << " ";
        }
//        cout << endl;
        for(long t=1; t<=maxT; t++){
            ans = t;
            for (long i=0; i<d; i++) {
                if(t>=p[i]) continue;
                ans += p[i]/t -1 ;
                if(p[i]%t) ans++;
            }
            maxT = min(maxT, ans);
        }
        /*
        while ((p.top()+1)/2 +1  < p.top() ) {
            maxT = min(maxT, p.top() + ans);
            if(p.top()%2){
                
            }
            ans++;
            t1 =(p.top()+1)/2;
            t2 = p.top() - t1;
            p.pop();
            p.push(t1);
            p.push(t2);
            if(ans>=maxT) break;
        }
         */
        cout << "Case #" << _case << ": " << maxT << endl;
	}
	return 0;
}
