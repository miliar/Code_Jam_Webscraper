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
#include <ctime>

using namespace std;

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int i, n, t, s, c, num;
    int a[1001];
    cin>>t;
    for(int l=1; l<=t; l++) {
        s=0;
        c=0;
        cin>>n>>num;
        for(i=n;i>=0;i--) {
            int temp=num%10;
            a[i]=temp;
            num/=10;
        }
        for(i=0;i<=n;i++) {
            if(a[i]>0) {
                if(i<=s) {
                    s+=a[i];
                }
                else {
                    c+=(i-s);
                    s+=a[i]+c;
                }
            }
        }
        cout<<"Case #"<<l<<": "<<c<<"\n";
    }
    return 0;
}
