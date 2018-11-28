#include <iostream>
using namespace std;

int main()
{
  int T; //number of test cases
  string input;
  string front_end;
  string back_end;
  int hv;
  int j;
  
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
	cin >> input;
	cout << "Case #" << i << ": ";
	front_end.push_back(input[0]);
	for(j = 1; j < input.size(); j++)
	{
	  if(input[j] >= front_end[front_end.size() - 1])
		front_end.push_back(input[j]);
	  else
	    back_end.push_back(input[j]);
	}
	for(j = front_end.size() - 1; j >= 0; j--)
	  cout << front_end[j];
    cout << back_end << endl;
	front_end.clear();
	back_end.clear();
  }
  return 0;
}