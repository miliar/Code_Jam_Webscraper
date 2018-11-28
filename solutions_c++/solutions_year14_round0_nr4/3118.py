#include <bits/stdc++.h>
using namespace std;
int ntc, n;
double tmp;
priority_queue<double, vector<double>, greater<double> > pq;
deque<double> de;
set<double> s;
int main(){
	scanf("%i", &ntc);
	for(int tc=1;tc<=ntc;tc++){
		scanf("%i", &n);
		int ans1 = 0, ans2 = 0;
		for(int i=0;i<n;i++){
			scanf("%lf", &tmp);
			pq.push(tmp);
		}
		for(int i=0;i<n;i++){
			scanf("%lf", &tmp);
			s.insert(tmp);
			de.push_back(tmp);
		}
		sort(de.begin(), de.end());
		while(!pq.empty()){
			float a = pq.top();
			pq.pop();
			set<double>::iterator itr = s.upper_bound(a);
			if(itr == s.end()) { ans2++; s.erase(s.begin()); }
			else s.erase(itr);
			if(a < de[0]) de.pop_back();
			else{
				de.pop_front();
				ans1++;
			}
		}
		printf("Case #%i: %i %i\n", tc, ans1 , ans2);
	}
}