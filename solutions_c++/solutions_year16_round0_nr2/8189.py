#include <iostream>
#include <string>
#include <algorithm>


using namespace std;


int main()
{
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
     string s;
     int count=0;
     cin>>s;
     while(true)
     {
     
	    std::reverse(s.begin(),s.end())	;
     	std::size_t found=s.find('-');
     	if (found==string::npos)
     	{
     		break;
		 }
		    std::reverse(s.begin(),s.end())	;
		 count++;
		 for(int i=0; i < (s.size()-found) ;i++)
		 {
		 
		 if (s[i]=='-')
		    s[i]='+';
		 else
		     s[i]='-';
		}
		 
	 }
  	
    cout << "Case #" << i << ": " << count << endl;
  
  }
}
