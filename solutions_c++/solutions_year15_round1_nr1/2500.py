#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <climits>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <utility>
using namespace std;
vector<int> mushperTenSec;
typedef long long int ll;
int maxDiff;
ll method1()
{
	ll sum=0;
	for(int i=1;i<mushperTenSec.size();i++){
		if(mushperTenSec[i] < mushperTenSec[i-1]){
			sum += mushperTenSec[i-1] - mushperTenSec[i];
			maxDiff = max(maxDiff,mushperTenSec[i-1] - mushperTenSec[i]);
		}
	}
	return sum;
}

ll method2()
{
	ll sum = 0;
	for(int i=0;i<mushperTenSec.size()-1;i++){
		if(mushperTenSec[i]<maxDiff){
			sum += mushperTenSec[i];
		}
		else
			sum += maxDiff;
	}
	return sum;
}

int main()
{
    // freopen("in","r",stdin);
    // freopen("output","w",stdout);
    int cnt=1;
    int T;
    scanf("%d",&T);
    while(T--){
    	mushperTenSec.clear();
    	int N,tmp;
    	scanf("%d",&N);
    	for(int i=0;i<N;i++){
    		scanf("%d",&tmp);
    		mushperTenSec.push_back(tmp);
    	}
    	maxDiff = 0;
    	printf("Case #%d: %lld %lld\n",cnt++,method1(),method2());
    }
	return 0;
}