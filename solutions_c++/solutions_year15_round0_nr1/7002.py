#include <iostream>
using namespace std;
int main(){
	int N, Smax, level;
	int friends;
	string audience;
	cin>>N;
	for(int i=0; i<N; i++){
		level=friends=0;
		cin>>Smax>>audience;
		for(int j=0; j<Smax+1; j++){
			if(level>=j && audience[j]!='0')
				level+=(audience[j]-'0');
			else if(level<j && audience[j]!='0'){
				int add = j-level;
				friends+=add;
				level+=add+(audience[j]-'0');
			}
		}
		cout<<"Case #"<<i+1<<": "<<friends<<endl;
	}
}
