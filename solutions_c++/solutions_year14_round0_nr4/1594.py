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
  fin.open("D-large.txt");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  //	 fout.setf( std::ios::fixed, std:: ios::floatfield );
	// fout.precision(7);
  
  while(test_cases>0)
  {

	int count;
	double temp;
	fin>>count;
	vector<double> first,second;
	vector<double> ffirst,ssecond;
	for(int i=0;i<count;i++)
	{
			fin>>temp;
			first.push_back(temp);
			ffirst.push_back(temp);
	}
	for(int i=0;i<count;i++)
	{
			fin>>temp;
			second.push_back(temp);
			ssecond.push_back(temp);
	}
	sort(first.begin(),first.end());
	sort(second.begin(),second.end());

	int score_g,score_b;
	int score_temp=0;
	score_g = 0;
	score_b = 0;
	for(int i=0;i<count;i++)
	{
		double f1=first.front();
		auto it = second.begin();
		while(it!=second.end())
		{
			if(*it > f1)
			{
				second.erase(it);
				score_temp++;
				break;
			}
			it++;
		}
		first.erase(first.begin());
	}


	score_g = count-score_temp;
//	fin>>second_r;


	std::sort(ffirst.begin(),ffirst.end());
	std::sort(ssecond.begin(), ssecond.end(), std::greater<double>());

	score_temp=0;
	for(int i=0;i<count;i++)
	{
		double f1=ffirst.front();
		auto it = ssecond.begin();
		auto itl = ssecond.back();
		while(it!=ssecond.end())
		{
			if(f1>itl)
			{
				ssecond.pop_back();
				break;
			}
			if(*it > f1)
			{
				ssecond.erase(it);
				score_temp++;
				break;
			}
			it++;
		}
		ffirst.erase(ffirst.begin());
	}


	score_b = count-score_temp;



	fout<<"Case #"<<num++<<": ";
    //if(res.size()==0)
    //  fout<<"Volunteer cheated!"<<endl;
    //else if(res.size()>1)
    //  fout<<"Bad magician!"<<endl;
    //else

	 fout<<score_b<<" "<<score_g<<endl;

    test_cases--;
  }
  return 0;
}