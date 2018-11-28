#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <array>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
class Record {
	public:
	int rec[10];
	
	Record() {
		for (int i=0;i<10;i++) {
			rec[i]=0;
		}
	}
	
	bool isFull() {
			for (int i=0;i<10;i++) {
				if (rec[i]==0) {
					return false;
				}
			}
			return true;
		}
};


int sheepCount(int n) {
	if (n==0) {
		return 0;
	}
	
	Record track;
	int mul=1;
	int num, digit;
	while (mul<9999999) {
		num=n*mul;
		while (num != 0) {
			digit = num%10;
			if (track.rec[digit]==0) {
				track.rec[digit]=1;
				if (track.isFull()) {
					return n*mul;
				}
			}
			num = (int) num/10;
		}
		mul++;
	}
	return 0;
}

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    int out = sheepCount(n);
    if (out != 0) {
	   cout << "Case #" << i << ": " << out << endl;
	}
	else {
		   cout << "Case #" << i << ": INSOMNIA" << endl;
		}
    
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}