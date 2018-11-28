#include <bits/stdc++.h>
using namespace std;
int main(){
int t, n;
cin>>t;
for(int j=1; j<=t; j++){
	cin>>n;
	if(n==0){
		cout<<"Case #"<<j<<": INSOMNIA"<<endl;
	}else{
		unsigned long long  x=n, y;
		bool visit[10];
		fill(visit, visit+10, false);
		int i=1,c=0;
		bool check=true;
		while(check){
			y = i*x;
			while(y){
				if(!visit[y%10]){
					c++;
					visit[y%10]=true;
				}
				if(c==10){
					cout<<"Case #"<<j<<": "<<(i*x)<<endl;
					check=false;
					break;
				}
				y=y/10;
			}
			i++;
		}
	}
}
}
