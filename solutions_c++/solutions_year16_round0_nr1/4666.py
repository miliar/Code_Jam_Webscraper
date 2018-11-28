#include <iostream>
using namespace std;



int main() {
	// your code goes here
	int t;
	bool visited[10];
	cin>>t;
	for(int i=1; i<=t; i++){
		long long N;
		cin>>N;
		
		for(int j =0; j<10; j++){
			visited[j] = false;
		}
		int count = 0;
		int mul = 1;
		long long cur;
		if(N == 0)
			goto p;
		while(count < 10 ){
			cur = N*mul;
			while(cur){
				if(!visited[cur%10]){
					visited[cur%10] = true;
					count++;
				}
				cur /= 10;
			}
		mul += 1;
		}
		
		mul--;
		
		p:
		if(count == 10)
			cout<<"Case #"<<i<<": "<<N*mul<<endl;
		else
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
	}
	return 0;
}