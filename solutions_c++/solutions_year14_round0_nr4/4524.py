#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int main(){
	map<double, bool> a, b, a2, b2;
	int T;
	int n;
	int ans;
	double tmp;
	cin>>T;
	for(int s=0;s<T;s++){
		cin>>n;
		ans=0;
		for(int i=0;i<n;i++){
			cin>>tmp;
			a.insert (pair<double,bool>(tmp,true));
		}
		for(int i=0;i<n;i++){
			cin>>tmp;
			b.insert (pair<double,bool>(tmp,true));
		}
		a2=a;
		b2=b;
		while(a.size()){
			map<double, bool>::iterator t1, t2;
			t1=a.end();
			t2=b.end();
			t1--;
			t2--;
			//cout<<t1->first<<"  "<<t2->first<<endl;
			
			if(a.rbegin()->first>b.rbegin()->first){
				a.erase(t1);
				b.erase(t2);
				ans++;
			}
			else{
				a.erase(a.begin());
				b.erase(t2);
			}
		}
		cout<<"Case #"<<s+1<<": "<<ans<<" ";
		ans=0;
		while(a2.size()){
		//cout<<a2.begin()->first<<endl;
			if(b2.lower_bound(a2.begin()->first)!=b2.end()){
				b2.erase(b2.lower_bound(a2.begin()->first));
			}
			else{
				b2.erase(b2.begin());
				ans++;
			}
			a2.erase(a2.begin());
		}
		cout<<ans<<endl;
		a.clear();
		b.clear();
		
		
	}

	return 0;
}