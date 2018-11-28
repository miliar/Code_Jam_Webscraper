#include <iostream>
#include <iomanip>
using namespace std;


class Set
{
public:
	double c, f,  x, cur, p;

	Set()
	{
		p = 2;
		cur = 0;
	}

	double simulate()
	{
		double t1 , t2;
		
		for(;;)
		{
			t1 = holding();
			t2 = check_next();

			if(t1 > t2)
			{
				next_farm();
			}
			else 
			{
				cur = cur + t1;
				break;
			}	
		}

		return cur;
	}

	double holding()
	{
		return(x/p);
	}

	void next_farm()
	{
		double f1, f2;
		f1 = c/p;
		cur = cur+ f1;
		p = p+f;
	}
	double check_next()
	{
		double f1, f2, f3;
		f1 = c/p;
		f2 = p+f;
		f3 = x/f2;
		return(f1+f3);

	}
};

int main()
{

	int cases;
	cin >> cases;
	Set *set;
	set = new Set[cases];
	double *arr = new double[cases];

	for (int i = 0; i < cases; ++i)
	{
		cin >> set[i].c;
		cin >> set[i].f;
		cin >> set[i].x;
		arr[i] = set[i].simulate();
		//std::cout << setprecision(7);
		std::cout.precision(7);
  		std::cout.setf( std::ios::fixed, std:: ios::floatfield );
		cout << "Case #" << i+1 << ": " << arr[i] << endl;
	}

	delete[] set;
	return 0;
}