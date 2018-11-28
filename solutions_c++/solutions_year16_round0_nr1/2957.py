#include<iostream>
using namespace std;
int main (){
	int x;
	cin>>x;
	int number;
	int array[10]={0};
	int count;
	int times;
	int product;
	for(int i=1;i<=x;i++){
		cin>>number;
		for(int j=0;j<10;j++){
			array[j]=0;
		}
		count=0;
		if(number==0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}else{
			times=1;
			do{
				product=number*times;
				times++;
				
				while(product!=0){
					if(array[product%10]==0){
						count++;
						array[product%10]++;
					}
					product-=(product%10);
					product/=10;
				}
				
				
			}while(count!=10);
			times-=1;
			cout<<"Case #"<<i<<": "<<times*number<<endl;
		}
	}
}
