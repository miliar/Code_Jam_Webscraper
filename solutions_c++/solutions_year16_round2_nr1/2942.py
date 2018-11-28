#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

int tt;
string sentence;





int main()
{
  cin >> tt;
  getline(cin, sentence);

  for(int t=0; t < tt; t++)
  {
	  getline(cin, sentence);
	  sort(sentence.begin(), sentence.end());
//	  cout << "hello: " << sentence << endl;

	  int solution[10] = {0};

	  int order[10] = {0, 2, 4, 6, 8, 1, 3, 5, 7};
	  string search[10][2] = {
		  {"Z", "ZERO"},
		  {"W", "TWO"},
		  {"U", "FOUR"},
		  {"X", "SIX"},
		  {"G", "EIGHT"},
		  {"O", "ONE"},
		  {"T", "THREE"},
		  {"F", "FIVE"},
		  {"S", "SEVEN"},
	  };
	  
	  for(int i=0; i < 10; i++)
	  {
		  int found = count(sentence.begin(), sentence.end(), search[i][0][0]);
		  solution[order[i]] += found;
		  for(int j=0; j < found; j++)
		  {
//			  cout << "found: " << found << endl;	
			  string kill = search[i][1];
			  for(int k=0; k < kill.length(); k++)
			  {
				  sentence.erase(find(sentence.begin(), sentence.end(), kill[k]));
			  }
		  }

	  }

	  solution[9] += sentence.length() / 4;

//	  cout << "After: " << sentence << endl;
//	  cout << "After: " << sentence.length() << endl;

	  string ohno[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
	  string output = "";
	  for(int i=0; i < 10; i++)
	  {
		  for(int j=0; j < solution[i]; j++)
		  {
			  output += ohno[i];
		  }
	  }

	  

	  cout << "Case #" << t+1 << ": " << output << endl; 
  }

  return 0;
}
