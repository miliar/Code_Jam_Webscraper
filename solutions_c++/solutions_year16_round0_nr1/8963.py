#include<iostream>
//#include<conio.h>
using namespace std;

int main(){
	int t,t1=1,a[10],count=0,d;
	long n,i,n1,j;
	cin>>t;
	while(t1<=t){
		cin>>n;
		n1=n;
		for(j=0;j<10;j++)
			a[j]=0;
		if(n==0){
		 cout<<"Case #"<<t1<<": INSOMNIA\n";
		}	
		else{
		for(count=0,i=1;count!=10;i++){
			n1=n*i;
			for(j=0;n1!=0;j++){
				d=n1%10;
				if(a[d]==0){
					count++;
					a[d]=1;
				}
				n1=n1/10;
			}
		}
		cout<<"Case #"<<t1<<": "<<n*(i-1)<<endl;
		}
		t1++;
	}
//	getch();
	return 0;
}
