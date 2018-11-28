#include<iostream>
#include<cstdio>
#include<cmath>
#include<cctype>
#include<sstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<functional>
#include<numeric>
#include<utility>
#include<cstdlib>
#include<cstring>
#include<ctime>
using namespace std;

const int MAXN = 10005;
int p[MAXN];
int q[MAXN];

int main() {
    int i,j,k,t,Case = 1;
    string a;
    cin>>t;
    while(t--)
    {
        cin>>a;
        if (a[0] == '+') {
            p[1] = 0;
            q[1] = 1;
        } else {
            p[1] = 1;
            q[1] = 0;
        }
        for (int i = 2; i <= a.length(); i++) {
            if (a[i-1] == '+' )
            {
                p[i] = p[i-1];
                q[i] = p[i-1] + 1;
            } else {
                p[i] = q[i-1] + 1;
                q[i] = q[i-1];
            }
        }
        
        cout<<"Case #"<<Case++<<": "<<p[a.length()]<<endl;
        
    }
    return 0;
}
