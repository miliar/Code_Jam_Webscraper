#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin>>t;
	for (int metal= 1; metal<=t; metal++){
		int r, c, w;
		cin>>r>>c>>w;
		if (r==1){
			if (w==c){
				cout<<"Case #"<<metal<<": "<<w<<endl;
			}
			else if (c%w==0){
				cout<<"Case #"<<metal<<": "<<c/w+w-1<<endl;
			}
			else{
				cout<<"Case #"<<metal<<": "<<c/w+w<<endl;
			}
		}
	}
	return 0;
}