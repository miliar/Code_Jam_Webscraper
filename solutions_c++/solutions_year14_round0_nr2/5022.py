#include <iostream>
#include <cstdio>
#include<stack>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cctype>
#include <cmath>
#include <iomanip>
#include<cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

//initilaly cookies = 0
//2 cookies/s by clicking on a giant cookie
//atleast C cookies, buy a cookie farm
//cookie farm costs C cookies & gives extra F cookies/s
//once we have X cookies, we win

int main() {
    int t;
    freopen("/Users/shalini/Downloads/B1.txt","r",stdin);
    freopen("/Users/shalini/Downloads/B11.txt","w",stdout);

    cin>>t;
    for(int i = 1;i <= t;i++) {
        double c,f,x;
        cin>>c>>f>>x;
        double start = 2.0;
        double atmost = x/start;
        double till = 0;
        int cnt = 0;
        while(1) {
            ++cnt;
            double take = c/start + x/(start+f), direct = x/start;
            if(take > direct) {
                atmost = till + direct;
                break;
            }
            else {
                atmost = till + take;
                till += (c/start);
                start += f;
            }
        }
       // cout<<cnt<<"\n";
        printf("Case #%d: %0.7lf\n",i,atmost);
       // cout<<"Case #"<<i<<": "<<atmost<<"\n";
    }
    return 0;
}