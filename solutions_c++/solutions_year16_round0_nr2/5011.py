#include<iostream>
using namespace std;
string a;
int n, res;
int main(){
	cin>>n;
	for(int i = 0; i < n; i++){
		cin>>a;
		cout<<"CASE #"<<i+1<<": ";
		res = 0;
		int len = a.size();
		for(int i = 1; i < len; i++){
			if(a[i] != a[i-1]){
				res++;
			}
		}
		if(a[a.size()-1] == '-') res++;
		cout<<res<<endl;
	}
	
	return 0;
}
