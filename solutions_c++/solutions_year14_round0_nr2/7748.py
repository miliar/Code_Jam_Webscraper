#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream cin( "input.txt" );
    ofstream cout( "output.txt" );
    
    int n;
    cin >> n;
    
    for( int i=0; i<n; i++ )
    {
    	double C, F, X;
    	cin >> C >> F >> X;
    	
    	double time = X, timeN = X / 2;
    	
    	for( int j=1; timeN < time; j++ )
    	{
    		time = timeN;
			
			timeN += X/( 2 + F * j ) + C / (2 + F * (j - 1)) - X / (2 + F * (j - 1));
    	}
    	
    	cout << "Case #" << i+1 << ": " << fixed << setprecision( 7 ) << time << endl;
    }
}
