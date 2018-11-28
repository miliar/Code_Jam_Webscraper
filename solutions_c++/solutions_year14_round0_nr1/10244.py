#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main(){
	int T,p,x,i,j;
	cin>>T;
	
	set<int> cisla;
	vector<int> ries;
	
	
	for(int xyz=0;xyz<T;xyz++){
		ries.resize(0);
		cisla.erase(cisla.begin(),cisla.end());
		cin>>p;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>x;
				if(i==p-1){
					cisla.insert(x);
					//cout<<x<<endl;
				}
			}
			
		}
		cin>>p;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>x;
				if(i==p-1){
					if(cisla.count(x)){
						ries.push_back(x);
						//cout<<x<<endl;
					}
				}
			}
		}
		cout<<"Case #"<<xyz+1<<": ";
		if(ries.size()==0){
			cout<<"Volunteer cheated!";
		} else if(ries.size()>1){
			cout<<"Bad magician!";
		} else {
			cout<<ries[0];
		}
		cout<<"\n";
	}
	return 0;
}
