#include<iostream>
#include<iomanip>
#include<sstream>

using namespace std;

void flip(string* s,  int case_n, int counter){
	bool finish=true;
	string temp=*s;

	for(int i=0; i<temp.length(); ++i){
		if(temp[i]=='-'){
			finish=false;
		}
	}

	if(finish==true){
		cout<<"Case #"<<case_n<<": "<<counter<<endl;
		return;
	}else{
		int loc1=0;
		int loc2=0;


		for(int i=0; i<temp.length(); ++i){
			if(temp[i]=='-'){
				loc1=i;
				break;
			}
		}

		for(int i=loc1; i<temp.length(); ++i){
					if(temp[i]=='+'){
						loc2=i;
						break;
					}
				}

		if(loc2==0){

			for(int i=0; i<temp.length(); ++i){
				if(temp[i]=='-'){
								temp[i]='+';
							}else{
								temp[i]='-';
							}
			}

		}else{

		for(int i=0; i<loc2; ++i){
			if(temp[i]=='-'){
				temp[i]='+';
			}else{
				temp[i]='-';
			}
		}
		}

		*s=temp;

		flip(s, case_n, 1+counter);
	}

}


int main(){
	int total;
	cin>>total;


	string pancake;
	int case_num=1;
	getline(cin,pancake);

	for(int j=0; j<total; ++j){

//		cin>>pancake;
		getline(cin,pancake);
		flip(&pancake, case_num, 0);

		++case_num;
	}

}
