#include <iostream>
using namespace std;

long long ringArea(long long r)
{
    return (2*r + 1);
}

int main()
{
    int T;
    
    cin >> T;
    
    for (int i=0; i<T; i++)
    {
	long long r, t;
	long long paint=0, rings=0;

	cin >> r >> t;
	
	do
	{   
	    if (t < 3)
	    {
		rings = 1;
		break;
	    }
	    paint += ringArea(r);
	    rings++;
	    //cout << "Case #" << i << ": " << " R: " << r << " Paint: " << t << " Paint used: " << paint << " Rings: " << rings << endl;
	    
	    r += 2;
	}
	while(t >= paint);
	//cout << "................................" << endl;

	cout << "Case #" << i + 1<< ": " << rings - 1 << endl;
    }
    
    return 0;
}
