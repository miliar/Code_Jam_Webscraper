#include <iostream>
using namespace std;


int main(){

	int T;
	cin>>T;
	int caseno = 1;
	while(T--){
		int Smax;
		cin>>Smax;
		string str;
		cin>>str;

		int *array = new int[Smax+1];
		char a;
		int ia;
		for(int i = 0; i < Smax+1; ++i){
			a = str[i];
			ia = a - '0';
			array[i] = ia;
		}

		
		int more = 0, got = 0;

		for(int i = 0; i < Smax+1; ++i){
			if(got < i){
				more += i-got;
				got += i-got;
			}
			got += array[i];
		}

		cout<<"Case #"<<caseno<<":"<<" "<<more<<endl;
		caseno++;

	}
}