#include <iostream>  
#include <sstream>
using namespace std; 

bool all_good(bool d[10]){
    return d[0] 
	&&d[1]
	&&d[2]
	&&d[3]
	&&d[4]
	&&d[5]
	&&d[6]
	&&d[7]
	&&d[8]
	&&d[9];
}

int main() {
    int t, n;
    cin >> t;
    string output = "INSOMNIA";
    for (int i = 1; i <= t; ++i) {
	cin >> n;
	bool digits[10] = {false};
	for(int j=1; j<=1000; ++j) {
	    ostringstream oss;
	    oss << j*n;
	    for(auto c:oss.str()) {
		int d= c - '0';
		if(0<=d && d<=9) {
		    digits[d] = true;
		}
	    }
	    if(all_good(digits)) {
		output = oss.str();
		break;
	    } 
	}
	cout << "Case #" << i << ": " <<output<<endl;
    }
    return 0;
}
