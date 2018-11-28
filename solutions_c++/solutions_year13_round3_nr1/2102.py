/*
 * jam1.cpp
 *
 *  Created on: 2013-5-12
 *      Author: york
 */


#include<iostream>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

bool isO(char a){
	if(a == 'a' || a == 'e' || a == 'i' || a=='o' || a=='u' ){
		return true;
	}
	return false;
}

int main(){
	std::ofstream ofs;
	ofs.open("out.txt");
	int T,n,pre,count,cur,i,sum;
	string tmp;
	cin >> T;
	for(int st=0;st<T;++st){
		cin >> tmp;
		cin >> n;
		cur = 0;
		pre = 0;
		sum = 0;
		while(cur < tmp.length()){
			count = 0;
			for(i = pre;i < tmp.length();++i){
					if(!isO(tmp[i])){
						count++;
						if(count == n){
							++i;
							break;
						}
					}
					else{
						count = 0;
					}
			}
			if(count < n){
				break;
			}
			else{
				sum += (i-pre + 1 - n) *( tmp.length() - i+1);  //maybe
				pre = i - n + 1;
				cur = i;
			}

		}
		ofs << "Case #" << st+1 <<": "  << sum << '\n';
	}

	ofs.close();
	return 0;
}



