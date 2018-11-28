#include<iostream>
#include<string>
#include<fstream>

using namespace std;


void flipper(string& pancakes, int start)
{

  for(int i = start; i >= 0 ;i--)
    {
      if(pancakes[i] == '+'){
	pancakes[i] = '-';
      }
      else
	pancakes[i] = '+';
    }
  //out << pancakes << endl;
}

int main()
{
  int n;
  string s;
  cin >> n;
  
  ofstream out;
  out.open("output.txt");

  for (int j = 0; j < n; j++)
    {
      size_t swaps = 0;
  //     cin >> s;
  //     for(int i = s.length() -2; i >=1; i--)
  // 	{
  // 	  if(s[i] != s[i+1])
  // 	    ++swaps;
  // 	}

  //     if(s[0] == '-')
  //     	swaps++;
  //     if(s[0] == '+' and s[1] == '-')
  // 	swaps+=2;
      // if(s[1] == '-' and s[0] == '+')
      // 	swaps+=1;
      
      // if(s[0] == '-')
      // 	++swaps;
      //       
      
      cin >> s;
      for(int i = s.length() - 1; i >= 0; i--)
      	{
      	  if(s[i] == '-')
      	    {
      	      swaps++;
      	      flipper(s,i);
      	    }

      	}
       out << "Case #" << j+1 << ": " << swaps << endl;
    

    }

}
