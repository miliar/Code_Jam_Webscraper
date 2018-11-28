#include <iostream>
#include <string>

using namespace std;

int main(){
	int n,t,count,need,T;
	string s;
	cin>>T;
	for(int z = 0; z<T; z++){
		cin >> n;
		cin >> s;
		count = 0;
		need = 0;
		for(int i=0; i<n+1; i++){
			t=s[i]-'0';
			if(count>=i) count+=t;
			else if(t!=0){
				need+= i-count;
				count+=(need+t);
			}
		}
		cout<<"Case #"<<z+1<<": "<<need<<endl;
	}
}