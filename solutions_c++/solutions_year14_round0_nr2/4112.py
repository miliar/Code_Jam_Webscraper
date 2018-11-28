#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>
#include<fstream>
#include <cassert>
#include <sstream>
#include <iomanip>
using namespace std;

vector<string> split(const string& s)
{
   vector<string> ret;
   typedef string::size_type string_size;
   string_size i = 0;

   // invariant: we have processed characters [original value of i, i) 
   while (i != s.size()) {
      // ignore leading blanks
      // invariant: characters in range [original i, current i) are all spaces
      while (i != s.size() && isspace(s[i]))
         ++i;

      // find end of next word
      string_size j = i;
      // invariant: none of the characters in range [original j, current j)is a space
      while (j != s.size() && !isspace(s[j]))
         j++;

      // if we found some nonwhitespace characters 
      if (i != j) {
         // copy from s starting at i and taking j - i chars
         ret.push_back(s.substr(i, j - i));
         i = j;
      }
   }
   return ret;
   }

int main()
{ vector<double> v;
 double c,f,x,result;
 double t,j,tj=0,t_previous,rate,t_current;
 string ch;
 int no_of_cases,i;
 ifstream file ("B-large.in");
 ofstream out ("B-large.out");

 getline(file,ch);

 no_of_cases=atoi(ch.c_str());


  cout << fixed << setprecision(7);
  out << fixed << setprecision(7);
 for(i=0;i<no_of_cases;i++)
 {
 getline(file,ch);
 istringstream iss(ch);
 vector<double>::iterator it = v.begin();
 copy(istream_iterator<double>(iss),istream_iterator<double>(),inserter(v,it));
 c=v[0];f=v[1];x=v[2];
 rate=2;t_current=0;t_previous=x/2;
 
     t=t_current+c/rate;
	 rate=rate+f;
     tj=t+x/rate;
	 t_current=t;



    while (tj<t_previous)
	{
     t_previous=tj;
	 t=t_current+c/rate;
	 rate=rate+f;
     tj=t+x/rate;
	 t_current=t;
	 };
	


 cout<<"Case #"<<i+1<<": "<<t_previous<<endl;
 out<<"Case #"<<i+1<<": "<<t_previous<<endl;
 }

 return 0;
}

