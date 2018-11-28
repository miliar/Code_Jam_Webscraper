#include <iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i= 1;i<=t;i++){
		int a;
		cin>>a;
		int num1[4]={0,0,0,0};
		int num2[4]={0,0,0,0};
		int z,x,c,v;
		for(int m = 0; m<4;m++){
			cin>>z>>x>>c>>v;
			if((m+1)==a)
			{
				num1[0]=z;
				num1[1]=x;
				num1[2]=c;
				num1[3]=v;
			}
		}
		int b;
		cin>>b;
		for(int m=0;m<4;m++)
		{
			cin>>z>>x>>c>>v;
			if((m+1)==b){
				num2[0]=z;
				num2[1]=x;
				num2[2]=c;
				num2[3]=v;
			}
		}
		int num =0;
		int out;
		for(int q=0;q<4;q++)
		{
			for(int w =0;w<4;w++){
				if(num1[q] == num2[w]){
					out = num1[q];
					num++;
				}
			}
		}
		if(num==1){
			cout<<"Case #"<<i<<": "<<out<<endl;
		}
		else if(num==0){
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
	}
	return 0;
}  
