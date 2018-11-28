#include <iostream>
#include <fstream>

using namespace std;

int cards[4][4],r,rn;

void input()
{
	cin >> r;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			cin >> cards[i][j];
		}
	}
}

int main()
{
	int t,row[4],card;
    ofstream out;

    out.open("output.txt",ios::out);

	cin >> t;
	int cnt = 1;
	for(int i=1; i<=t; i++) {
        bool found = false,bad = false;
		input();
		for(int j=0; j<4; j++) {
			row[j] = cards[r-1][j];
		}
		input();
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				if(row[j] == cards[r-1][k]) {
					if(found) {
                        bad = true;
					} else {
						card = row[j];
						found = true;
					}
				}
			}
		}
		if(bad) {
            out << "Case #" << cnt << ": Bad magician!" << endl;
            cnt++;
		} else {
            if(!found) out << "Case #" << cnt << ": Volunteer cheated!" << endl;
            else out << "Case #" << cnt << ": " << card << endl;
            cnt++;
		}
	}

	return 0;
}