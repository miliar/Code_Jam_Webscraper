#include <iostream>
#include <string>


using namespace std;


int main(){

//cout<<"Hello"<<endl;
int num;

cin>>num;
//cout<<"Num: "<<num<<endl;

for(int i = 0; i < num; i++){
	int input;
	cin>>input;
	if(input != 0){
	//cout<<"-----"<<input<<endl;
	int numsFound[] = {0,0,0,0,0,0,0,0,0,0};
	bool foundAll = false;
	int currentNum = 0;
	while(!foundAll){
		currentNum+=input;
		//cout<<"Testing for "<<currentNum<<endl;
		int tempCurrentNum = currentNum;
		while(tempCurrentNum > 0){
			//cout<<tempCurrentNum%10<<endl;;
			numsFound[tempCurrentNum%10] = 1;
			tempCurrentNum/=10;
		}
		foundAll = true;	
		for(int k = 0; k < 10; k++){
			if(!numsFound[k]){
				foundAll = false;
				break;				
			}
		}
	}
	cout<<"Case #"<<i+1<<": "<<currentNum<<endl;
	//cout<<"-----------"<<endl;
	} else {
		cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
	}
}

return 0;
}
