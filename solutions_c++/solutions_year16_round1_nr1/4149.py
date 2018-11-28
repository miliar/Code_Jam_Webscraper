#include <iostream>
#include <string.h>
using namespace std;

int main() {
	string str, newStr;
	char a, b;
	int length, tempIndex, strLength, newStrIndex, strIndex, index;
	
	cin>>length;
	for(index = 0; index<length; index++){
	    str = "";
	    newStr = "";
	    cin>>str;
	    newStrIndex = 0;
	    strLength = str.length();
	    newStr.insert(newStr.begin(), 1, str[0]);
	    for(strIndex = 1; strIndex < strLength; strIndex++){
	        if(str[strIndex]>=newStr[0]){
	             newStr.insert(newStr.begin(), 1, str[strIndex]);
	        } else {
	            newStr.insert(newStr.end(), 1, str[strIndex]);
	        }
	    }
	    cout<<"Case #"<<index + 1<<": "<<newStr<<"\n";
	    strIndex = 0;
	}
	
	return 0;
}