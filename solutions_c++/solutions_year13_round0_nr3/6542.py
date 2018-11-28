#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
	
	int t,i,j,k;
	int a,b;
	cin >> t;
	int count=0;
	for(j=1;j<=t;j++){
		count=0;
		cin >> a;
		cin >> b;
		if(a<=1 && 1<=b){
			count++;
		}
		if(a<=4 && 4<=b){
			count++;
		}
		if(a<=9 && 9<=b){
			count++;
		}
		if(a<=121 && 121<=b){
			count++;
		}
		if(a<=484 && 484<=b){
			count++;
		}
		cout<<"Case #"<< j<<":"<<" " <<count<<endl;
		
	}
	
}

