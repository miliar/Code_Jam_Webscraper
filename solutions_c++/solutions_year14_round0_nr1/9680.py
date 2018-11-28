#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t,ans;
	cin>>t;
	for(int caso=1; caso<=t;caso++){
		set<int> s;
		vector<int> v;
		for(int i=0;i<2;i++){
			cin>>ans;
			ans--;
			for(int j=0;j<4;j++)
				for(int k=0;k<4;k++){
					int celd;
					cin>>celd;
					if(j==ans){
						s.insert(celd);
						v.push_back(celd);
					}
				}
		}
		if(s.size()==8){
			cout<<"Case #"<<caso<<": Volunteer cheated!"<<endl;
		}
		if(s.size()<=6){
			cout<<"Case #"<<caso<<": Bad magician!"<<endl;
		}
		if(s.size()==7){
			int resp;
			sort(v.begin(),v.end());
			for(int l=1;l<v.size();l++){
				if(v[l]==v[l-1]){
					resp=v[l];
					break;
				}
			}
			cout<<"Case #"<<caso<<": "<<resp<<endl;
		}
		
	}
	return 0;
}
