#include "cstdio"
#include <fstream>
#include <iostream>
using namespace std;
typedef long long i64;

int main() {
  ifstream infile;
  ofstream outfile;
  infile.open("A-small-attempt1.in");
  outfile.open("a.out");
  int T = 0;
//  scanf("%d", &T); 
  infile >> T;
  cout << "TEST CASE: " << T << endl;
  int R;
  int row[4];
  int row2[4];
  int chk = 0;
  int chkCard = 0;
  for (int Ti = 1; Ti <= T; ++Ti) {
	for (int i=0 ; i < 2; ++i) {
		//scanf("%d", &R);
		infile >> R;
		cout << "ROW: " << R << " " ;
		for(int j=1; j <= 16; j++)
		{
			int card;
			//scanf("%d", &card);
			infile >> card;
			if((R-1)*4 < j && R*4 >= j)
			{
				(i==0) ? row[j-((R-1)*4)-1] = card : row2[j-((R-1)*4)-1] = card;
			}
		}
	}
	printf("TEST %d [%d,%d,%d,%d] - [%d,%d,%d,%d] ",Ti,
						row[0],row[1],row[2],row[3],
						row2[0],row2[1],row2[2],row2[3]);

	chk = 0;
	chkCard = 0;
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++)
		{
			if(row[i] == row2[j])
			{
				chk++;
				chkCard = row[i];
			}
		}
	}
	char buf[64];
	switch(chk)
	{
		case 1:	sprintf(buf,"Case #%d: %d\n", Ti, chkCard);	break;
		default: sprintf(buf,"Case #%d: Bad magician!\n", Ti);	break;
		case 0: sprintf(buf,"Case #%d: Volunteer cheated!\n", Ti); break;
	}
	printf("Result %d Card %d\n", chk, chkCard);
	outfile << buf;
  }
  infile.close();
  outfile.close();
  return 0;
}