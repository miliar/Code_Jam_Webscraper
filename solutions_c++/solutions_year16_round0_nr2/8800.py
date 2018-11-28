#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, j;
	string N;
	long long int num_node;
	long long int final_flip;
	cin>>t;

	for(int i = 1;i<=t;++i){
		cin>>N;
		final_flip = 0;
		num_node = 0;
		while(num_node < N.size()){
			
			num_node = 0;
			
			if(N[0] == '-'){
				N[0] = '+';
				++num_node;
				j = 1;
				while(j<N.size() && (N[j] == '-')){
					N[j] = '+';
					++num_node;
					++j;
				}
				++final_flip;
				
			}else{
				N[0] = '-';
				++num_node;
				j = 1;
				while(j<N.size() && (N[j] == '+')){
					N[j] = '-';
					++num_node;
					++j;
				}
				if(num_node < N.size())
					++final_flip;
			}
		}
		cout<<"Case #"<<i<<": "<<final_flip<<endl;
	}
	return 0;
}