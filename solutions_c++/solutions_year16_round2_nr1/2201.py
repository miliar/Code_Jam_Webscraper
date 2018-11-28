#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <set>

#define ll long long

using namespace std;



string digs[] = {
	"ZERO", "SIX", "EIGHT", "TWO", "THREE", "FOUR", "ONE",  "FIVE",  "SEVEN",  "NINE"
};

int myints[] = {0, 1, 2, 3, 4, 5, 6};
int digord[] = {0, 6, 8, 2, 3, 4, 1, 5, 7, 9};


string ss(map<int, int> letter) {
	string res;

	for(int i=0; i<10; ++i) {
		bool ok = true;
		while(ok) {
			for(int j=0; j<digs[i].length(); ++j) {
				letter[digs[i][j]]--;
				if(letter[digs[i][j]] < 0)
					ok = false;
			}
			for(int j=0; j<digs[i].length() && !ok; ++j) {
				letter[digs[i][j]]++;
			}

			if(ok) res += char(digord[i] + '0');
		}
	}


	for(int i=0; i<256; ++i)
		if(letter[i] != 0)
			cout<<"aa\n";


	sort(res.begin(), res.end());
	return res;

	// for(int i=4; i<10; ++i) {
	// 	bool ok = true;
	// 	for(int j=0; j<digs[i].length(); ++j) {
	// 		letter[digs[i]]--;
	// 		if(letter[digs[i]] < 0)
	// 			ok = false;
	// 	}
	// 	for(int j=0; j<digs[i].length() && !ok; ++j) {
	// 		letter[digord[i]]++;
	// 	}

	// 	if(ok) res += string(digs[i]);
	// }
}

void solve(int t) {

	string num;
	cin>>num;
	
	// vector<int> digits;

	// for(int i=0; i<256; ++i)
	// 	letters[i] = 0;

	map<int, int> letters;

	for(int i=0; i<num.length(); ++i) {
		letters[num[i]]++;
	}



   //  sort(myints,myints+7);

  	// do {
	  //   // std::cout << myints[0] << ' ' << myints[1] << ' ' << myints[2] << '\n';
 	 // } while ( std::next_permutation(myints,myints+6) );



	cout<<"Case #"<<t<<": "<<ss(letters)<<"\n";

}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin>>T;
	int t = 1;
	while(T--)
		solve(t++);

	return 0;

}