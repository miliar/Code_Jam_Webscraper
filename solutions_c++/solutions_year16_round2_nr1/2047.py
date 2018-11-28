//GCJ - !B Prob A
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<cstring>
#include<string>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define OO (int)2e9
#define INF (ll)9e18
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
using namespace std;

int t,l,n;
char s[2005];
int dat[30];
vector<int>res;
vector<int>::iterator it;

int main(){
	scanf("%d",&t);
	repp(tc,1,t){
		while(!res.empty())res.pob();
		repp(i,0,28)dat[i]=0;
		n=0;
		scanf("%s",s);
		l=strlen(s);
		repp(i,1,l)dat[s[i-1]-'A'+1]++;
		//Z ZERO
		while(dat[26]--){
			dat[5]--;
			dat[18]--;
			dat[15]--;
			res.pb(0);
			n++;
		}
		//W TWO
		while(dat[23]--){
			dat[20]--;
			dat[15]--;
			res.pb(2);
			n++;
		}
		//X SIX
		while(dat[24]--){
			dat[19]--;
			dat[9]--;
			res.pb(6);
			n++;
		}
		//G EIGHT
		while(dat[7]--){
			dat[5]--;
			dat[9]--;
			dat[8]--;
			dat[20]--;
			res.pb(8);
			n++;
		}
		//S SEVEN
		while(dat[19]--){
			dat[5]--;
			dat[22]--;
			dat[5]--;
			dat[14]--;
			res.pb(7);
			n++;
		}
		//T THREE
		while(dat[20]--){
			dat[8]--;
			dat[18]--;
			dat[5]--;
			dat[5]--;
			res.pb(3);
			n++;
		}
		//R FOUR
		while(dat[18]--){
			dat[6]--;
			dat[15]--;
			dat[21]--;
			res.pb(4);
			n++;
		}
		//O ONE
		while(dat[15]--){
			dat[14]--;
			dat[5]--;
			res.pb(1);
			n++;
		}
		//N NINE
		while(dat[14]--){
			dat[9]--;
			dat[14]--;
			dat[5]--;
			res.pb(9);
			n++;
		}
		//F FIVE
		while(dat[6]--){
			dat[9]--;
			dat[22]--;
			dat[5]--;
			res.pb(5);
			n++;
		}
		sort(res.begin(),res.begin()+n);
		printf("Case #%d: ",tc);
		for(it=res.begin();it!=res.end();it++){
			printf("%d",*it);
		}
		printf("\n");
	}
	return 0;
}
