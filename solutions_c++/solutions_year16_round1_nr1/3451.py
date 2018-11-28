#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>

using namespace std;

int main()
{
  int t;
  string input, lastword, temp;

  cin>>t;
  
  for(int i=1; i<=t; i++)
    {
      cin>>input;
      for(int j=0; j<input.length(); j++)
	{
	  temp = input[j];
	  if(input[j] >= lastword[0])
	    {
	      lastword.insert(0, temp);
	    }
	  else
	    {
	      lastword.insert(j, temp);
	    }
	}
      cout<<"Case #"<<i<<": "<<lastword<<endl;
      lastword.clear();
    }

  return 0;
}
