#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#include<vector>
#include<list>
#include<map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)

int search(int a,int b) {




	}

int main() {
	freopen("A-small-attempt0.in", "r", stdin); freopen("A-small.out", "w", stdout);

	int T,r,t,ans,val,tot;

	scanf("%d",&T);

	for(int i=1;i<=T;i++) {
		scanf("%d %d",&r,&t);
		ans=0;
		val=2*r+1;tot=0;
		for(;tot<=t;ans++,val+=4) {
			tot+=val;
			//cout<<tot<<" "<<val<<" "<<ans<<endl;
			}
		ans--;
		printf("Case #%d: %d\n",i,ans);
		}

	return 0;
	}
