#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int t,a,n;
	cin>>t;
	for(int m=0;m<t;m++){
	cin>>a>>n;	
	int mt[n];
	for(int i=0;i<n;i++) cin>>mt[i];
	sort(mt,mt+n);
	int i,mo,y;
	y=n;
	if(a==1){cout<<"Case #"<<(m+1)<<": "<<n<<"\n";continue;} 
	for(mo=0,i=0;i<n;i++){if(a>mt[i]) a+=mt[i];
			else{while(mt[i]>=a){a=2*a+-1;mo++;}
			a+=mt[i];}
	if(y>mo+n-i-1) y=mo+n-i-1;	
	}
	cout<<"Case #"<<(m+1)<<": "<<y<<"\n";	
	}
	return 0;}	
