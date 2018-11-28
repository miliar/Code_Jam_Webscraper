#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>
#include <iomanip>

#define long long
#define mp make_pair

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >>test;
	for (int t=1; t<=test; ++t){
		long n;
		cin >>n;
		set<long> st;
		long m;
		cin >>m;
		vector<pair<long,long> > path(m);
		vector<long> num(m);
		for (int i=0; i<m; ++i){
			cin >>path[i].first >>path[i].second >>num[i];
			st.insert(path[i].first);
			st.insert(path[i].second);
		}
		int kol=st.size();
		vector<long> in(kol),out(kol),cards(kol),tr(kol);
		map<long,long> pos;
		int cur=0;
		for (set<long>::iterator it=st.begin(); it!=st.end(); ++it){
			tr[cur]=*it;
			pos.insert(make_pair(*it,cur++));
		}
		long min_sum=0;
		for (int i=0; i<m; ++i){
			in[pos[path[i].first]]+=num[i];
			out[pos[path[i].second]]+=num[i];
		}
		for (int i=0; i<kol; ++i){
			cards[i]+=in[i];
			long need=out[i];
			for (int j=i; need>0; --j){
				long q=min(need,cards[j]);
				long dif=tr[i]-tr[j];
				min_sum+=dif*q*(n*2-dif+1)/2;
				need-=q;
				cards[j]-=q;
			}
		}
		long true_sum=0;
		for (int i=0; i<m; ++i)
			true_sum+=(path[i].second-path[i].first)*num[i]*(n*2-path[i].second+path[i].first+1)/2;
		cout <<"Case #" <<t <<": " <<true_sum-min_sum <<endl;
	}
	return 0;
}