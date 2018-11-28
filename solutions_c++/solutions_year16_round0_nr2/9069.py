#include<iostream>
//#include<conio.h>

using namespace std;
void swap(char a[],int i){
	int j,temp;
	for(j=0;j<=i/2;j++){
		temp=a[i-j];
		a[i-j]=a[j];
		a[j]=temp;
		if(a[j]=='+')
		 a[j]='-';
		else
		 a[j]='+'; 
		if(i-j != j){
			if(a[i-j]=='+')
			 a[i-j]='-';
			else
			 a[i-j]='+'; 
		} 
	}
}
int main(){
	char a[105];
	int t,t1=1,i,j,l,count;
	cin>>t;
	while(t1<=t){
		cin>>a;
		for(l=0;a[l]!='\0';l++);
		for(i=0,count=0;i<l;i++){
			for(j=0;a[j]==a[j+1] && j<l-1;j++);
			if(j==l-1)
				if(a[0]=='+')
					break;
				else{
					++count;break;
				}	
			swap(a,j);count++;
		}
		cout<<"Case #"<<t1<<": "<<count<<endl;t1++;
	}
//	getch();
	return 0;
}
