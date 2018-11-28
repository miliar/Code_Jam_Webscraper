#include<iostream>
#include<string>
#include<set>
using namespace std;
string bad="Bad magician!";
string che="Volunteer cheated!";
int main(){
	int T; cin>>T;
	for(int kases=1;kases<=T;kases++){
		int R1,R2,a;
		set<int> S1,S2;
		cin>>R1;
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				cin>>a;
				if(i == R1) S1.insert(a);			
			}		
		}
		cin>>R2;
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				cin>>a;
				if(i == R2 && S1.find(a) != S1.end()) S2.insert(a);			
			}		
		}
		cout<<"Case #"<<kases<<": ";
		if(int(S2.size()) == 1) cout<<*(S2.begin())<<endl;
		else if(int(S2.size()) > 1) cout<<bad<<endl;
		else cout<<che<<endl;
	}
}
