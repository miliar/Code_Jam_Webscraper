#include<iostream>
#include<iomanip>
#include<sstream>

using namespace std;

void count_sheep(int i, int* a, int counter){

	if(i==0){
		cout<<"INSOMNIA"<<endl;
		return;
	}

	bool finish=true;
	int num = i*counter;

	ostringstream convert;   // stream used for the conversion

	convert << num;      // insert the textual representation of 'Number' in the characters in the stream

	string s = convert.str();

    for(int j=0; j<s.length(); ++j){
    	char c=s[j];
    	int offset=c-'0';

    	a[offset]=1;
    }

	for(int m=0; m<10; ++m){
		if( a [m]==0 ){
			finish=false;
		}
	}

	if(finish==false){
		count_sheep(i, a, counter+1);
	}else{
		cout<<num<<endl;
		return;
	}

}


int main(){
	int total;
	cin>>total;

	int a[10];


	int test;

	for(int j=0; j<total; ++j){
		for(int i=0; i<10; ++i){
				a[i]=0;
			}

		cin>>test;
		count_sheep(test, a, 1);
	}

}
