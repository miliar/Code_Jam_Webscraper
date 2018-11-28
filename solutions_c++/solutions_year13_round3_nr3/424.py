#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <limits.h>
//#include <sys/time.h>
//#include <time.h>
using namespace std;
#define ll long long
ll h[3000];
int main(void)
{
	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t)
	{
		int N;
		cin>>N;
		vector <int> d(N),n(N),w(N),e(N),s(N),del_d(N),del_p(N),del_s(N);
		for(int i=0;i<N;++i){
			cin>>d[i]>>n[i]>>w[i]>>e[i]>>s[i]>>del_d[i]>>del_p[i]>>del_s[i];
		}

		vector <ll> dd,ww,ee,ss;
		for(int i=0;i<N;++i){
			ll pd=d[i],pw=w[i],pe=e[i],ps=s[i];
			dd.push_back(pd);
			ww.push_back(pw);
			ee.push_back(pe);
			ss.push_back(ps);
			for(int j=1;j<n[i];++j){
				dd.push_back(pd+del_d[i]);
				ww.push_back(pw+del_p[i]);
				ee.push_back(pe+del_p[i]);
				ss.push_back(ps+del_s[i]);
				pd=pd+del_d[i];
				pw=pw+del_p[i];
				pe=pe+del_p[i];
				ps=ps+del_s[i];
			}

		}

		for(int i=0;i<dd.size();++i){
			for(int j=i+1;j<dd.size();++j){
				if(dd[i]>dd[j]){
					swap(dd[i],dd[j]);
					swap(ww[i],ww[j]);
					swap(ss[i],ss[j]);
					swap(ee[i],ee[j]);
				}
			}
		}
#if 0
for(int i=0;i<dd.size();++i){
	cout<<dd[i]<<";"<<ww[i]<<";"<<ee[i]<<";"<<ss[i]<<endl;
}
#endif

		const int cent=500;
		memset(h,0,sizeof(h));
		int result=0;
		vector <pair <int,int> > interval;
		vector <ll> attack;
		int prevday=-1;
		for(int i=0;i<dd.size();++i){
			bool fail=false;
			for(int j=ww[i];j<=ee[i];++j){
				int pos0=(j+cent)*2;
				int pos1=(j+cent)*2+1;
				if(j==ee[i])pos1=pos0;
				if(h[pos0]>=ss[i]&&h[pos1]>=ss[i]){
				}else{
					attack.push_back(ss[i]);
					interval.push_back(pair<int,int>(pos0,pos1));
					//h[pos0]=max(h[pos0],(ll)ss[i]);
					//h[pos1]=max(h[pos1],(ll)ss[i]);
					fail=true;;
				}
			}
			if(fail){
				++result;
			}else{
			}
			if(i==N-1||dd[i+1]!=dd[i]){
				for(int j=0;j<attack.size();++j){
					int pos0=interval[j].first;
					int pos1=interval[j].second;
					for(int k=pos0;k<=pos1;++k){
						h[k]=max(h[k],(ll)attack[j]);
					}
				}
				attack.clear();
				interval.clear();
			}
		}
		cout<<"Case #"<<_t<<": "<<result<<endl;
		cerr<<"cerr:"<<endl;
	}

}


//	cout.setf(ios::fixed);

