#include <iostream>
#include <iomanip>
#include <list>
#include <algorithm>

using namespace std;

class Game
{
public:
	list<double> N;
	list<double> K;

	Game ( ) : N(), K(){ }
	void init();
	int play();
	int playD();
};

void Game::init()
{
	N.sort();
	K.sort();
}

int Game::playD()
{
	int pointsN = 0;
	
	list<double>::iterator itrN, itrK;

	while( ( itrN = N.begin() ) != N.end() )
	{
		if( *itrN < *(K.begin()) )
		{
			// say lie to waste max which is greater than *itrN
			K.pop_back();
			N.erase( itrN );
		}
		else
		{
			K.erase( K.begin() );
			N.erase( itrN );
			++pointsN;
		}
	}

	return pointsN;
}

int Game::play()
{
	int pointsN = 0;
	list<double> N1(N);
	list<double> K1(K);

	list<double>::iterator itrN, itrK;
	while( ( itrN = N1.begin() ) != N1.end() )
	{
		for( itrK = K1.begin(); itrK != K1.end(); ++itrK)
		{
			if(*itrK > *itrN)
			{
				break;
			}
		}
		if( itrK != K1.end() )
		{
			K1.erase( itrK );
			N1.erase( itrN );
		}
		else
		{
			K1.erase( K1.begin() );
			N1.erase( itrN );
			++pointsN;
		}
	}
	return pointsN;
}

int main()
{
	Game war;
	int numtc = 0, currenttc = 0, num = 0;
	double val = 0;

	cin >> numtc;
	while( ++currenttc <= numtc )
	{
		cin >> num;
		for( int i = 0; i < num; ++i )
		{
			cin >> val;
			war.N.push_back( val );	
		}
		for( int i = 0; i < num; ++i )
		{
			cin >> val;
			war.K.push_back( val );	
		}
		war.init();

		cout << "case #" << currenttc <<": " << war.playD() << " " << war.play()<<"\n";
	}

	return 0;
}
