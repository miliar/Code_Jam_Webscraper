#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#define ARAY_NUMBER (5)

void div10(int x, unsigned char aryBit[ARAY_NUMBER] )
{
  aryBit[0] = aryBit[1] =  aryBit[2] = aryBit[3] = aryBit[4] = 0;
  for ( int i = 0; i < ARAY_NUMBER; i++ ) {
	  int y = ((((x>>3)+x)>>1)+x)>>4;
	  int t;
	  do{
		 t = x-(((y<<2)+y)<<1) + 1;
		 y += ((((t>>3)+t)>>1)+t)>>4;
	  }while(t > 10);
	  aryBit[i] = (t - 1); 
	  if ( y == 0 ) break;
	  x = y;
  }
}
int loopAdd(int x, int limit, unsigned char aryBit[ARAY_NUMBER], unsigned char aryWork[ARAY_NUMBER])
{
	unsigned short data;
	unsigned char flg;
	unsigned char valid;
	int number;
	if ( x  == 0 ) return 0; 
	data = 0;
	aryWork[0] = aryWork[1] =  aryWork[2] = aryWork[3] = aryWork[4] = 0;
	for ( number = x; number <= limit & data != 0x3FF; number +=x ) {
		aryWork[0] += aryBit[0];
		flg = ( aryWork[0] >= 10 );
		aryWork[0] -= 10 * flg;
	
		aryWork[1] += aryBit[1] + flg;
		flg = ( aryWork[1] >= 10 );
		aryWork[1] -= 10 * flg;
	
		aryWork[2] += aryBit[2] + flg;
		flg = ( aryWork[2] >= 10 );
		aryWork[2] -= 10 * flg;

		aryWork[3] += aryBit[3] + flg;
		flg = ( aryWork[3] >= 10 );
		aryWork[3] -= 10 * flg;

		aryWork[4] += aryBit[4] + flg;
		flg = ( aryWork[4] >= 10 );
		aryWork[4] -= 10 * flg;

		data  |= (aryWork[4]!=0 ? (1 << aryWork[4]) : 0 );
		data  |= (aryWork[3]==0 ? (aryWork[4] != 0) : (1 << aryWork[3]) );
		valid  = aryWork[3] + aryWork[4];
		data  |= (aryWork[2]==0 ? (valid != 0)      : (1 << aryWork[2]) );
		valid += aryWork[2];
		data  |= (aryWork[1]==0 ? (valid != 0)      : (1 << aryWork[1]) );
		data  |= ( 1 << aryWork[0] );
	}
	if ( data != 0x3FF) return 0;
	return number - x;
}

void main() {
  int t, n;
  unsigned char aryFlag[ARAY_NUMBER];
  unsigned char aryOut[ARAY_NUMBER];
  int answer;

  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
	div10(n, aryFlag );
	answer = loopAdd(n, 40000, aryFlag, aryOut );

	// answer
    cout << "Case #" << i << ": ";
	if ( 0 == answer ) cout << "INSOMNIA" << endl;
	else cout << answer << endl;
  }
}