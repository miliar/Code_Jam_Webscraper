#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;


void solve(int por) {
    printf("Case #%d: ",por);
    char C[147];
    scanf(" %s",C);
    string s=C;
    int n=1;
    for(int i=1; i<s.length(); i++) if(s[i]!=s[i-1]) n++;
    if(s[s.length()-1]=='+') n--;
    printf("%d\n",n);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
