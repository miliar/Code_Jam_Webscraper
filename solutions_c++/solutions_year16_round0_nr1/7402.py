#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;


int main(int argc, char** argv) {
	int t,count=1,j,input,temp,arr[10];
	cin>>t;
	while(count<=t) {
		for(int i=0;i<10;i++){
			arr[i]=0;
		}
		cin>>input;
		cout<<"Case #"<<count<<": ";
		count++;
		if(input==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		for(int i=1;i<1000;i++){
			temp=input*i;
			while(temp){
				arr[temp%10]++;
				temp=temp/10;
			}
			for(j=0;j<10;j++){
				if(arr[j]==0){
					break;
				}
			}
			if(j==10){
				cout<<input*i<<endl;
				//cout<<i<<endl;
				break;
			}
		}
	}
	return 0;
}
