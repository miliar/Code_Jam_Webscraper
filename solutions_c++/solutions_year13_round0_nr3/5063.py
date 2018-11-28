#include <iostream>
#include <math.h>
#include <sstream>
#include <fstream>
#include <string.h>
using namespace std;

int Is_square (int num)
{
  int square_root = (int) sqrt((double) num);
  if(square_root *square_root == num)
    return square_root;
  else
    return -1;
}

bool Is_palindrome(int num)
{

int reverse_num = 0;
int orignal = num;

  while (orignal > 0)
  {
    reverse_num = reverse_num * 10 + orignal % 10;
    orignal /= 10;
  }

  if(num == reverse_num)
    return true;
  else
    return false;
}


int main()
{
     ifstream infile;
     ofstream outfile;
	 infile.open ("C-small-attempt0.in");
	 outfile.open ("output_file.in");
	 string T;
	 getline(infile,T);
	 stringstream buffer(T);
	 int X;
	 string line;
	 buffer >> X;

    for (int i=1 ;i<=X ;i++)
    {
            getline(infile,line);
            int array_num[2];

            char * cstr, *string_num;
            cstr = new char [line.size()+1];
            strcpy (cstr, line.c_str());
            string_num=strtok (cstr," ");
            int counter=0;
            int c=0;

                       while (string_num!=NULL) {
                             stringstream buffer_num(string_num);
                        buffer_num >> array_num[c];
                        string_num=strtok(NULL," ");
                       c++;
                      }
                      for(int j=array_num[0] ;j<=array_num[1] ;j++)
                    {
                         if(Is_palindrome(j))
                         {
                             int temp_sqr;
                             temp_sqr=Is_square(j);
                             if(temp_sqr!=-1)
                             {
                                 if(Is_palindrome(temp_sqr))
                                 {
                                     counter++;
                                 }

                             }
                         }


                    }
    outfile<<"Case #"<<i<<": "<<counter<<endl;

    }
    return 0;
}
