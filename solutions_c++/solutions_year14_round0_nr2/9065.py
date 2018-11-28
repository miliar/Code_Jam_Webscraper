#include<iostream>
using namespace std;
long double recidual(long double t,long double r,int i){
	long double ans=t/((r*i)+2);
	return ans;	
	}
long double buy(long double c,long double r,int i){
	long double ans=c/((r*i)+2);
	return ans;
	}
int main(){
cout.precision(15);
int nc;
cin>>nc;
for(int i=0;i<nc;i++){
	long double c,t,r;
	cin>>c>>r>>t;
	int flag=0,k=0;
	while(flag==0){
		if(recidual(t,r,k+1)+buy(c,r,k)<recidual(t,r,k)){
			k++;
			}
		else{
			flag=1;
			}
		}
	long double ans=0;
	for(int l=0; l<k;l++){
		ans+=buy(c,r,l);
		}
	ans+=recidual(t,r,k);
	cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

}
