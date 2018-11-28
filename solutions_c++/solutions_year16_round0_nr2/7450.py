#include <iostream>
#include <string>


using namespace std;


int main(){

//cout<<"Hello"<<endl;
int num;

cin>>num;
//cout<<"Num: "<<num<<endl;

for(int i = 0; i < num; i++){
	string input;
	cin>>input;
	//cout<<input<<endl;	
	int switchNum = 0;
	char prev = input[0];
	for (int k = 1; k < input.size(); k++){
 	   //cout << input[k]<<endl;
	   if(prev != input[k]){
		switchNum++;
		prev=input[k];
	   }
	}
	if(input[input.length()-1] == '-'){
		switchNum++;
	}
	//cout<<switchNum<<"------"<<endl;
	cout<<"Case #"<<i+1<<": "<<switchNum<<endl;
}

return 0;
}
