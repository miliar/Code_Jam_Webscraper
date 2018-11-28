#include <iostream>
using namespace std;

unsigned pos;

unsigned short row(unsigned short curr=pos) {
	return curr/4;
}

unsigned short col(unsigned short curr=pos) {
	return curr%4;
}

int main() {
	unsigned int T;
	char set[4][5];
	bool result[256];
	cin >> T;
	for(int i=1;i<=T;++i) {
		bool finished = true;
		bool checked[4][4] = {false};
		result['X'] = false;
		result['O'] = false;
		cin >> set[0] >> set[1] >> set[2] >> set[3];
		for(pos=0;pos<16;++pos) {
			char plyr = set[row()][col()];
			if(plyr!='.' && result[plyr] == false) {
				if(col()<1
					&& (set[row()][col()+1]==plyr || set[row()][col()+1]=='T')
					&& (set[row()][col()+2]==plyr || set[row()][col()+2]=='T')
					&& (set[row()][col()+3]==plyr || set[row()][col()+3]=='T')	)
					result[plyr] = true;
				else if(col()<1 && row()<1
					&& (set[row()+1][col()+1]==plyr || set[row()+1][col()+1]=='T')
					&& (set[row()+2][col()+2]==plyr || set[row()+2][col()+2]=='T')
					&& (set[row()+3][col()+3]==plyr || set[row()+3][col()+3]=='T')	)
					result[plyr] = true;
				else if(row()<1
					&& (set[row()+1][col()]==plyr || set[row()+1][col()]=='T')
					&& (set[row()+2][col()]==plyr || set[row()+2][col()]=='T')
					&& (set[row()+3][col()]==plyr || set[row()+3][col()]=='T')	)
					result[plyr] = true;
				else if(col()==3 && row()<1
					&& (set[row()+1][col()-1]==plyr || set[row()+1][col()-1]=='T')
					&& (set[row()+2][col()-2]==plyr || set[row()+2][col()-2]=='T')
					&& (set[row()+3][col()-3]==plyr || set[row()+3][col()-3]=='T')	)
					result[plyr] = true;
			} else if(plyr=='.') {
				finished = false;
			}
		}
		if(result['X']==true && result['O']==false)
			cout << "Case #" << i << ": X won\n";
		else if(result['X']==false && result['O']==true)
			cout << "Case #" << i << ": O won\n";
		else if(result['X']==false && result['O']==false && finished || result['X']==true && result['O']==true)
			cout << "Case #" << i << ": Draw\n";
		else
			cout << "Case #" << i << ": Game has not completed\n";
	}
	return 0;
}