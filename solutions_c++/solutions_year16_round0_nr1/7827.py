#include<iostream>
#include<set>
#include<fstream>
using namespace std;
int main()
{
int a,n_cases=0;
set <int> set;
ifstream in;
ofstream out;
in.open("INPUT.in");
out.open("OUTPUT.txt");


in>>a;



while(a>0)
{
	 n_cases++;
	long no,no_cpy,counter=1,p;
	in>>no;
	no_cpy=no;
	p=no;
	
	if(no_cpy==0)
	{
		out<<"Case #"<<n_cases<<":"<<" INSOMNIA\n";

	}
	
    else{

	
	
      while(set.size()<10)
     {
				  no=no_cpy;
        while(no_cpy>0)
       {


	    set.insert(no_cpy%10);
	    no_cpy=no_cpy/10;
         }
	 no_cpy=no;
     if(set.size()<10)
     {

 	   counter++;
	   no_cpy=counter*p;

      }
      else
       {
       out<<"Case #"<<n_cases<<":"<<" "<<no_cpy<<endl;
	   set.clear(); break;

	   }
      }


}a--;
}



}
