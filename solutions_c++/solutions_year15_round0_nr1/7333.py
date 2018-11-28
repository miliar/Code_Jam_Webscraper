#include <iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	int p=1;
	while(t--){
		int n;
		string s;
		cin>>n>>s;
		int add=0;
		int total=0;
		for(int q=0;q<=n;q++){
			if(q>total){
				add+=q-total;
				total=q;
			}
			total+=s[q]-'0';
		}
		cout<<"Case #"<<p++<<": "<<add<<endl;
	}
}
