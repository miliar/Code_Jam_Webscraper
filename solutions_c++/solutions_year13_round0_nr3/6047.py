

#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
#include <math.h>

        using namespace std;
ofstream myfile;
char str[100];

bool isPalindrome(long num) {
 int i,j;
itoa(num,str,10);
for(i = 0,j =(strlen(str)-1); i<(strlen(str)/2);i++,j--)
{
if((str[i] )!= (str[j]))
{
return false;
}
}
return true;


  }

int main(){


        myfile.open("progout.txt");





string line;int numCases;

ifstream inputFile;
inputFile.open("C:\\Dev-Cpp\\bin\\codejam\\C-small-attempt0.in");
//(0): A-very-small.in    //(1): A-small-practice.in    //(2): A-large-practice.in
if(!inputFile.is_open()){
        myfile<<"ERROR: invalid file"<<endl;
myfile.close();
return(-1);
}


        getline(inputFile,line);
numCases=atoi(line.c_str());

for(int c=0;c<numCases;c++){
  int count=0;
        getline(inputFile,line);
if (line.empty()) {
        getline(inputFile,line);
}
        string cppstart= line.substr(0, line.find(" ")) ;
string cppend =line.substr( line.find(" ")+1,line.length()-1) ;

long    start=atoi(cppstart.c_str());
long   end=atoi(cppend.c_str());


   long  startSquareRoot=ceil(sqrt(start));
long  endSquareRoot=floor(sqrt(end));

for (long i=startSquareRoot;i<=endSquareRoot;i++)   {



                if (isPalindrome(i)  && isPalindrome(i*i) ){


                count+=1;

        }


        }


myfile<<"Case #"<<(c+1)<<": "<< count<<endl;


} //end for each test case

        return 0;
myfile.close();
} //end main










