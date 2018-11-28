#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm> 
#include <utility>
#include <stack>
#include <queue> 
#include <cmath>
#include <map>
#include <sstream>
#include <functional>
#include <numeric>

#define mp make_pair
#define pb push_back

using namespace std;

long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
pair<int, int> count(int a, int k){
	int ret = 0;
	while(a<=k){
		a += (a-1);
		ret++;
	}
	return mp(a, ret);
}
int main(int argc, char *argv[]){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++){
    	printf("Case #%d: ", tt);
    	int a, n;
    	vector<int>v;
    	scanf("%d%d", &a, &n);
    	for(int i=0; i<n; i++){
    		int k;
    		scanf("%d", &k);
    		v.pb(k);
    	}
    	if(a==1)printf("%d\n", n);
    	else{
	    	sort(v.begin(), v.end());
	    	int ret = 0;
	    	for(int i=0; i<v.size(); i++){
	    		if(v[i]<a){
	    			a+=v[i];
	    			//printf("\nk = %d, a = %d, ret = %d", v[i], a, ret);
	    		}else{
		    		pair<int, int>temp = count(a, v[i]);
		    		if(temp.second<v.size()-i){
		    			ret += temp.second;
		    			a = temp.first + v[i];
		    			//printf("\nk = %d, a = %d, ret = %d, temp = %d", v[i], a, ret, temp.first);
		    		}else{
		    			ret += v.size()-i;
		    			//printf("\nk = %d, a = %d, ret = %d, temp = %d", v[i], a, ret, temp.first);
		    			break;
		    		}
	    		}
	    	}
	    	printf("%d\n", ret);
    	}
    }
    return 0;
}