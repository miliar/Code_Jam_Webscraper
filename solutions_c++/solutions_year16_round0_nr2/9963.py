#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#include <iostream>
#include <fstream>
#define cin fin

#define pb push_back
#define puts(x) cout << #x << " : " << x << endl;
#pragma GCC diagnostic ignored "-Wconversion"

#define REP(i,n) for (int i=0;i<(n);i++)
#define REPE(i,n) for (int i=0;i<=(n);i++)

#define init(a,b) memset((a), (b), (sizeof(a)));

#define PI 3.14159265
#define EPS (1e-10)
#define EQ(a,b) (abs((a)-(b)) < EPS)

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int main() {
    ifstream fin("/tmp/in.txt");
    freopen("/tmp/out.txt", "w", stdout);
    int n;cin>>n;
    for(int cs=0;cs<n;cs++){
        int res=0;
        string s;cin>>s;
        for(int i = 0;i<s.size()-1;i++){
            if(s[i]==s[i+1])continue;
            if(s[i]=='-'){
                // - -> +
                res++;
            } else {
                //+ -> -
                res++;
            }
        }
        if(s[s.size()-1]=='-')res++;
//        bool allm=true;
//        for(int i = 0;i<s.size();i++)
//            if(s[i]=='+')allm=false;
//        if(allm)res=1;
        printf("Case #%d: %d\n", cs+1, res);
    }
    return 0;
}
