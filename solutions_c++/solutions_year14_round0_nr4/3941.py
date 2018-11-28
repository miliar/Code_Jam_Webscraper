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
{ vector<double> naomi;
  vector<double> ken;
  
 string ch;
 int no_of_cases,i,n,j,k,l,m;
 ifstream file ("D-large.in");
 ofstream out ("D-large.out");

 getline(file,ch);

 no_of_cases=atoi(ch.c_str());


  cout << fixed << setprecision(5);
  out << fixed << setprecision(5);
 for(k=0;k<no_of_cases;k++)
 { j=0,m=0;l=0;
   naomi.clear();
   ken.clear();

   getline(file,ch);
   n=atoi(ch.c_str());

   getline(file,ch);
   istringstream iss(ch);

 vector<double>::iterator it = naomi.begin();
 copy(istream_iterator<double>(iss),istream_iterator<double>(),inserter(naomi,it));

 sort(naomi.begin(),naomi.end());

 //cout<<"naomi : ";

 //for (vector<double>::size_type i = 0; i != naomi.size(); ++i)
 //       cout << naomi[i] << " ";
 //
 // cout<<endl;

 getline(file,ch);
  istringstream isd(ch);
  it  = ken.begin();
 copy(istream_iterator<double>(isd),istream_iterator<double>(),inserter(ken,it));
 sort(ken.begin(),ken.end());

   /*cout<<"ken : ";
   for (vector<double>::size_type i = 0; i != ken.size(); ++i)
        cout << ken[i] << " ";
    cout<<endl;*/
   
 while(j<n)
 {   
	 if (naomi[j]>ken[l])
	  l++;
	 j++;
 }
 j=0;
  while(j<n)
 {   
	 if (ken[j]>naomi[m])
	 m++;
	 j++;
 }

   cout<<"Case #"<<k+1<<": "<<l<<" "<<n-m<<endl;
   out<<"Case #"<<k+1<<": "<<l<<" "<<n-m<<endl;
 }

 return 0;
}

