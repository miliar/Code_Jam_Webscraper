#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

using std::cout;
using std::cin;
using std::string;
using std::stringstream;

// エントリポイント
int main(int argc, char* argv[])
{
	std::ofstream ofs("result.txt");
	string buf;
	int time(0), sel1(0), sel2(0), k, j, cards1[4][4], cards2[4][4], num, comp;
	bool res;
	cin >> time;
	
	for ( int t=1; t<=time; t++ ) {
		// 1回目入力
		cin >> sel1;
		cin.ignore(1024, '\n');
		for ( k=0; k<4; k++ ) {
			std::getline(cin, buf);
			stringstream ss(buf);
			ss >> cards1[k][0] >> cards1[k][1] >> cards1[k][2] >> cards1[k][3];
			if ( ss.fail() ) return 0;
		}
		
		// 2回目入力
		cin >> sel2;
		cin.ignore(1024, '\n');
		for ( k=0; k<4; k++ ) {
			std::getline(cin, buf);
			stringstream ss(buf);
			ss >> cards2[k][0] >> cards2[k][1] >> cards2[k][2] >> cards2[k][3];
			if ( ss.fail() ) return 0;
		}
		
		if ( sel1<1 || sel1>4 || sel2<1 || sel2>4 ) return 0;
		sel1--;
		sel2--;
		comp = 0;
		for ( k=0; k<4; k++ ) {
			for ( j=0; j<4; j++ ) {
				res = (int)(cards1[sel1][k]==cards2[sel2][j]);
				if ( res ) {
					num = cards1[sel1][k];
					comp++;
				}
			}
		}
		
		if ( comp>=2 ) {
			ofs << "Case #" << t << ": Bad magician!\n";
		}
		else if ( comp==0 ) {
			ofs << "Case #" << t << ": Volunteer cheated!\n";
		}
		else {
			ofs << "Case #" << t << ": " << num << "\n";
		}
	}
	
	return 0;
}

