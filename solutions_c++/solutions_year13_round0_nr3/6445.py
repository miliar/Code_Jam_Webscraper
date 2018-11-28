#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>

using namespace std;


bool checkpanda(int a){
	stringstream ss;
	ss << a;
	string str = ss.str(); 
	bool ispan = true;	

	for(int i = 0; i < str.length();i++){
		if(str.length()%2 && i == str.length()/2)
			break;
		if(str[i] != str[str.length()-1-i]){
			ispan = false;
			break; 
		}
	}
	
	return ispan;
}

int main(){

	int ncase,pancnt;
	int stn,enn;

	cin >> ncase;
	for(int i = 0;i < ncase;i++){
		pancnt = 0;
		cin >> stn >> enn;
		//scanf("%lld" , &stn);
		//scanf("%lld", &enn);
		int k = 1;
	
		while(k*k < stn){
			k++;	
		}

		for(int j = k;j*j <= enn;j++){
			if(checkpanda(j*j)){
				//cout << "-> " << j << endl; 
				if(checkpanda(j))
					pancnt++;
			}
		}

		cout << "Case #" << i+1 << ": " << pancnt << endl;
						
	}	
	
	return 0;
}
