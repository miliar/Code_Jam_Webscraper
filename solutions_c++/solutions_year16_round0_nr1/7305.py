#include <iostream>
using namespace std;
int main(){
	int c,n,ll=1;
	cin>>n;
while(n--){
cin>>c;
	int t=0,r,k=0,s,aaa=0;
	int a[]={0,0,0,0,0,0,0,0,0,0};
	while(1){
		if(c==0){
			cout<<"Case #"<<ll<<": INSOMNIA"<<endl;
			break;
		}
		int ct=0;
		for(int m=0;m<10;m++){
			if(a[m]==1){
				ct++;
			}
		}
		if(ct==10){
			break;
		}
		r=c*k;
		 aaa=r;
		while(r>0){
			s=r%10;
			if(a[s]==0){
				a[s]=1;
			t++;
			}
			r=r/10;
		}
		k++;
	}
	int ct=0;
		for(int m=0;m<10;m++){
			if(a[m]==1){
				ct++;
			}
		}
		if(ct==10)
			cout<<"Case #"<<ll<<": "<<aaa<<endl;
   ll++;
   }
}

