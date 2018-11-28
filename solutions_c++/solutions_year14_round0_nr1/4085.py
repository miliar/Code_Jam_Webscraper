#include<fstream>
#include<iostream>
#include<vector>
#include<string>
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
{  vector<string>v;
   vector<string>y;
   string ch,c;int no_of_cases,i,rownum1,rownum2,j,k;
   	
	ifstream f ("A-small-attempt0.in");
	ofstream g ("A-small-attempt0.out");
	getline(f,ch);
	//v=split(ch);
	no_of_cases=atoi(ch.c_str());
	//cout<<ch<<endl;

	for(i=0;i<no_of_cases;i++)
	{ 
		c="Volunteer cheated!";

		getline(f,ch);
		rownum1=atoi(ch.c_str());
		for (j=1;j<=4 && getline(f,ch);j++)
		{ if (j==rownum1)
			 v=split(ch);
		}

		/*cout<<"v :";
		for(j=0;j<v.size();j++)
			cout<<v[j]<<" ";
		cout<<endl;*/
		
		getline(f,ch);
		rownum2=atoi(ch.c_str());

		for (j=1;j<=4 && getline(f,ch);j++)
		{	
			if (j==rownum2)    	
		    { y=split(ch); }
		}

	/*	cout<<rownum2<<"y :";

		for(j=0;j<y.size();j++)
			cout<<y[j]<<" ";
		cout<<endl;*/

		for (j=0;j<y.size();j++)
		  { for (k=0;k<v.size();k++)
		     { if (y[j]==v[k])
		       {    if (c=="Volunteer cheated!") 
			          {c=y[j];}
			        else
                     { c="Bad magician!";						 
		              break; }
		        }
		     }
		 }
		
		cout<<" "<<"Case #"<<i+1<<": "<<c<<endl;
		g<<"Case #"<<i+1<<": "<<c<<endl;

     }

 f.close();

 return 0;

}