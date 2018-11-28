#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int m1[1001], ans, t, n, h1, h2;

bool check(deque<int>& dq){
	bool desc = 0;
	int pre = -1;
	for(deque<int>::iterator i = dq.begin() ; i != dq.end() ; i ++){
		if((*i) > pre){
			if(desc) return 0;
		}
		else{
			if(!desc) desc = 1;
		}
		pre = (*i);
	}
	return true;
}

int main(int argc, const char *argv[])
{
	int cc = 0;
	cin>>t;
	while(t--){
		cin>> n;
//		cout<<"n:"<<n<<endl;
		deque<int> dq;
		for(h1 = 0 ; h1 < n ; h1 ++){
			cin>>m1[h1];
			dq.push_back(m1[h1]);
		}
		ans = 0;

		while(!check(dq)){
			int mn_idx = 0, mx_idx = 0, idx = 0, cidx = 0;
			deque<int>::iterator mn = dq.begin(), mx = dq.begin(), i = dq.begin();
			for( ; i != dq.end() ; i ++, idx ++){
				if((*i) == -1){ cidx = idx; continue; }
				if((*i) < (*mn)){ mn = i; mn_idx = idx; }
				if((*i) >= (*mx)){ mx = i; mx_idx = idx; }
			}
			int size = dq.size();
			ans += min(size -1 - mn_idx, mn_idx);
			dq.erase(mn);
//			for(int i = 0 ; i < dq.size() ; i ++)
//				cout<< dq[i] << ' ';
//			cout<<endl;
//			cout<<ans<<endl;
		}


		printf("Case #%d: %d\n", ++cc, ans);
	}
	return 0;
}
