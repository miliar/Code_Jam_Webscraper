#include <iostream>
using namespace std;
int main(){

	int t,tn,r1,r2,a,k,c[4],match,i,j,val;
	tn=0;
	cin>>t;
	while(t--){
		tn++;
		for(i=0;i<4;i++)
			c[i]=0;
		match=0;
		cin>>r1;
		k=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>a;
				if(i==r1-1){
					c[k]=a;
					k++;
				}

			}
		}
		
		cin>>r2;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>a;
				if(i==r2-1){
					for(k=0;k<4;k++){
						if(c[k]==a)
						{
							val = a;
							match++;
						}
					}
				}
			}
		}

		if(match==0)
			cout<<"Case #"<<tn<<": "<<"Volunteer cheated!"<<endl;
		else if(match==1)
			cout<<"Case #"<<tn<<": "<<val<<endl;
		else
			cout<<"Case #"<<tn<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}