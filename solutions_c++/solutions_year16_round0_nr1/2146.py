#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>

using namespace std;

long long solve(long long n){
	set<int> s;
	long long i;
	for(i=1;s.size()<10;i++){
		long long x=n*i;
		while(x){
			s.insert(x%10);
			x/=10;
		}
	}
	
	i--;
	return n*i;
	
}

int main()
{
		
    int T;
    cin>>T;
	
    for(int t=1;t<=T;t++){
		long long n;
		cin>>n;
		
		if(n==0) printf("Case #%d: INSOMNIA\n",t);
        else printf("Case #%d: %lld\n",t,solve(n));
    }
    
    return 0;
}