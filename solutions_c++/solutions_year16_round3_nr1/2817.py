#include<iostream>
using namespace std;

class data{
	public:
		int num;
		char party;
};

char partName(int i){
	char ch;
	switch(i){
		case 1: 
				ch='A';
				break;
		case 2: 
				ch='B';
				break;
		case 3: 
				ch='C';
				break;
	}
	return ch;
}

void sort(data *dataset,int n){
	for(int i=n;i>=1;i--){
		for(int j=1;j<=i;j++){
			if(dataset[j].num < dataset[j+1].num){
				int temp;
				temp=dataset[j].num;
				dataset[j].num=dataset[j+1].num;
				dataset[j+1].num=temp;
				char ch;
				ch=dataset[j].party;
				dataset[j].party=dataset[j+1].party;
				dataset[j+1].party=ch;
			}
		}
	}
}
int main(){
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		int n;
		data dataset[50];
		for(int i=1;i<=50;i++){
			dataset[i].num=0;
			dataset[i].party='1';
		}
		cin>>n;
		for(int i=1;i<=n;i++){
			dataset[i].party=partName(i);
			cin>>dataset[i].num;
		}
		cout<<"Case #"<<t<<": ";
		sort(dataset,n);
		while(dataset[1].num!=0){
			if(dataset[1].num==dataset[2].num && dataset[1].num >1){
				cout<<dataset[1].party<<dataset[2].party<<" ";
				dataset[1].num--;
				dataset[2].num--;
			}
			else if(dataset[1].num==1 && dataset[2].num==0){
				cout<<dataset[1].party<<" ";
				dataset[1].num--;
			}
			else if(dataset[1].num==1 && dataset[2].num==1 && dataset[3].num==1){
				cout<<dataset[1].party<<" ";
				dataset[1].num--;
			}
			else if(dataset[1].num==1 && dataset[2].num==1 && dataset[3].num==0){
				cout<<dataset[1].party<<dataset[2].party<<" ";
				dataset[1].num--;
				dataset[2].num--;
			}
			else if(dataset[1].num==1 && dataset[2].num==0 && dataset[3].num==0){
				cout<<dataset[1].party<<" ";
				dataset[1].num--;
			}
			else if(dataset[1].num > dataset[2].num){
				cout<<dataset[1].party<<dataset[1].party<<" ";
				dataset[1].num--;
				dataset[1].num--;
			}
			sort(dataset,n);
		}
		cout<<endl;	
	}
	return 0;
}
