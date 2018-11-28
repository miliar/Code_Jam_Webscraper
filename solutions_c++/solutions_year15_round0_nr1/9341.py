#include<iostream>
#define M 1003
#define f(i,a,b) for(int i=a;i<b;i++)
using namespace std;
int main(){
	int t,n,m[M],rs,sum;
	char c;
	cin>>t;
	f(i,1,t+1){
		cin>>n;
		rs=0;
		cin>>c;
		sum=m[0]=c-'0';
		
		f(j,1,n+1){
			cin>>c;
			m[j]=c-'0';
			if(sum+rs<j){
				rs+=j-sum-rs;
			}
			sum+=m[j];
		}
		cout<<"Case #"<<i<<": "<<rs<<endl;
	}
	return 0;
}
