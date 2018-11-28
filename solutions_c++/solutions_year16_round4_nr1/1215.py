using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
typedef long long LL;
string getstring(int n,string cur){
    if (n==0) {
            return cur;
    }
    string a,b;
    if (cur=="R") {a=getstring(n-1,"R");b=getstring(n-1,"S");}else
        if (cur=="S") {a=getstring(n-1,"S");b=getstring(n-1,"P");}else
        if (cur=="P") {a=getstring(n-1,"P");b=getstring(n-1,"R");};
    if (a+b<b+a) return a+b;
    return b+a;
}
int ok(string st,int r,int p,int s)
{
    int sum=0;
    for (char ch: st) if (ch=='R') sum++;
    if (sum!=r) return 0;

    sum=0;
    for (char ch: st) if (ch=='S') sum++;
    if (sum!=s) return 0;

    sum=0;
    for (char ch: st) if (ch=='P') sum++;
    if (sum!=p) return 0;
    return 1;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    cin>>t;
    for (int time=1;time<=t;time++)
    {
        int n,r,p,s;
        cin>>n>>r>>p>>s;
        string tmp1,tmp2,tmp3;
        cout<<"Case #"<<time<<": ";
        tmp1=getstring(n,"R");
        tmp2=getstring(n,"S");
        tmp3=getstring(n,"P");
        if (ok(tmp1,r,p,s)) cout<<tmp1;
        else if (ok(tmp2,r,p,s)) cout<<tmp2;
        else if (ok(tmp3,r,p,s)) cout<<tmp3;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
}
