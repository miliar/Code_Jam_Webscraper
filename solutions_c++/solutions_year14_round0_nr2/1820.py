#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm> // sort, max_element, random_shuffle, remove_if, lower_bound 
#include <functional>
#include <fstream>
#include <set>
using namespace std;
char a[4][4];
int main()
{
  int test_cases;
  ifstream fin;
  fin.open("B-large.txt");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  	 fout.setf( std::ios::fixed, std:: ios::floatfield );
	 fout.precision(7);
	 	double C,F,X;
 // 	fin>>C>>F>>X;
//	test_cases=1000;
  while(test_cases>0)
  {
	  double res=0;

	fin>>C>>F>>X;
	double X1=X;
	long long int num_buy=0;
	double rate = 2;
//	long long int maxcount = X1/C;
/*	while(X1/(double)rate > (X1/((double)rate+F) + C/(double)rate))
	{
		num_buy=num_buy*2;
		if(num_buy==0)
			num_buy=1;
		rate=ra(double)num_buy*F;
	}
*/
	rate-=(double)num_buy*F;
	num_buy/=2;
	while(X1/(double)rate > (X1/((double)rate+F) + C/(double)rate))
	{
		num_buy++;
		rate+=F;
	}

	rate = 2;
	for(int i=0;i<num_buy;i++)
	{
		res+=C/(double)rate;
		rate+=F;
	}
	res+= X/rate;

//	fin>>second_r;

	fout<<"Case #"<<num++<<": ";
    //if(res.size()==0)
    //  fout<<"Volunteer cheated!"<<endl;
    //else if(res.size()>1)
    //  fout<<"Bad magician!"<<endl;
    //else

	 fout<<res<<endl;

    test_cases--;
  }
  return 0;
}