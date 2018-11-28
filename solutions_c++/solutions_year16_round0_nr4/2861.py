#include <bits/stdc++.h>
using namespace std;

int main(){
	// freopen("inputp4.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	long long t,k,cc,s,i,j,c,K;
	long long pos;
	long long finalPos[105];
	cin>>t;
	for(long long cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": ";
		cin>>k>>c>>s;

		if(c==1){
			if(s>=k)
			{
				for(i=1;i<=k;i++)
					cout<<i<<" ";
				cout<<endl;
			}
			else
				cout<<"IMPOSSIBLE"<<endl;
			continue;
		}

		K=k;
		for(i=1;i<=k;i++){
			pos = i;
			for(j=2;j<=c;j++){
				pos = (pos-1)*k + i;
			}
			finalPos[i]=pos;
		}

		bool isEven = k%2 == 0;
		if(isEven) k=k/2;
		else k = k/2 +1;
		if(s>=k){
			for(i=1;i<=k;i++,K--){
				cout<<finalPos[i]-i+K<<" ";
			}
			cout<<endl;
		}
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}