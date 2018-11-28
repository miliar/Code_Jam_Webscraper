
/*Paresh Verma*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <queue>		//max heap implementation
#include <limits.h>

#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define LL long long
#define fill(x,y) memset(x, y, sizeof(x))
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
	public:
		bool operator() (const int& l, const int& r)const{
			return l<r;
		}
};

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

bool ispalin(long long x){
	char s[20];
	sprintf(s,"%lld",x);
	int i,j,k;
	i=0; j=strlen(s)-1;
	while(i<j){
		if(s[i]!=s[j])
			return false;
		i++; j--;
	}
	return true;
}

#define maxn 10000010
vector<long long> num;

int main(){
	long long i,j,k,l;
	for(i=1;i<maxn;i++){
		if(ispalin(i) && ispalin(i*i)){
			num.pub(i*i);
		}
	}
	int T;
	scanf("%d",&T);
	for(int p=1;p<=T;p++){
		long long  a,b;
		scanf("%lld%lld",&a,&b);
		printf("Case #%d: ", p);
		long long s,e,m,i1,i2;
		s=0; e=num.size()-1;
		while(s<=e){
			m=(s+e)/2;
			if(num[m]>=a){
				i1=m;
				e=m-1;
			}
			else{
				s=m+1;
			}
		}
		s=0; e=num.size()-1;
		while(s<=e){
			m=(s+e)/2;
			if(num[m]<=b){
				i2=m;
				s=m+1;
			}
			else{
				e=m-1;
			}
		}
//		cout << i1 << " " << i2 <<endl;
		printf("%lld\n", i2-i1+1);
	}
	return 0;
}
