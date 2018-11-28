//
//  main.cpp
//  google_code_jam
//

#include <iostream>
#include <vector>
#include <iomanip> 

using namespace std;

using std::vector;
using std::cin;
using std::cout;

int main(int argc, const char * argv[])
{
	int num_test_cases = 0;
	
	cin>>num_test_cases;
	if (num_test_cases < 1 || num_test_cases > 100)
		num_test_cases = 0;
	
	for (int test_case = 1; test_case <= num_test_cases; test_case++)	{
		double c = 0.0;
		double x = 0.0;
		double f = 0.0;
		double total_time = 0.0;
		double cookies_per_sec = 2.0;
		
		cin>>c;
		cin>>f;
		cin>>x;
		
		while(true)	{
			double x_sec = x / cookies_per_sec;
			double x_with_c_sec = (c/cookies_per_sec) + (x/(cookies_per_sec + f));
			
			if (x_with_c_sec < x_sec)	{
				total_time += c/cookies_per_sec;
				cookies_per_sec += f;
			}
			else{
				total_time += x/cookies_per_sec;
				break;
			}
		}
		
		cout<<"Case #"<<test_case<<": "<<std::fixed<<std::setprecision(7)<<total_time<<"\n";
	}
	
    return 0;
}

