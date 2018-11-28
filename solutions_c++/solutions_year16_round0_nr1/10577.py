#include <iostream>
using namespace std;
int main(){
	int t;cin>>t;
	for(int z=0;z<t;z++){
		
		int n;cin>>n;
		if(n==0)cout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
		else{
		
		int m=0;int a[10]={0};int x=2;int k=n;
		while(m!=10){m=0;
			
			while(k!=0){
				a[k%10]=1;
				k/=10;
			}
			for(int i=0;i<10;i++){
				m+=a[i];
			}
			k=n*x;x++;
		//	cout <<m<<"	"<<n<<'	'<<k<<"	"<<x<<endl;
		}
		int ans=n*(x-2);int q=z+1;
		cout<<"Case #"<<q<<": "<<ans<<endl;
			
		}
		
	}
}
