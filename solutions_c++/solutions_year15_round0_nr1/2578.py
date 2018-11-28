#include <stdio.h>
#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cassert>
#include <sstream>
#include <iterator>

using namespace std;

#define file "file"
#define mp make_pair
#define pb push_back
#define xx real()
#define yy imag()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef complex<double> point;

const int MAXN = 1e4 + 5;

char s[MAXN];

void solve(){
    int n;
    scanf("%d",&n);
    scanf("%s",s);
    n++;
    int ans = 0;
    int sum = 0;
    for(int i = 0;i < n;i++){
        int cur = s[i] - '0';
        if(sum < i){
            ans += i - sum;
            sum = i;
        }
        sum += cur;
    }
    printf("%d\n",ans);
}

int main()
{
//	#ifndef ONLINE_JUDGE
//    assert(freopen("input.txt","r",stdin));
//    assert(freopen("output.txt","w",stdout));
//    #else
//    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
//    #endif
	int t = 1;
	scanf("%d",&t);
	int cs = 1;
	while(t--){
        printf("Case #%d: ",cs++);
		solve();
	}
	return 0;
}
