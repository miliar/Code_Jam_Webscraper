#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <cmath>

using namespace std;

int isPalindrom(int x)
{
    int num = x;
    int n = num;
    int reverse = 0;
    int dig;
    while (num > 0)
    {
      dig = num % 10;
      reverse = reverse * 10 + dig;
      num = num / 10;
    }
    return (n==reverse);
}

int isIt(int x)
{
    if (isPalindrom(x))
    {
        int root = sqrt(x);
        if (root*root == x)
        {
            return isPalindrom(root);
        }
    }
    return 0;
}

int broj(int A,int B)
{
    int count = 0;
    for (int i = A; i <= B; ++i)
    {
        if (isIt(i))
        {
            count++;
        }
    }
    return count;
}

int main(int argc, char **argv )
{
	int number_of_lines;
    string filename(argv[1]);
    string line;
    int A,B;
    ifstream myfile(filename.c_str());
    ofstream myfileOut("output.out");
    if (myfile.is_open()&&myfileOut.is_open()) 
    {
        //first read the number of lines
        getline (myfile,line);
        number_of_lines = atoi(line.c_str());
        //make vector of vectors
        // vector< list<int> > cases(number_of_lines);
        //go for all lines and translate to Googlerese
        // std::list<int> list;
		for (int i=0; i<number_of_lines; i++) 
            {
            	
            	// list.clear();
            		getline (myfile,line);
                	sscanf (line.c_str(),"%d %d",&A,&B);
                    myfileOut << "Case #"<<i+1<<": "<<broj(A,B)<<endl;
            	// cases[i]=list;
                // getline (myfile,line);
                // myfileOut << "Case #"<<i+1<<": "<< line<<endl;
            }
        myfile.close();
        myfileOut.close();
    }
    

	     
        
    return 0;
}