#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (int argc, char *argv[]) {
	int t,n;
	cin>>t;
	vector<double> v_naomi, v_ken;
	vector<bool> v_ken_spent;
	for(int tc=0;tc<t;tc++) { 
		v_naomi.clear();
		v_ken.clear();
		v_ken_spent.clear();
		cin>>n;
		v_naomi.resize(n);
		v_ken.resize(n);
		v_ken_spent.resize(n);
		for(int i=0;i<n;i++) { 
			cin>>v_naomi[i];
		}
		for(int i=0;i<n;i++) { 
			cin>>v_ken[i];
			v_ken_spent[i] = false;
		}
		sort(v_naomi.begin(), v_naomi.end());
		sort(v_ken.begin(), v_ken.end());
		int c_w = 0, c_dw = 0;
		bool w_finished = false;
		vector<double>::iterator it = v_ken.begin();
		int j=0;
		for(int i=0;i<n;i++) { 
			if(v_naomi[i] > v_ken[j]){
				c_dw++;
				j++;
			}
			
			if(!w_finished){
				it = upper_bound(it, v_ken.end(), v_naomi[i]);
				if(it == v_ken.end()){
					w_finished = true;
					c_w = n-i;
				}
				else
					it++;
			}
		}
		cout<<"Case #"<<tc+1<<": "<<c_dw<<" "<<c_w<<endl;
	}
	return 0;
}

