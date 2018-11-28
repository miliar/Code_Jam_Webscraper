#include <stdio.h>
#include<iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <fstream>
using namespace std;
char ll;
int ct=0;
std::string str;

int main()
{
    //FILE *f = fopen("ina.txt", "r");
   // FILE *f1 = fopen("outnew1.txt", "w");
    std::ifstream file("ina.txt");
    std::ofstream out("outa.txt");
    int t;
    int ii=1;
   // cin>>t;
    //fscanf(f, "%d",&t);
    file>>t;


  while(t--)
  {
   //fscanf(f,"%s",&str);
   file>>str;

    std::string s="";
    s=s+str[0];

	int n = str.length();
	std::string word = str;
    std::sort(word.begin(), word.end());
	ll=word[n-1];
	int i;

	for( i=1;i<n;i++)
    {
        int l=s.length();
         if(s.length()==n && s[0]==ll)
        break;
        else
        {

        if(str[i]>s[i-1] && str[i]>=s[0])
                  s=str[i]+s;

        else
       s=s+str[i];


        }

    }

    out<<"Case #"<<ii<<": "<<s;
    out<<endl;
    ii++;
  }
    out.close();
	return 0;
}
