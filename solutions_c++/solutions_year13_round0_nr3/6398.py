#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;
int explode(string str, string delim, string *result);
int reverse(int n);
int main(int argc, char **argv)
{
    char temp[1024];
    int testCases = 0;
    string board[4][4];
    ifstream iFile("C-small-attempt0.in");
    ofstream output("out.txt");
    string message = "";
    if(iFile.fail())
    {
        cout<<"Unable to open input file!"<<endl;
        exit(1);
    }
   
    iFile.getline(temp, 1024);
    testCases = atoi(temp);
    int min = 0, max = 0;
    for(int i=0; testCases > i; ++i)
    {
        iFile.getline(temp, 1024);
        string input(temp);
        string range[2];
        explode(input, " ", range);
        min = atoi(range[0].c_str());
        max = atoi(range[1].c_str());
        //cout<<min<<"-"<<max<<endl;
        int num = 0, total = 0;
        for (int j = min; max >= j; ++j)
        {
            stringstream s;
            num = j;
            s<<num;
            string source (s.str());
            s.str("");
            s<<reverse(num);
            string dest (s.str());
            if(dest != source)
                continue;
                
            num = (int) sqrt(num);
            if((num * num) != j)
                continue;
            s.str("");
            s<<num;
            source = s.str();
            s.str("");
            s<<reverse(num);
            dest = s.str();
            if(source == dest)
                total++;
        }
        output<<"Case #"<<i+1<<": "<<total<<endl;
        //break;
    }
    
    output.close();
    
    
    return 0;
}

int reverse(int n)
{
    int rev = 0;
    int num = n;
    while(num)
    {
        rev = rev*10 + num%10;
        num/=10;
    }
    return rev;
}

int explode(string str, string delim, string *result)
{
    char *token;
    char cStr[1024];
    int i = 0;
    strcpy(cStr, str.c_str());
    
    token = strtok(cStr, delim.c_str());
    while(token!=NULL)
    {
        result[i++] = token;
        token = strtok(NULL, delim.c_str());
    }
    return i;
}
