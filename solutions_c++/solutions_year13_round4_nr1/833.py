#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
typedef long long ll;
const int base=1000002013;
const int MAXN = 2000;




int main(){
//	freopen("1.txt","r",stdin);

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("AoutSmall.txt","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("AoutLarge.txt","w",stdout);
	int TT;
	cin>>TT;
	for(int T=0;T<TT;T++){
		printf("Case #%d: ",T+1);
		int n,m;
		cin>>n>>m;
		ll ans=0;
		vector<int> b(m*2);
		vector<pair<pair<int,int>, int > > a(m);
		for(int i=0;i<m;i++){
			int A,B,p;
			cin>>A>>B>>p;
			b[i*2]=A;
			b[i*2+1]=B;
			ans = (ans + (n*1ll*(B-A) - (B-A)*1ll*(B-A-1)/2)%base*p%base)%base;
			a[i]=make_pair(make_pair(A,B),p);
		}
		sort(b.begin(),b.end());


		map<int,int> mm;
		mm[b[0]]=0;
		int cnt=1;
		for(int i=1;i<m*2;i++)
			if(b[i]!=b[i-1]){
				mm[b[i]]=cnt;
				b[cnt]=b[i];
				cnt++;
			}
		b.resize(cnt);

		vector<ll> c(cnt);
		for(int i=0;i<m;i++){
			a[i].first.first=mm[a[i].first.first];
			a[i].first.second=mm[a[i].first.second];
			for(int j=a[i].first.first;j<a[i].first.second;j++)
				c[j] += a[i].second;
		}

		vector<int> g(cnt);
		g[0]=b[0];
		for(int i=1;i<cnt;i++){
			g[i]=b[i];
			b[i-1]=b[i]-b[i-1];
		}
		b[cnt-1]=0;

		vector<pair<int, pair<int,int> > > h;
		for(int i=0;i<cnt-1;i++)
			for(int j=i;j<cnt-1;j++)
				h.push_back(make_pair(g[j+1]-g[i],make_pair(i,j)));
		sort(h.begin(),h.end());
		reverse(h.begin(),h.end());

		ll res=0;

		for(int i=0;i<h.size();i++){
			ll ma=1ll<<60;
			for(int j=h[i].second.first;j<=h[i].second.second;j++)
				ma=min(c[j],ma);
			if(ma){
				res = (res + (n*1ll*(h[i].first) - (h[i].first)*1ll*(h[i].first-1)/2)%base*ma%base)%base;
				for(int j=h[i].second.first;j<=h[i].second.second;j++)
					c[j]-=ma;
			}
		}
		
		int u=(ans+base-res)%base;
		printf("%d\n",u);



		//int aa[2000];
		//int bb[2000];
		//memset(aa,0,sizeof(aa));
		//memset(bb,0,sizeof(bb));

		//for(int i=0;i<m;i++){
		//	a[i].second.first=a[i].first.second-a[i].first.first-1;
		//	a[i].first.first=mm[a[i].first.first];
		//	a[i].first.second=mm[a[i].first.second];
		//	for(int j=a[i].first.first;j<a[i].first.second;j++)
		//		aa[j]=(aa[j]+a[i].second.second)%base;
		//}

		//build(bb,aa,1,0,cnt-1);




		//int su=0;
		//set<pair<int, pair<int,int> > > s;
		//sort(a.begin(),a.end());

		//
		//
		//vector<int> ddd;

		//for(int i=0;i<m;i++){
		//	a[i].second.first=a[i].first.second-a[i].first.first-1;
		//	a[i].first.first=mm[a[i].first.first];
		//	a[i].first.second=mm[a[i].first.second];
		//}

		//memset(d,0,sizeof(d));
		//set<pair<int, int > > ss[2000];


		//for(int i=0;i<m;i++){
		//	d[a[i].first.second]
		//}





		
		
	}
}

//int main(){
////	freopen("1.txt","r",stdin);
//
////	freopen("A-small-attempt1.in","r",stdin);
////	freopen("AoutSmall.txt","w",stdout);
//
////	freopen("A-large.in","r",stdin);
////	freopen("AoutLarge.txt","w",stdout);
//	int TT;
//	cin>>TT;
//	for(int T=0;T<TT;T++){
//		printf("Case #%d: ",T+1);
//		int n,m;
//		cin>>n>>m;
//		ll ans=0;
//		vector<pair<pair<int,int>, pair<int, int> > > a(n);
//		vector<int> b(n*2);
//		for(int i=0;i<m;i++){
//			int A,B,p;
//			cin>>A>>B>>p;
//			b[i*2]=A;
//			b[i*2+1]=B;
//			ans = (ans + n*1ll*(B-A+1) - (B-A)*(B-A+1)/2)%base;
//			a.push_back(make_pair(make_pair(A,B),make_pair(0,p)));
//		}
//		int su=0;
//		set<pair<int, pair<int,int> > > s;
//		sort(a.begin(),a.end());
//		sort(b.begin(),b.end());
//		map<int,int> mm;
//		mm[b[0]]=0;
//		int cnt=1;
//		for(int i=1;i<N*2;i++)
//			if(b[i]!=b[i-1])
//				mm[b[i]]=cnt++;
//		
//		vector<int> ddd;
//
//		for(int i=0;i<m;i++){
//			a[i].second.first=a[i].first.second-a[i].first.first-1;
//			a[i].first.first=mm[a[i].first.first];
//			a[i].first.second=mm[a[i].first.second];
//		}
//
//		memset(d,0,sizeof(d));
//		set<pair<int, int > > ss[2000];
//
//
//		for(int i=0;i<m;i++){
//			d[a[i].first.second]
//		}
//
//
//
//
//
//		
//		
//	}
//}
