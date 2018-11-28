#include <fstream>
#include <math.h>

//calculate the paint needed based on innner radius of ring.
//int paint_cost( int r )
//{
//	return 2 * r + 1;
//}



int main()
{
	//open files.
	std::ifstream in;
	std::ofstream out;

	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");

	//global variables.
	int T, r, t;
	in >> T;

	//in & out.
	for( int test_case = 0; test_case < T; test_case ++ )
	{
		in >> r >> t;	
		out << "Case #" << test_case + 1 << ": " <<
			(int)(( 1 - 2 * r + std::sqrt( (float)( (2*r-1)*(2*r-1) + 8 * t) )) / 4)
			<< std::endl;
	}


	//close files.
	in.close();
	out.close();

	return 0;
}