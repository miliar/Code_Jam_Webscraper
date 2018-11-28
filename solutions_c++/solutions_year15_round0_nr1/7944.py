#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>    //also contains priority_queue
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
#include <ctime>
using namespace std;
#define LL long long int
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define FOR(i,st,end) for(int (i)=(st);i<(end);i++)
#define FORD(i,st,end) for(int (i)=(st);i>=(end);i--)
#define TOINT(c) ((int)(c)-'0')
int main(void)
{
    int t,m,sum,req;
    string s;
    cin >> t;
    FOR(i,0,t){
        sum = 0;
        req = 0;
        cin >> m;
        cin >> s;
        //vector<int> v(m+1,0);
        sum = TOINT(s[0]);  //those who'll always stand.
        FOR(j,1,m+1){
            if(sum<j){
                req += (j-sum);
                sum += (j-sum); //fulfill the deficiency so these people can fucking stand up.
            }
            sum += TOINT(s[j]); //these ppl have stood up.
        }
        cout<<"Case #"<<(i+1)<<": "<<req<<"\n";
    }
}
