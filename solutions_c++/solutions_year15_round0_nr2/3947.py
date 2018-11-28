#include <iostream>
#include <string>
using namespace std;
int main(){
	freopen("out.txt","w",stdout);
	int p[1010];
	int t;
	cin>>t;
	for(int c=1;c<=t;c++){
		int d;
		cin>>d;
		for(int i=0;i<d;i++)
			cin>>p[i];

		int mx=0;
		for(int i=0;i<d;i++)
			if(p[i]>mx)mx=p[i];
		
		int r=1e9;
		for(int i=1;i<=mx;i++){
			int res=0;
			for(int j=0;j<d;j++)
				res+=(p[j]-1)/i;
			if(r>res+i)r=res+i;
		}
		cout<<"Case #"<<c<<": "<<r<<endl;
	}
	return 0;
}
