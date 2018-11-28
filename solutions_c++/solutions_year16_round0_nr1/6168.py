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
    int a,d;
    cin>>t;
    while(t--)
    {
        vector<bool> b(10, false);
        cin>>d;
        a = d;
        if (d != 0) {
            while(1) {
                int e = a;
                while(a>0) {
                    int c = a%10;
                    b[c] = true;
                    a = a/10;
                }
                int i = 0;
                while(i < 10 && b[i]) i++;
                if (i == 10) {
                    a = e;
                    break;
                }
                a = e + d;
            }
            cout<<"Case #"<<Case++<<": "<<a<<endl;
            
        } else {
            cout<<"Case #"<<Case++<<": "<<"INSOMNIA"<<endl;
            
        }
        
    }
    return 0;
}
