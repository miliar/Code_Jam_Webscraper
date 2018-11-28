#include<bits/stdc++.h>
using namespace std;

#define LL long long int
#define ULL unsigned long long int
#define MP make_pair
#define PB push_back
#define LD long double
#define MOD 1000000007

void input(){
	freopen("D-small-attempt0.in","r",stdin);
   	freopen("D-small-attempt0.out","w",stdout);
}





int main(){
input();
LL ts=1,t,K,C,S,U[105],x,i;
cin>>t;
while(t--){
	

	cin>>K>>C>>S;
	cout<<"Case #"<<ts<<": ";ts++;
	x=pow(K,C-1);
	if(C==1){
		for(i=1;i<=K;i++){
			cout<<i<<" ";
		}
		cout<<endl;
		continue;
	}
	for(i=1;i<=K;i++) U[i]=x*i;
	cout<<"1 ";
	x=2;
	for(i=1;i<K;i++){
		cout<<U[i]+x<<" ";
		x++;
	}

	cout<<endl;
}

	











return 0;
}
