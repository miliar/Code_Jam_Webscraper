#include <iostream>
#include <cstring>
using namespace std;

int m[256];
char s[2002];
bool canform(char *l) {
	int len = strlen(l);
	int d = 0;
	bool ok = true;
	for (int i = 0; i < len; i++) {
		if (!m[l[i]]) {
			// cout<<l[i]<<")";
			ok = false;
			break;
		}
		--m[l[i]];
		++d;
	}

	if (!ok) {
		for (int i = 0; i < d; i++) {
			++m[l[i]];
		}
		return false;
	}
	// cout<<"*";
	return true;
}
void getback(char *l) {
	int i = 0;
	while(l[i]) {
		++m[l[i]];
		++i;
	}
}
char arr[][100] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int total;
int nums[2000];
int numsc = 0;
int c = 0;
bool work(int ii) {
	// cout<<ii<<" "<<numsc<<" "<<total<<endl;
	if (numsc == total) return true;
	if (numsc > total) return false;
    for (int i = ii; i < 10; i++) {
    	int len = strlen(arr[i]);
    	// cout<<"["<<i<<"]";
    	if (canform(arr[i])) {
    		// cout<<" ";
    		numsc+=len;
    		nums[c] = i;
    		++c;
    		if (work(i)) {
    			return true;
    		}
    		--c;
    		numsc-=len;
    		getback(arr[i]);
    		// cout<<"<"<<endl;
    	}
    }
    return false;
}

int main() {
    int T;
    
    
    cin>>T;
    for (int ti = 1; ti <= T; ti++) {
        cout<<"Case #"<<ti<<": ";
        cin>>s;
        memset(m, 0, 256*sizeof(int));
        int len = strlen(s);
        total = len;
        for (int i = 0; i < len; i++) {
        	++m[s[i]];
        }
        for (int i = 0; i < len; i++) {
        	// cout<<s[i]<<m[s[i]]<<" ";
        }
        // for (int i = 0; i < 10; i++) {
        // 	while(canform(arr[i])) {
        // 		cout<<i;
        // 	}
        // }
        numsc = 0;
        c = 0;
        work(0);
        for (int i = 0; i < c; i++) {
        	cout<<nums[i];
        }
        // for (int i = 0; i < 10; i++) {
        // 	if (canform(arr[i])) {
        // 		cout<<i;
        // 		--i;
        // 	}
        // }
        cout<<endl;
    }
    return 0;
}
