#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int T, S_max;
	int c;
	
	cin>>T;
	for(int t=0;t<T;t++){
		cin>>S_max;
		int alreadyClapping = 0, required = 0;
		//reading 1 whitespace
		c = getchar();
		
		for(int k=0;k<S_max+1;k++){
			c = getchar();
			int current_shyness_count = c-48;
			
			if(alreadyClapping < k  && current_shyness_count!=0){
				required += (k-alreadyClapping);
				alreadyClapping+=(k-alreadyClapping);
			}
			alreadyClapping+=current_shyness_count;

		}
		cout<<"Case #"<<t+1<<": "<<required<<endl;
	}
	
	return 0;
}
