#include<stdio.h>
#include<stdlib.h>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

pair<pair<int,int>,int> a[1024];
priority_queue<pair<int,int> > pq;
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >  q;
int n,m;

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) {
		scanf("%d %d",&n,&m);
		for(int i=0;i<m;i++) scanf("%d %d %d",&a[i].first.first,&a[i].first.second,&a[i].second);
		long long s1=0;
		for(int i=0;i<m;i++) {
			int t=abs(a[i].first.first-a[i].first.second);
			s1+=((long long)n*t-((long long)t*t+t)/2)*a[i].second;
		}
		long long s2=0;
		sort(a,a+m);
		for(int i=0;i<m;i++) {
			while(!q.empty()) {
				int sta=q.top().first;
				if (sta>=a[i].first.first) break;
				int num=q.top().second;
				q.pop();
				while(num) {
					int up=pq.top().first;
					int tic=pq.top().second;
					pq.pop();
					int t=(sta-up);
					int p=tic;
					if (p>num) p=num;
					s2+=((long long)n*t-((long long)t*t+t)/2)*p;
					tic-=p;
					num-=p;
					if (tic>0) pq.push(make_pair(up,tic));
				}
			}
			pq.push(make_pair(a[i].first.first,a[i].second));
			q.push(make_pair(a[i].first.second,a[i].second));
		}
		while(!q.empty()) {
			int sta=q.top().first;
			int num=q.top().second;
			q.pop();
			while(num) {
				int up=pq.top().first;
				int tic=pq.top().second;
				pq.pop();
				int t=(sta-up);
				int p=tic;
				if (p>num) p=num;
				s2+=((long long)n*t-((long long)t*t+t)/2)*p;
				tic-=p;
				num-=p;
				if (tic>0) pq.push(make_pair(up,tic));
			}
		}
		printf("Case #%d: %lld\n",++cs,s1-s2);
	}
	return 0;
}
