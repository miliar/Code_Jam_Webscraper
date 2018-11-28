#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

int main() {
	// your code goes here

    freopen("final.in","r",stdin);
    freopen("out_final.in","w",stdout);


	int i,j,k,min1;
	int t;
	int x,r,c;

	cin>>t;
	i=1;
	while(t--){

		cin>>x>>r>>c;

		min1=min(r,c);

		if(x==1){
			cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
			i++;
		}else if(x==2){

			if((r>=2 || c>=2) &&((r*c)%2==0)){
				cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
				//cout<<"GABRIEL"<<endl;
				i++;
			}else{
				//cout<<"RICHARD"<<endl;
				cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
				i++;
			}
		}else if(x==3){
				if((r>=3 || c>=3) && ((r*c)%3==0) && c!=1 && r!=1) {
					//cout<<"GABRIEL"<<endl;
					cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
					i++;
				}else{
					//cout<<"RICHARD"<<endl;
					cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
					i++;
				}
		}else{
			if((r>=4 && c>=4) || (r==4 && c==3) || (r==3 && c==4)){
				//cout<<"GABRIEL"<<endl;
				cout<<"Case #"<<i<<":"<<" GABRIEL"<<endl;
				i++;
			}else{
				//cout<<"RICHARD"<<endl;
				cout<<"Case #"<<i<<":"<<" RICHARD"<<endl;
				i++;
			}

		}

	}

	return 0;
}
