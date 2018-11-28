#include<iostream>
#include<fstream>
#include<cstdio>
#include<stdlib.h>
using namespace std;


int main(){
	int test;
	cin>>test;
	for(int i = 1; i <= test; i++){
		int s_max, s, friends = 0;
		cin>>s_max;
		char* p;
		//cout<<p;
		cin>>p;
		int curr_standing = p[0] - '0';
		for(int j = 1; j <= s_max; j++){
			int s = p[j] - '0';
			if(j <= curr_standing && s != 0){
				curr_standing += s;
			}
			else if(s != 0){
				friends += abs(curr_standing - j); 
				curr_standing += friends + s;
			}
			if(curr_standing >= s_max)
				break;
		}
		cout<<"Case #"<<i<<": "<<friends<<endl;
		
	}
	
}
