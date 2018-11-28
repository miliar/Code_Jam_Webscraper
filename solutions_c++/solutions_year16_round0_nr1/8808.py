#include<iostream>
#include<fstream>
#include<cstdlib>
#include<time.h>
using namespace std;

int t,i;

long int n,numb;
int arr[10];
int j = 1;
int sum = 0;

int main(){
	cin>>t;
	int k = t;
	while(k){
		cin>>n;
		for(i = 0;i<10;i++)
			arr[i] = 0;
		j = 1;
		if(n == 0)
			cout<<"Case #"<<t-k+1<<": INSOMNIA"<<endl;
		else{
			while(1){
				long int num = j*n;
				numb = num;
				sum = 0;
				while(numb/10){
					arr[numb%10] = 1;
					numb = numb/10;
				}
				arr[numb%10] = 1;
				for(i = 0;i<10;i++)
					sum += arr[i];
				if(sum == 10){
					cout<<"Case #"<<t-k+1<<": "<<num<<endl;
					break;
				}
				j = j+1;
			}
		}	
		k = k-1;
	}
}
