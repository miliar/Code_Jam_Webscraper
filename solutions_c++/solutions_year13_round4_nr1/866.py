#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <vector>

using namespace std;

int main(){
	int T;

	cin >> T;

	for(int t=1;t<=T;t++){
		int N,M;
		cin >> N >> M;

		vector<pair<int,int> > Set;

		long long sum = 0;
		for(int i=0;i<M;i++){
			int o,e,p;
			cin >> o >> e >> p;
			for(int i=0;i<p;i++){
				Set.push_back(make_pair(o,e));
				sum += (e-o)*N - (e-o)*(e-o-1)/2;
			}
		}


		
		while(true){
			bool swapped = false;
			for(int i=0;i<Set.size();i++){
				for(int j=i+1;j<Set.size();j++){
					int o1 = Set[i].first;
					int e1 = Set[i].second;
					int o2 = Set[j].first;
					int e2 = Set[j].second;
					
					if(o1>o2){
						int temp1 = o1;
						int temp2 = e1;
						o1 = o2;
						e1 = e2;
						o2 = temp1;
						e2 = temp2;
					}
					if(e1<o2)continue;
					if(o2>=o1&&e2<=e1) continue;
					Set[i] = make_pair(o1,e2);
					Set[j] = make_pair(o2,e1);
					swapped = true;
				}
			}
			if(!swapped) break;
		}

		long long newsum = 0;
		for(int i=0;i<Set.size();i++){
			int o = Set[i].first;
			int e = Set[i].second;
			newsum += (e-o)*N - (e-o)*(e-o-1)/2;
		}
		cout<<"Case #"<<t<<": "<<(sum-newsum)%1000002013<<endl;
	}

	
}