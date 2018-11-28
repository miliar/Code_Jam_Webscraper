#include <iostream>
#include <cstring>
using namespace std;

int mark[11];
int cnt() {
	int ret = 0;
	for (int i = 0; i < 10; i++) {
		if (mark[i] == 1)
			ret++;
	}
	return ret;
}

int main()
{
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int ans = 0;
    	memset(mark,0,sizeof(mark));
    	int n;
    	cin >> n;
    	if (n == 0) {
    		cout << "Case #" << i<< ": " << "INSOMNIA" << endl;
    		continue;
    	}
    	
    	for (int j = 1; j <= 75; j++) {
    		int num = j*n;
    		while (num > 0) {
                mark[num%10] = 1;
                num /= 10;
            }
    		if (cnt() == 10) {
    			ans = j*n;
    			break;
    		}
    	}
    	cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}