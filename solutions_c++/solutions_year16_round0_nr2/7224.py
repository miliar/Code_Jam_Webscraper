#include <iostream>
#include <string>

using namespace std;

int main(){
	string str;
	int num,count;
	char pre;
	cin >> num;
	for(int i = 1 ; i <= num ; i++){
		cin >> str;
		pre = str.at(str.length()-1);
		if(pre == '+')
			count = 0;
		else
			count = 1;
		for(int j = str.length()-2 ; j >= 0 ; j--){
			if(str.at(j) != pre) 
				count++;
			pre = str.at(j);
		}

		cout  << "Case #" << i << ": " << count << endl;
	}


	return 0;
}