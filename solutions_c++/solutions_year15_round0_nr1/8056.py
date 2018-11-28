#include <fstream>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <map>
#include<stack>
#include<map>
#include<queue>
#include <math.h>
#include<set>
#include<stdint.h>
#include <utility>
#include <cmath>
#include <iostream>
#include <iomanip>
#define MAXN 100005
#define MaxVal 86410
#define MAXLG 17
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

using namespace std;
typedef long long int ll;
typedef pair<int, int> mp;
template<class T> void chmin(T &t, const T &f) { if (t > f) t = f; }
template<class T> void chmax(T &t, const T &f) { if (t < f) t = f; }

int main()
{
    ifstream inFile("/Users/neel/Desktop/Practice/Practice/a.txt");
    ofstream output;
    output.open("/Users/neel/Desktop/Practice/Practice/output.txt");
    
    int t;
    inFile >> t;
    for(int caseNo=0; caseNo<t; ++caseNo)
    {
        output << "Case #" << caseNo + 1 << ": ";
        
        char a[1005];
        int n, i;
        inFile >> n;
        inFile >> a;
        
        int tot = a[0] - '0', ans=0;
        for(i=1; i<=n; ++i)
        {
            if(tot >= i)
                tot += (a[i] - '0');
            else
            {
                ans += i - tot;
                tot += i - tot + (a[i] - '0');
            }
        }
        
        output << ans << endl;
    }
    output.close();
    return 0;
}