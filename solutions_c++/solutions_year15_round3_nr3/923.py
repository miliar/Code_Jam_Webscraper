#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cmath>
#include <set>

using namespace std;
set<int> st;

void find(vector<int> val){
	st = set<int>();
	int l= val.size();
    unsigned int psize = pow(2,l);
    for(int cnt = 0; cnt < psize; cnt++){
      int sm=0;
      for(int j = 0;j < l; j++){    
	        if(cnt & (1<<j)){
			    	sm+=val[j];
	        }
       }
       st.insert(sm);
    }
}
 
int main(){
	int t;
	cin>>t;
	for(int h=0;h<t;h++){
		int c,d,v,cnt=0;
		cin>>c>>d>>v;
		vector<int> val(d);
		st = set<int>();
		for(int i=0;i<d;i++){
			int temp;
			cin>>temp;
			val.push_back(temp);
		}	
		find(val);	
		for(int i=1;i<=v;i++){	
			if(st.count(i)>0){
				continue;
			}
			else{
				val.push_back(i);
				find(val);
				cnt++;
			}	
		}
		cout<<"Case #"<<(h+1)<<": "<<cnt<<endl;
	}
}
