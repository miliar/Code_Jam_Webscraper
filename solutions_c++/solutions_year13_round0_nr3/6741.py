#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;

bool palin(int x)
{
     char str[33];
     itoa(x, str, 10);
     int size = strlen(str);
     for (int i = 0; i < (size + 1)/2; i++)
     {
         if (str[i] != str[size - 1 - i])
            return false;
     }
     return true;
}

int get_square(int a, int b)
{
    int result = 0;
    for (int i = a; i <=b; i++)
    {
        int tmp = (int)sqrt(i);
        if (palin(i) && palin(tmp) && (tmp*tmp)==i )
        {
           result++;
        }
    }
    return result;
}


int main()
{
    std::ifstream infile("C-small-attempt1.in");
    std::string line;
    string num;
    std::getline(infile, num);
    int nums = atoi(num.c_str());
    ofstream outfile;
    outfile.open("output.txt");
    int counter = 0;
    while (std::getline(infile, line))
    {
          std::istringstream iss(line);
          int a, b;
          if (!(iss>>a>>b)) {break;}
          counter++;
          int out = get_square(a, b);
          cout<<"Case #"<<counter<<": "<<out<<endl; 
          outfile<<"Case #"<<counter<<": "<<out<<endl;
    }
    system("pause");
 //   return 0;
}
