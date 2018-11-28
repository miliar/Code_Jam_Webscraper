#include <iostream>
#include <vector>
#include <string>
using namespace std;

int happy=0,sad=1;
vector<int> c;

int f(int n,int face){
	if(n<0) return 0;
	if(c[n]==face){
		return f(n-1,face);
	} else {
		int tmp=f(n-1,c[n])+1;
		for(int i=0,j=n;i<=j;i++,j--){
			c[i]=1-c[i];
			if(i!=j){
				c[j]=1-c[j];
				swap(c[i],c[j]);
			}
		}
		if(c[n]==face){
			tmp=min(tmp,f(n-1,face)+1);
		} else {
			tmp=min(tmp,f(n-1,c[n])+2);
		}
		for(int i=0,j=n;i<=j;i++,j--){
			c[i]=1-c[i];
			if(i!=j){
				c[j]=1-c[j];
				swap(c[i],c[j]);
			}
		}
		return tmp;
	}
}

int main(){
	int t;
	cin>>t;
	int n;
	string s;
	for(int i=1;i<=t;i++){
		cin>>s;
		n=s.size();
		c=vector<int>(n);
		for(int j=0;j<n;j++) 
			c[j]= s[j]=='+' ? 0:1;
		cout<<"Case #"<<i<<": "<<f(n-1,happy)<<endl;
	}
	return 0;
}