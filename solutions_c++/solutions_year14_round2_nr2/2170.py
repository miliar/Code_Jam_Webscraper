#include <iostream>
#include <string>
#include <cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;


int main() {
	int T,t,a,b,k,count,num;
	cin>>T;
	for(t=1;t<=T;++t){
		count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;++i)
			for(int j=0;j<b;++j){
				if((i&j)<k){
					++count;
				}
			}
		cout<<"Case #"<<t<<": "<<count<<endl;;

	}
	return 0;
}
