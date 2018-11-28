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
#include <vector>
#include <fstream>

#define pb push_back
#define mp make_pair

using namespace std;

int main(){
    //ofstream out;
    //out.open("A.out");
    int T, n, s, k;
    char c;
    cin>>T;
    for(int t=0; t<T; t++) {
        cin>>n;
        s = k = 0;
        for(int i=0; i<=n; i++) {
            if(i>s) {
                k += (i-s);
                s = i;
            }
            cin>>c;
            s += (c-'0');
        }
        cout<<"Case #"<<t+1<<": "<<k<<endl;
    }
    //out.close();
    return 0;
}
