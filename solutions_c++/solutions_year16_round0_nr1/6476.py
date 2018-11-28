#include <iostream>
#include <cstring>
using namespace std;

int main() {
	// your code goes here
	int N,T;
	int digits[10],lastnum,curnum;
	cin >> N;
	for(int i=0;i<N;++i) {
		memset(digits,0,sizeof(digits));
		cin >> T;
		if(T==0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
		else {
			curnum=T;
			while(digits[0]==0 || digits[1]==0 || digits[2]==0 || digits[3]==0 || digits[4]==0 || digits[5]==0 || digits[6]==0 || digits[7]==0 || digits[8]==0 || digits[9]==0) {
				lastnum=curnum;
				while(curnum>0) {
					digits[curnum%10]++;
					curnum=curnum/10;
				}
				curnum=lastnum+T;
			}
			cout << "Case #" << i+1 << ": " << lastnum << endl;
		}
	}
	return 0;
}