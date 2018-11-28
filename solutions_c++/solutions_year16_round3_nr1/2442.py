#include<iostream>
//#include<conio.h>
using namespace std;

int max(int p[],int n,int j=-1){
	int pos = -1,max=-1;
	for(int i=0;i<n;i++){
		if(i==j)
			continue;
		if(p[i]>max){
			max = p[i];
			pos=i;
		}	
	}
	return pos;
}

int sum(int p[],int n){
	int sum=0;
	for(int i=0;i<n;i++){
		sum=sum+p[i];
	}
	return sum;
}

int main(){
	int i,j,t1=1,t,n,max1p,max2p;
	freopen("senate.in","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>t;
	while(t1<=t){
		cin>>n;max1p=-1;max2p=-1;
		int p[27];
		for(i=0;i<n;i++){
			cin>>p[i];
		}
		cout<<"Case #"<<t1++<<": ";
		int Sum=sum(p,n);
		while(Sum!=0){
			max1p=max(p,n);
			max2p=max(p,n,max1p);
			if(p[max1p]!=p[max2p]){	
				cout<<char(max1p+65)<<" ";p[max1p]--;
			}		
			else if(p[max1p]==p[max2p] && p[max1p]==1){
				if(Sum==2){
					cout<<char(max1p+65)<<char(max2p+65)<<" ";
					p[max1p]--;p[max2p]--;
				}
				else{
					cout<<char(max1p+65)<<" ";p[max1p]--;
				}
			}	
			else{
				cout<<char(max1p+65)<<char(max2p+65)<<" ";
				p[max1p]--;p[max2p]--;
			}
			Sum=sum(p,n);
		}
		cout<<endl;	
	}
	//	getch();
	return 0;
}
