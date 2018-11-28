#include <iostream>
#include <cmath>
using namespace std;
int c[20];
int m[10][10];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;++k){
		int a,b,n=0,q=0;
		cin>>a;
		for(int i=1;i<=4;++i){
			for(int j=1;j<=4;++j){
				cin>>m[i][j];
			}
		}
		for(int j=1;j<=4;++j){
			++c[m[a][j]];
		}
		cin>>b;
		for(int i=1;i<=4;++i){
			for(int j=1;j<=4;++j){
				cin>>m[i][j];
			}
		}
		for(int j=1;j<=4;++j){
			++c[m[b][j]];
		}
		for(int i=1;i<=16;++i){
			if(c[i]==2){
				++q;
				n=i;
			}
			c[i]=0;
		}
		if(q==1){
			cout<<"Case #"<<k<<": "<<n<<endl;
		}else if(q>1){
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		}else{
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}