#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
#include <iostream>
#include<stdlib.h>
#include<stdio.h>
#include<map>

using namespace::std;

bool is_palindrome(int num)
{

  char NUM[5] = {'\0'};
  int num_len = 0;

  sprintf(NUM , "%d" , num);

  for(int i = 0; NUM[i] != '\0'; i++)num_len++;

  for(int i = 0; i < num_len / 2; i++)
    {
      if(NUM[i] != NUM[num_len - i - 1])
	{
	  return false;
	}
    }

  return true;

}



int main(void)
{
  map<int , int> m;

  for(int i = 1; i <= 1000; i++)
    {
      m[i * i] = i;
    }

  int T;

  cin >> T;

  for(int i = 0; i < T; i++)
    {
      int A , B;
      cin >> A >> B;
      int ans = 0;

      for(int j = A; j <= B; j++)
	{

	  if( m.find(j) != m.end() )
	    {

	      if( is_palindrome(j) == true && is_palindrome(m[j]) == true)
		{
		  ans++;
		}

	    }

	}
      cout << "Case #" << i + 1 << ": " << ans << endl;
    }


  return 0;
}
