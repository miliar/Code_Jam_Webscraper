#include<bits/stdc++.h>
using namespace std;
int _A[1005];
int main(){
	//freopen("in","r",stdin);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		string tmp;
		int n;
		cin>>tmp;
		cin>>n;
		for(int j=0;j<tmp.size();j++)
			if(tmp[j]=='+')	_A[j+1]=1;
			else			_A[j+1]=0;
		int cnt=0;
		for(int j=1;j+n-1<=tmp.size();j++){
			if(_A[j])	continue;
			for(int k=0;k<n;k++)
				_A[j+k]=!_A[j+k];
			cnt++;
		}
		cout<<"Case #"<<i<<": ";
		bool flag=true;
		for(int j=tmp.size()+1-n;j<=tmp.size();j++)
			if(!_A[j])	flag=false;
		if(flag)	cout<<cnt<<endl;
		else		cout<<"IMPOSSIBLE"<<endl;
		
	}
}
