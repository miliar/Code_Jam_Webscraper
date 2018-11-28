#include <iostream>
using namespace std;

int main ()
{
  int count;
  //cout << "Please enter an integer value: ";
  cin >> count;
  //cout << count;
  int shy;
  char val;
  int friends;
  int audience;
  int person;

  for (int i = 0; i < count; i++)
  {
	friends = 0;
	audience = 0;
	cin >> shy;
	for (int j = 0; j <= shy; j++)
	{
		cin >> val;
		person = val - 48;
		if (person == 0 && j >= audience)
		{
			friends++;
			audience++;
		}
		audience += person;
	}	
	cout << "Case #" << (i+1) << ": " << friends << endl;
  }
  //cout << "The value you entered is " << i;
  //cout << " and its double is " << i*2 << ".\n";
  return 0;
}