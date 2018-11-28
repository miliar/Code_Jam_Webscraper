#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[20];

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    cin >> t;
    int cas = 1;
    while(t--) {
	int ra,rb;
	memset(a,0,sizeof(a));
	cin >> ra;
	for(int i = 1 ; i <= 4 ; i++) {
	    for(int j = 1; j<= 4 ; j++) {
		int temp;
		cin >> temp;
		if(i == ra) {
		    a[temp] ++;
		}
	    }
	}
	cin >> rb;
	for(int i = 1 ; i <= 4 ; i++) {
	    for(int j = 1; j <= 4 ; j++) {
		int temp;
		cin >> temp;
		if( i == rb ) {
		    a[temp]++;
		}
	    }
	}

	int ans = 0;
	int val = -1;
	for(int i = 1 ; i <= 16 ; i++) {
	    if(a[i] == 2) ans ++,val = i;
	}

	cout << "Case #"<<cas++<<": ";

	if(ans == 1) {
	    cout << val << endl;
	} else if(ans > 1) {
	    cout <<"Bad magician!" << endl;
	} else {
	    cout << "Volunteer cheated!" << endl;
	}
    }

    return 0;
}
