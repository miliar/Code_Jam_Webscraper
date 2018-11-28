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

int solve(){

}
int main()
{
	int testCases;
	int n,numbers[1009];
	freopen("As.in","r",stdin);
	freopen("As.out","w",stdout);
	cin>>testCases;
	for(int k=1 ; k<=testCases ; k++){
        cin>>n;
        int ans1=0,ans2=0;
        int add=0;
        for(int i=1 ; i<=n;  i++){
            cin>>numbers[i];
            if(i==1){
                continue;
            }
            if(numbers[i]<numbers[i-1])
                ans1+=(numbers[i-1]-numbers[i]);
            add=max(add,numbers[i-1]-numbers[i]);
        }
        for(int i=2 ; i<=n ; i++){
            ans2+=min(add,numbers[i-1]);
        }
	    cout<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
