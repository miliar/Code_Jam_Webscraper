#include <iostream>
#include <iomanip>
using namespace std;

class Game
{
	double play( double timeToReduce, double &timeToBuyFarm );
public:
	double C;
	double F;
	double X;
	double rate;
	Game ( double c, double f, double x ) :
		C( c ), F( f ), X( x ), rate( 2.0 ) { }
	double play();
};

double Game::play( double timeToReduce, double &timeToBuyFarm)
{
	timeToBuyFarm = C/rate;
	rate += F;
	return ( timeToBuyFarm + X/rate );
}

double Game::play( )
{
	double timeToReduce = X/rate;
	double savedTime = 0;
	double timeToBuyFarm = 0;
	double currentBestTime = X/rate;

	while( 1) 
	{
		double newTime = play( timeToReduce, timeToBuyFarm );
		if( newTime < timeToReduce )
		{
			currentBestTime = savedTime + newTime ;
			savedTime += timeToBuyFarm;
			timeToReduce = newTime - timeToBuyFarm;
		}
		else
			break;
	}

	return currentBestTime;
}



int main()
{
	int numTC = 0, currentTC = 0;

	cin >> numTC;
	while( ++currentTC <= numTC )
	{
		double C = 0.0f, F = 0.0f, X = 0.0f;
		cin >> C >> F >> X;
		
		Game cookieGame( C, F, X );
		double seconds = cookieGame.play();
		cout << std::fixed << std::setprecision(7) << "Case #" << currentTC <<": " << seconds<<"\n";
	}
}
