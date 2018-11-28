#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string s;
		cin>>s;
		int flip=0;
		char lastVal=s[0];
		for(int i=1;i<s.length();i++){ 
			if(lastVal!=s[i]){
				lastVal=s[i];
				flip++;
			}
		}
		if(lastVal=='-'){
			flip++;
		}
		
		cout<<"Case #"<<i+1<<": ";
		cout<<flip<<endl;
	}
	return 0;
}