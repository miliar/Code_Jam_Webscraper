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
  fin.open("A-small-attempt02.txt");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  std::set<int> Ahold;
  int temp;

  while(test_cases>0)
  {
  int state=0;
  int result = -1;
  int first_r,second_r;
	fin>>first_r;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			fin>>temp;
			if(i==first_r-1)
				Ahold.insert(temp);
		}

	fin>>second_r;
	vector<int> res;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			fin>>temp;
			if(i==second_r-1)
				if(Ahold.find(temp)!=Ahold.end())
				{
					res.push_back(temp);
				}

		}
//	fin>>second_r;
    fout<<"Case #"<<num++<<": ";
    if(res.size()==0)
      fout<<"Volunteer cheated!"<<endl;
    else if(res.size()>1)
      fout<<"Bad magician!"<<endl;
    else
		fout<<res.front()<<endl;
	Ahold.clear();
	res.clear();
    test_cases--;
  }
  return 0;
}