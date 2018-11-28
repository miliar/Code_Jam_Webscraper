#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <fstream>
#include <stack>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;

string n;
int a[35];
long long s[10];

int main(){
    int t,kase=0,c,s,k;
    cin>>t;
    while (t--) {
        kase++;
        cin>>k>>c>>s;
        cout<<"Case #"<<kase<<":";
        for (int i=1; i<=s; i++) {
            cout<<" "<<i;
        }
        cout<<endl;
    }
    return 0;
    
}
