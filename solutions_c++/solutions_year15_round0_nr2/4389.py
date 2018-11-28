#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int p[1010],cp[1010];
int main(){
	freopen("f.txt","r",stdin);
	freopen("fout.txt","w",stdout);
	int t,x = 1,y = 1;
	cin >> t;
	while(t--){
		int d,m = 0,fm = 0;
		cin >> d;
		std::vector<pair<double,int>> v;
		for(int i = 0; i < d; i++){
		//	int c,s;
			cin >> p[i];
			cp[i] = p[i];
			v.push_back(make_pair<double,int>((double)p[i],i));
		}
		

		make_heap(v.begin(),v.end());
		fm = v[0].first;
		y = v[0].first;
		int u = 0;
		while(u < y){
			m ++;
			double x = (double)p[v[0].second] / (p[v[0].second] / floor(v[0].first) + 1),pos = v[0].second;
			
			v.erase(v.begin());
			v.push_back(make_pair<double,int>(x,pos));
			make_heap(v.begin(),v.end());
		/*	std::pop_heap (v.begin(),v.end()); v.pop_back();
			v.push_back(make_pair<double,int>(x,pos));
			std::push_heap (v.begin(),v.end());*/
			fm = min(m + (int)ceil(v[0].first), fm);
			u++;

		}
		

		cout << "Case #" << x << ": " << fm << '\n';
		x++;

	}


	return 0;
}