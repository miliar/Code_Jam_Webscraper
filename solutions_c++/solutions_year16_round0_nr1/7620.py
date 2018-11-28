#include<iostream>
using namespace std;

int all_digits(int digits[]){
	for(int i=0;i<10;i++){
		if(digits[i]<=0)
			return 0;
	}
	return 1;
}

int sheep_sleep(int N){
int digits[10];
for(int i=0;i<10;i++){
digits[i]=0;
}
if(N<=0)
return -1;
int NN=N;
int j=2;
while(1){
int temp=NN;
while(temp>0){
digits[temp%10]++;
temp=temp/10;
}
if(all_digits(digits))
	return NN;
else{
	NN=N*j;
	
}
j++;
}
return -1;
}


int main(){
int T;
cin>>T;
for(int i=0;i<T;i++){
	int N;
	cin>>N;
	int last_num=sheep_sleep(N);
	if(last_num==-1)
		cout<<"Case #"<<i+1<<":"<<" INSOMNIA"<<endl;
	else
		cout<<"Case #"<<i+1<<": "<<last_num<<endl;

}

}
