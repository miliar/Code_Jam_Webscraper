#include<iostream>
#include<cstring>

#define WIDTH 4

using namespace std;

int arr[16] = {0};

int main(int argc, char * argv []) {
    int T;
    cin >> T;
    for(int i=0; i<T; i++) {
	memset(arr, 0, sizeof(arr));
	int fst = 0;
	cin >> fst;
	int num;
	for(int j=0; j<WIDTH; j++) {
	    for(int k=0; k<WIDTH; k++) {
		cin >> num;

		if(j+1 != fst) continue;

		arr[num-1] = 1;
	    }
	}

	bool bad_m = false;
	int tar = -1;

	cout << "Case #" << i+1 << ": ";

	int snd;
	cin >> snd;

	for(int j=0; j<WIDTH; j++) {
	    for(int k=0; k<WIDTH; k++) {
		cin >> num;

		if(j+1 != snd) continue;

		if(arr[num-1] == 1) {
		    if(tar == -1) {
		      tar = num;
		    } else {
			bad_m = true;
		    }
		}
	    }
	}

	if(bad_m) cout << "Bad magician!"; 
	else if(tar != -1) cout << tar;
	else cout << "Volunteer cheated!";
	cout <<endl;
    }
    return 0;
}
