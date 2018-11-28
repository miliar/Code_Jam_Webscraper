#include<iostream>


using namespace std;

int main(){
	int ts; cin>>ts;
	int tt =1;
	while(ts--){
	int x, y,z; cin>>x>>y>>z;
	cout <<"Case #" << tt++ << ": ";
	for(int i = 1; i<=x; i++){
		cout << i << " ";
	}
	cout << "\n";
	}
}
