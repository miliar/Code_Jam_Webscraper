#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define PB(X) push_back(X)
#define fill(x,v) memset(x,v,sizeof(x))
int a,b,K;
int solve(){
    int count=0;
    for(int i=0 ; i<a ; i++){
        for(int j=0 ; j<b ; j++){
            if((i&j)<K)
                count++;
        }
    }
    return count;
}
int main()
{
	int testCases;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>testCases;
	for(int k=1 ; k<=testCases ; k++){
        cin>>a>>b>>K;
	    cout<<"Case #"<<k<<": "<<solve()<<endl;
	}
	return 0;
}
