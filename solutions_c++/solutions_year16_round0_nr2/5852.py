#include <iostream>
#include <string>

using namespace std;


int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
	string seq;
	cin >> seq;
	char where[] = "+-";
	int res = 0;
	for(int j = seq.length()-1, k=0; j>=0;){ 
	    while(j>=0 && where[k] == seq[j]) j--;
	    if(j<0) break;
	    res++; k = (k+1)%2;
	}
	cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}

