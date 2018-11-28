#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>

using namespace std;

int main(){
	int test;
	cin >>test;
	for(int k = 1; k <= test;k++){
		string p;
		cin >> p;
		int count = 0;
		int j = 0;
		while(true){
			int index = 0;
			if(p[0] == '-'){
				for(int i = p.length() - 1;i >= 0;i--){
					if(p[i] == '-'){
						index = i;
						break;
					}
				}
				string temp = "",temp2 = "";
				for(int i = index;i >= 0;i--){
					if(p[i] == '-'){
						temp = temp + '+';
					}
					else
						temp = temp + '-';
				}
				for(int i = index + 1;i < p.length();i++){
					temp2 = temp2 + p[i];
				}
				p = temp + temp2;
				count++;
			}

			//cout << p <<"\n";
			int ct = 0;
			for(int i = 0;i < p.length();i++){
				if(p[i] == '-')
					ct++;
			}
			if(ct == 0)
				break;


			else if(p[0] == '+' && ct != 0){
				for(int i = 0;i < p.length();i++){
					if(p[i] == '+'){
						p[i] = '-';
					}
					else
						break;
				}
				count++;
			}			
			ct = 0;
			for(int i = 0;i < p.length();i++){
				if(p[i] == '-')
					ct++;
			}
			if(ct == 0)
				break;
		}
		cout <<"Case #"<<k<<": "<<count<<"\n";
	}
}