#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int A[5]={1,4,9,121,484};
	int T;
	cin>>T;
	for(int u=1;u<=T;++u){
		int a,b;
		cin>>a>>b;
		int res=0;
		for(int i=0;i<5;++i)
			if(A[i]>=a&&A[i]<=b)
				++res;
		cout<<"Case #"<<u<<": "<<res<<endl;
		
	}
	return  0;
}
