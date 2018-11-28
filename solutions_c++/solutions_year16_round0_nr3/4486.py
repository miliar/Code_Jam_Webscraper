#include<bits/stdc++.h>
using namespace std;
double pwr(int x,int y);
double Isprime(double sum);
int main(){
	freopen("a.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	int  n,j;
	int k=0;
	cin>>n>>j;
	int a[n]={0};
	a[0]=1;
	a[n-1]=1;
	double sum=0,b[12]={0};
	cout<<"Case #1:"<<endl;
	while(j){
		/*cout<<endl<<k<<endl;
		for(int p=0;p<n;p++)
				cout<<" a["<<p<<"]="<<a[p]<<" ";
			cout<<endl;*/
		int count=0;
		for(int l=2;l<11;l++){
			sum=0;
			for(int i=0;i<n;i++){
				if(a[n-i-1]==1){
					sum+=pow(l,i);
				}
			}
			int flag;
			flag=Isprime(sum);
			if(flag!=0){
				b[l]=flag;
				count++;	
			}
			if(flag==0){
				count=0;
				break;
			}
		}
		if(count==9){
			j--;
			for(int g=0;g<n;g++)
				cout<<a[g];
			cout<<" ";
			for(int g=2;g<11;g++){
				cout<<b[g]<<" ";
			}
			cout<<endl;
		}
		int carry=1;
		for(int i=n-2;i>=1;i--){
			if(a[i]==1&&carry==1){
				carry=1;
				a[i]=0;
			}
			else if(carry==1){
				carry=0;
				a[i]=1;
			}
		}			
	}
}
/*double pwr(int x,int y){
	double mul=1;
	for(int i=0;i<y;i++){
		mul=mul*x;
	}
	return mul;
}*/
double Isprime(double sum){
	double i,d=sqrt(sum);
	if(remainder(sum,2)==0)
		return 2;
	for(i=3;i<=d;i=i+2){
		if(remainder(sum,i)==0)
		return i;
	}
	return 0;
}
