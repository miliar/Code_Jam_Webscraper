//#include<iostream>
//#include<string>
//#include <fstream>
//
//using namespace std;
//int main()
//{
//	std::ifstream infile("A-small-attempt Large.in");
//	ofstream myfile("A-small-attempt Large.out");
//	
//	long long input, si, t_c, result, tillNow;
//	string _case;
//	infile >> t_c;
//	for(int i=1; i <= t_c; i++)
//	{
//		result = tillNow = 0;
//		infile >> si >> _case;
//		for(int j=0; j<=si; j++)
//		{
//			if(tillNow < j)
//			{
//				result++;
//				tillNow++;
//			}
//			tillNow += _case[j] - '0';
//		}
//		myfile << "Case #"<< i << ": " << result << endl;
//	}
//	infile.close();
//	myfile.close();
//	return 0;
//}



#include<iostream>
#include<string>
#include <fstream>

using namespace std;
int main()
{
	long long input, si, t_c, result, tillNow;
	string _case;
	cin >> t_c;
	for(int i=1; i <= t_c; i++)
	{
		result = tillNow = 0;
		cin >> si >> _case;
		for(int j=0; j<=si; j++)
		{
			if(tillNow < j)
			{
				result++;
				tillNow++;
			}
			tillNow += _case[j] - '0';
		}
		cout << "Case #"<< i << ": " << result << endl;
	}
	return 0;
}