#define debug


#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <string>
#include <set>
#include <queue>
#include <cstdlib>
#include <fstream>
#include <map>
#include <sstream>
#include <iterator>
#include <bitset>
#include <cctype>
#include <cmath>
#include <functional>
#include <iomanip>
#include <list>
#include <numeric>
#include <stack>
#include <utility>
#include <cassert>
#include <conio.h>
#include <concurrent_priority_queue.h>
using namespace std;
#define ll long long



/*
int a[20],b[20],c[20],d[20];
vector<int> ans;
int n;
bool check() {

	for(int i=0; i<n; i++) {
		c[i] = 1;
		for(int j=i-1; j>=0; j--) {
			if(ans[j]<ans[i]) {
				c[i] = max(c[i],c[j]+1);
			}
		}
	}
	for(int i=n-1; i>=0; i--) {
		d[i] = 1;
		for(int j=i+1; j<n; j++) {
			if(ans[j]<ans[i]) {
				d[i] = max(d[i],d[j]+1);
			}
		}
	}

	for(int i=0; i<n; i++) {
		if(a[i]!=c[i] || b[i]!=d[i]) {
			return false;
		}
	}

	return true;
}
void main2() {
	int t;
	scanf("%d",&t);
	for(int z=0; z<t; z++) {
		ans.clear();
		scanf("%d",&n);
		for(int i=0; i<n ;i++) {
			scanf("%d",&a[i]);
		}
		for(int i=0; i<n ;i++) {
			scanf("%d",&b[i]);
		}
		for(int i=1; i<=n; i++) {
			ans.push_back(i);
		}
		do {
			if(check()) break;
		} while(next_permutation(ans.begin(),ans.end()));

		printf("Case #%d: ",(z+1));
		for(int i=0; i<n; i++) {
			printf("%d ",ans[i]);
		}
		printf("\n");
	}


}





*/
int t;
ll n,m;
ll o[1000],p[1000],e[1000];
ll mod;

void main2() {
	int t;
	mod = 1000002013;
	scanf("%d",&t);
	for(int z=0; z<t; z++) {
		printf("Case #%d: ",(z+1));
		scanf("%lld",&n);
		scanf("%lld",&m);
		//printf("%lld %lld\n",n,m);
		for(ll i=0; i<m; i++) {
			scanf("%lld %lld %lld",&o[i],&e[i],&p[i]);
			//printf("%lld %lld %lld\n",o[i],e[i],p[i]);
		}
		ll tot1 = 0;
		for(ll i=0; i<m; i++) {
			ll tot3 = e[i]-o[i];
			ll tot2 =(n*tot3-(tot3*(tot3-1))/2);
			tot2%=mod;
			tot2*=p[i];
			tot2%=mod;
			tot1+=tot2;
			tot1%=mod;
			//printf("%lld\n",tot2);
		}
		vector<ll> data;
		for(ll i=0; i<m; i++) {
			data.push_back(e[i]);
		}
		sort(data.begin(),data.end());
		vector<ll>::iterator it = unique(data.begin(),data.end());
		data.resize(std::distance(data.begin(),it));
		ll tot2 = 0;
		map<ll,ll> data2;
		for(int i=0; i<data.size(); i++) {
			//printf("%lld\n",data[i]);
			for(map<ll,ll>::reverse_iterator it2 = data2.rbegin(); it2!=data2.rend(); it2++) {
				data2[it2->first+data[i]-data[i-1]] = it2->second;
				data2[it2->first] = 0;
			}
			ll s1 = i!=0 ? data[i-1]: -1;
			for(ll j=0; j<m; j++) {
				if(o[j]>s1 && o[j]<=data[i]) {
					data2[data[i]-o[j]]+=p[j];
				}
			}
			map<ll,ll>::iterator it2 = data2.begin();
			ll totp = 0;			
			for(ll j=0; j<m; j++) {
				if(data[i]==e[j]) totp+=p[j];
			}
			//cout<<totp<<endl;
			while(totp>0) {
				if(it2->second<totp) {
					ll tot3 =(n*it2->first-it2->first*(it2->first-1)/2);
					tot3%=mod;
					tot3*=it2->second;
					tot3%=mod;
					tot2+=tot3;
					tot2%=mod;
					totp-=it2->second;
					it2->second = 0;
				}
				else {
					ll tot3=(n*it2->first-it2->first*(it2->first-1)/2);
					tot3%=mod;
					tot3*=totp;
					tot3%=mod;
					tot2+=tot3;
					tot2%=mod;
					it2->second-=totp;
					totp = 0;
				}
				it2++;
			}
			/*
			for(map<ll,ll>::iterator it2 = data2.begin(); it2!=data2.end(); it2++) {
				printf("%lld %lld\n",it2->first,it2->second);
			}
			cout<<tot2<<endl;
			*/

		}
		printf("%lld\n",(tot1-tot2)%1000002013);
	}
	

}





int main() {
	//freopen("A-large-practice (2).in","r",stdin);
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	main2();
	return 0;
}

