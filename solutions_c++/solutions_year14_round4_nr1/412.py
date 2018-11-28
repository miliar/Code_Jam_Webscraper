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
int x, n;

int main() {
    int i,j,k,t,Case = 1;
    cin>>t;
    while(t--)
    {
        cin>>n>>x;
        
        for(int i = 0; i< n; i++)
            cin>>p[i];
        
        sort(p, p + n);
        
        int result = 0, l = 0, r = n - 1;
        while(l < r) {
            if (p[l] + p[r] <= x) ++result, ++l, --r;
            else ++result, --r;
        }
        if(l ==r) result++;
        //result += (l == r);
        cout<<"Case #"<<Case++<<": "<<result<<endl;
        
    }
    return 0;
}
