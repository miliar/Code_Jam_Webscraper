#include <fstream>

using namespace std;


int main() {
	ifstream f_in ("in.txt");
	ofstream f_out ("out.txt");
	int t;
	f_in >> t;
	for ( int test = 1; test <= t; test++ ) {
		int a = 0, b = 0, s = -1, ap = 0;
		int ar[4];
		bool mul = false;
		f_in >> a;
		for ( int i = 1; i <= 4; i++ ) { // row
			for ( int f = 1; f <= 4; f++ ) { // col
				int temp;
				f_in >> temp;
				if ( i == a ) {
					ar[ap++] = temp;
				}
			}
		}
		f_in >> b;
		for ( int i = 1; i <= 4; i++ ) {
			for ( int f = 1; f <= 4; f++ ) {
				int temp;
				f_in >> temp;
				if ( i == b && !mul ) {
					for ( int j = 0; j < 4; j++ ) {
						if ( ar[j] == temp ) {
							if ( s == -1 ) {
								s = temp;
							} else {
								mul = true;
							}
						}
					}
				}
			}
		}
		f_out << "Case #" << test << ": ";
		if ( mul ) {
			f_out << "Bad magician!";
		} else if ( s == -1 ) {
			f_out << "Volunteer cheated!";
		} else {
			f_out << s;
		}
		if ( test != t ) {
			f_out << '\n';
		}
	}
	f_in.close();
	f_out.close();
	return 0;
}
