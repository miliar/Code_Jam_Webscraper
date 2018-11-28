#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define p push
#define ms memset
#define maxn 100001
using namespace std;
set<int>x;
void num(ll int k){
	while(k!=0){
		//if(k%10!=0)
			x.insert(k%10);
		k/=10;
	}

}
int main(){	
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	ll int y,temp;
	for(int i=1;i<=t;i++){
		x.clear();
		cin>>y;
		if(y==0)
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<"\n";
		else{
			int counter=0;	
			while(x.size()!=10){
				counter++;
				temp=y*counter;
				num(temp);
			}
			cout<<"Case #"<<i<<": "<<temp<<"\n";
		}
	}	
}