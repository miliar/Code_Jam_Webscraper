#include <bits/stdc++.h>

using namespace std;

int V[10];
int c;
bool cd(int x){
    string a;
	stringstream ss;
	ss<<x;
	ss>>a;
	for(int i=0;i<a.size();i++){
		int aux=a[i]-'0';
		if(V[aux]==0)c++;
		V[aux]=1;
	}
//	cout<<c<<" - "<<x<<endl;
	return c>=10;
}
int main(){
	int t,n,nn;
	cin>>t;
	int cse=1;
	while(t--){
		cout<<"Case #"<<cse++<<": ";
		cin>>n;
		if(n==0){
			cout<<"INSOMNIA\n";
			continue;
		}
		nn=n;
		c=0;
		for(int i=0;i<10;i++)V[i]=0;
		while(!cd(nn)){
			nn+=n;
		}
		cout<<nn<<"\n";
	}
	return 0;
}
