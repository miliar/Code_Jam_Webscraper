#include <iostream>
using namespace std;
int a[10];
int func(int num){
	int count =0;
	 //= new int [](10);
	for(int i=0;i<10;i++)
		a[i]=0;
	for(int num1=num;;num1+=num){
		count++;
		if(count>1000)
			return -1;
		int num2=num1;
		while(num2!=0){
			a[num2%10]++;
			num2/=10;
		}
		int c=0;
		for(;c<10;c++)
			if(a[c]==0)
				break;
		if(c==10)
			return num1;
	}	
}

int main() {
	// your code goes here
	int t,num;
	cin>>t;
	for(int w=1;w<=t;w++){
		cin>>num;
		if(num==0)
			cout<<"Case #"<<w<<": "<<"INSOMNIA"<<endl;
		else{
			int res= func(num);
			if(res==-1)
				cout<<"Case #"<<w<<": "<<"INSOMNIA"<<endl;
			else
				cout<<"Case #"<<w<<": "<<res<<endl;
			}
			
	}
	return 0;
}

