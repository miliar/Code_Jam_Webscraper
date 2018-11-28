#include <bits/stdc++.h>
#define maximo 1002

using namespace std;


int main(){	
	
int x,smaximo,i,k,res,soma,a[maximo];
char s[maximo];
scanf("%d",&x);
	k=1;
	while(k<=x){
		cin>>smaximo>>s;
		res=0;
		soma=0;
		for(i=0;i<=smaximo;i++){
			if(soma>=i)
			soma+=(s[i]-'0');
			else{
			res+=(i-soma);
			soma+=(s[i]-'0')+(i-soma);
			}
		}
		a[k]=res;
	k++;
	}
	for(k=1;k<=x;k++){
	   	cout<<"Case #"<<k<<": "<<a[k]<<endl;
	}
return 0;
}