#include <iostream>
using namespace std;

bool allDigits(bool v[]) {
	for(int i = 0; i<10; i++)
		if(v[i] == false)
			return true;
	return false;
}

int main() {
	bool v[10] = {false, false, false, false, false, false, false, false, false, false};
	long n, r, mlt, i;
	int cases;
	cin >> cases;
	for(int a = 0; a < cases; a ++) {
	    cin >> n;
	    mlt = n;
	    i=0;
	    for(int j=0; j<10; j++) v[j] = false;
	    if(n != 0) {
	    	do {
		    	i += 1;
		    	n = mlt*i;
		    	while(n!=0) {
				   r = n%10; n = n/10;
				   v[r] = true;
			    }

		    } while(allDigits(v));
		    cout << "Case #" << a+1 << ": " << mlt*i << endl;
	    }
	    else {
	    	cout << "Case #" << a+1 << ": " << "INSOMNIA"<<endl;
	    }
	    
    }
    return 0;
}
