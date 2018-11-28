#include<iostream>
#include<cstdint>
using namespace std;

typedef std::uint32_t board;


//count bits set (from http://graphics.stanford.edu/~seander/bithacks.html)
unsigned int pcount(board v)
{
v = v - ((v >> 1) & 0x55555555);                    // reuse input as temporary
v = (v & 0x33333333) + ((v >> 2) & 0x33333333);     // temp
return ((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24; // count

}

static const char pieces[4]={'.','T','X','O'};

board read_board(istream& in)
{
	board b=0;
	for(int i=0;i<21;i++)
	{
		int s;
		int c=in.get();
			
		for(s=0;s<4;s++)
		{
			if(c==pieces[s])
				break;
		}
		if(s < 4)
		{
			b <<= 2;
			b|=s;
		}
	}
	return b;
}

static const board wins[]={
	0x000000FF,	//rows
	0x0000FF00,
	0x00FF0000,
	0xFF000000,
	0x03030303,	//columns...0b00000011
	0x0C0C0C0C,     //0b00001100
	0x30303030,
	0xC0C0C0C0,
	0xC0300C03,	//diagonals
	0x030C30C0
};

bool is_completed(board b)
{
	b&=0xAAAAAAAA; //a completed board has exactly 15 high-order bits
	return pcount(b)>=15;
}

std::string boardstatus(board b)
{
	for(unsigned int i=0;i<10;i++)	//10 possible winning configurations
	{
		board wcheck=b & wins[i];
		board hi=(wcheck & 0xAAAAAAAA) >> 1;
		board lo=wcheck & ~0xAAAAAAAA;
		
		/*
		 * 1110
		1111  ->o wins

		1111  ->o wins
		1111

		1111
		0000  ->x wins

		1110
		0001  ->x wins*/

		if(pcount(hi^lo)==4)
		{
			return "X won";
		}
		if(pcount(hi & lo) >= 3 && pcount(lo)==4)
		{
			return "O won";
		}
	}
	if(is_completed(b))
	{
		return "Draw";
	}
	return "Game has not completed";
}



int main()
{
	size_t T;
	cin >> T;
	
	for(size_t i=0;i<T;i++)
	{
		board b=read_board(cin);
		cout << "Case #" << i+1 << ": " << boardstatus(b) << endl;
	}
	
	return 0;
}
