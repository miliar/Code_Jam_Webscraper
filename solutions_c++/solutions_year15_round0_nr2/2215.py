#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

bool check(vector<int> &v, int m){
	//if(*max_element(v.begin(),v.end()) <= m) 
	//	return true;
	/*int sp = 0, res = 0, ac;
	for(int i=int(v.size())-1;i>=0;i--){
			ac = (v[i]+sp+1)/m;
			if(ac > 0){
				res = max(res, v[i]/(ac+1) + (v[i]%(ac+1) > 0?1:0) );
				sp += ac;
			}
			else break;
	}
	return (sp+res) <= m;*/
	for(int inte = 0; inte < m; inte++){
		int aci = 0;
		int rm = inte;
		bool ok = true;
		for(int i=int(v.size())-1;i >= 0;i--){
			aci += ((v[i]-1)/(m-inte));
			//aci += (v[i]+inte)/m;
			//aci = (v[i]/(1+rm)) + (v[i]%(1+rm) > 0?1:0);
			if(aci > inte){ ok = false; break;}
		}	
		if(ok ) return true;
	}
	return false;
}

int main(){
	int kases; cin>>kases;
	for(int kase = 1; kase <= kases; kase++){
		int D; cin>>D;
		vector<int> v(D);
		for(int i=0;i<D;i++) cin>>v[i];
		sort(v.begin(), v.end());
		int mr = 1, Mr = 1000, mid;
		while(mr < Mr){
			mid = (mr+Mr)/2; 
			if(check(v, mid)) Mr = mid;
			else mr = mid+1;
			//cout<<mr<<" "<<Mr<<endl;
		}
		cout<<"Case #"<<kase<<": "<<mr<<endl;	
	}
}
