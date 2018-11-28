#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

class party{
public:
	int idx;
	int c;
};
vector<party> counts;

bool operator<(party const & a, party const & b){
    return a.c > b.c;
}

int main() {
    freopen("/Users/Shiva/Desktop/input.in", "r", stdin);
    freopen("/Users/Shiva/Desktop/output", "w", stdout);
    int t=0;
    cin>>t; int tc = 1;
    while(t--){
    	counts.clear();
    	int v,n,sum = 0;
    	cin>>v;
    	n = v;
    	int idx = 0;
    	while(v--){
    		int c;
    		cin>>c;
    		party p; p.idx = idx; p.c = c;
    		counts.push_back(p);
    		sum += c;
    		idx++;
    	}
		vector<int> e;
		cout<<"Case #"<<tc<<": ";
    	while(sum > 0){
    		int maj = (sum-2)/2;
    		e.clear();
    		std::sort(counts.begin(), counts.end());
    		
    		for(int i=0;i<counts.size();i++){
    			if(counts[i].c > 0 && maj <= counts[i].c && e.size() < 2){
    				e.push_back(i);
    			}
    			if(e.size() > 2){
    				cout<<"problem "<<endl;
    				break;
    			}
    		}
    		if(sum == 3){
    			bool threeCon = true;
    			for(int i=0;i<counts.size();i++){
    				if(counts[i].c != 1){
    					threeCon = false;
    				}
    			}
    			if(threeCon){
    				char car = 65 + counts[e[0]].idx;
    				cout<<car<<" ";
    				counts[e[0]].c -= 1;
    				sum -= 1;
    				continue;
    			}
    		}
    		if(e.size() > 0){
    			for(int i=0;i<e.size();i++){
    				int sub =  2/e.size();
    				counts[e[i]].c -= sub; 
    				if((sub) == 2){
    					char car = 65 + counts[e[i]].idx;
    					cout<<car<<car;
    				}else{
    					
    					char car = 65 + counts[e[i]].idx;
    					cout<<car;
    				}
    				if(i+1 == e.size()){
    					cout<<" ";
    				}
    			}
    			sum -= 2;
    		}else{
    			cout<<"problem "<<endl;
    		}
    	}
    	cout<<endl;
		tc++;
    }
    return 0;
}