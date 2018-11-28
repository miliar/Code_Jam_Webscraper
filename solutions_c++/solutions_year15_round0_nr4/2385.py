#include<iostream>
using namespace std;

int main(){
	int T,n=0,X,R,C;
	char Ga[]="GABRIEL",Ri[]="RICHARD";
	cin>>T;
	while(n<T){
		cin>>X>>R>>C;
		cout<<"Case #"<<n+1<<":"<<" ";
		switch(X){
			case 1:	
					cout<<Ga;
					break;
			case 2:
					if((R*C)%2==0)	cout<<Ga;
					else	cout<<Ri;
					break;
			case 3:
					if(R*C==3 || (R*C)%3!=0)	cout<<Ri;
					else	cout<<Ga;
					break;
			case 4:
					if(R*C >= 12)	cout<<Ga;		// 3x4 or 4x4  : exploiting R,C <= 4
					else	cout<<Ri;
					break;
			}
		cout<<endl;
		n++;
	}
	return 0;
}