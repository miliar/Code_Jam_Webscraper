#include <iostream>
#include <cstring>

using namespace std;

int main() {
	// your code goes here
	long t,tc,j,len,count;
	char str[102];
	cin >> t;
	tc = t;
	while(t--){
	    cin >> str;

	    count = 0;
	    len = strlen(str);
	    for(int i = 0; i < len;){
	        j = i+1;
	        if(str[i] == str[j]){
	            i++;
	        }
	        else if(j<len && str[i] != str[j]){
	            for(int k = 0; k < j; k++){
	                str[k] = str[j];
	            }
	            i = 0;
	            count ++;
	        }
	        else i++;
	    }
	    if(str[0] == '-')
            count++;
	    cout << "Case #"<<tc-t<<": "<<count<<endl;
	}
	return 0;
}
