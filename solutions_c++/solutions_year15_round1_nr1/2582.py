#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <list>
#include <algorithm>
#include <map>

#define FO(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

using namespace std;

long first_method(const vector<int> &mr)
{
  long res = 0;
  for (int i = 1; i < mr.size(); i++)
  {
    if (mr[i - 1] > mr[i])
      res += (long)mr[i - 1] - (long)mr[i];
  }

  return res;
}

long second_method(const vector<int> &mr)
{
  long res = 0;

  int rate = 0;
  for (int i = 1; i < mr.size(); i++) {

    if (mr[i - 1] > mr[i])
      rate = max(rate, mr[i - 1] - mr[i]);
  }

  int rem = 0;
  for (int i = 0; i < mr.size() - 1; i++) {
    
    res += min((long)rate, (long)mr[i]);
    rem = max (mr[i] - rate, 0);
  }

  return res;
}

int main()
{
	//string file_name = "sample";

	//string file_name = "A-small-attempt3";
	string file_name = "A-large";	

	ofstream output_file(file_name + ".out");
	ifstream input_file (file_name + ".in");	

	int no_tests;
	if (input_file >> no_tests) {

		for (int test = 0; test < no_tests; test++) {

			int n;
			if (input_file >> n) {

        vector<int> mr;
        for (int i = 0; i < n; i++)
        {
          int t;
          input_file >> t;
          mr.push_back(t);
        }
        long ans1, ans2;

        ans1 = first_method(mr);
        ans2 = second_method(mr);

				output_file << "Case #" << (test + 1) << ": " << ans1 << " " << ans2 << std::endl;
			} 
		}
	}

	input_file .close();
	output_file.close();

	return 0;
}