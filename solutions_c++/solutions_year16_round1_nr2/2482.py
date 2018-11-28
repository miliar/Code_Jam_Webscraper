#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int c = 1; c <= T; c++)
    {
      int count[2501] = {0};
      int N;
      cin >> N;
      for (int i = 0; i < 2*N-1; i++)
	{
	  for (int j = 0; j < N; j++)
	    {
	      int height;
	      cin >> height;
	      count[height]++;	      
	    }
	}
      vector<int> answer;
      for (int i = 0; i < 2501; i++)
	{
	  if (count[i] % 2 == 1)
	    {
	      answer.push_back(i);
	    }
	}
      assert(answer.size() == N);
      cout << "Case #" << c <<  ":";
      for (int i = 0; i < N; i++)
	{
	  cout << " " << answer[i];
	}
      cout << endl;
    }
}
