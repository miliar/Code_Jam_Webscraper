#include <iostream>
using namespace std;
int main(){
	int t,te,i,j,k,n,m,a1[4],a2[4];
	cin>>t;
	for(te=0;te<t;te++){
		cout<<"Case #"<<te+1<<": ";	
		cin>>n;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>k;
				if(i==n-1)a1[j]=k;
			}
		}
		cin>>m;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>k;
				if(i==m-1)a2[j]=k;
			}
		}
		for(i=0,k=0;i<4;i++){
			for(j=0;j<4&&a2[j]!=a1[i];j++);
			if(j<4){
				if(k==0)n=a1[i];
				k++;
			}
		}
		if(k>1)cout<<"Bad magician!\n";
		else if(k==0)cout<<"Volunteer cheated!\n";
		else cout<<n<<"\n";
	}
	return 0;
}