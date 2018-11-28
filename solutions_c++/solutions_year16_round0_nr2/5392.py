//Revenge of the pancakes
#include <iostream>
using namespace std;
int main()
{
  string input;
  int N;
  int counter;
  int same;
  bool done;
  cin >> N;
  char b;
  char a;
  for(int i = 1; i <= N; i++)
  {
	cin >> input;
	cout << "Case #" << i << ": ";
	counter = -1;
	same = 0;
	done = false;
	b = input[0];
	a = b;
	while(!done)
	{
      counter++;
	  while(b == a)
	  {
	    same++;
		if(same == input.size())
		{
		  done = true;
		  if(b == '-')
			counter++;
		  break;
		}
		a = input[same];
	  }
	  b = a;
	}
	cout << counter << endl;
  }
  return 0;
}