#include<iostream>
#include<cmath>
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rep(i,a) loop(i,0,a)
using namespace std;

int main(){
	long long n,t,temp;
	cin>>n;
	rep(p,n){
		cin>>t;
		long long cnt;
		bool dt[10],check=false;
		rep(i,10)dt[i]=false;
		for(int i=1;i<=10000;i++){
			temp=t*i;
			while(1){
				dt[temp%10]=true;
				if(temp<10)break;
				temp/=10;
			}
			long long alt=0;
			rep(j,10)if(dt[j])alt++;
			if(alt==10){
				check=true;
				cnt=i;
				break;
			}
		}
		if(check)cout<<"Case #"<<p+1<<": "<<t*cnt<<endl;
		else cout<<"Case #"<<p+1<<": INSOMNIA"<<endl;
	}
	return 0;
}