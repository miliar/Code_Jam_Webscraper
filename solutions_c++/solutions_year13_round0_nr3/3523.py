#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;

class file_op
{
    int case_no;
    ifstream infile ;
    ofstream outfile;
    void write_file(string);
    int opr(int,int);
    int pali(vector<int>);
    
public:
    void read_file();
    
};



void file_op::read_file()
{
    
    string line;

    int i=0;
    int result;
    
    infile.open ("/Downloads/Input.in");
    outfile.open("/Downloads/Output.in");
    
    if (infile.is_open())
    {
        getline (infile,line);
        case_no=  atoi(line.c_str());
        //i++;
        for(i=0;i<case_no;i++)
        {
            int up=0,low=0;
            getline (infile,line);
            low=atoi((string(strtok((char *)line.c_str(), " "))).c_str());
            up=atoi((string(strtok(NULL, " "))).c_str());
            result=opr( floor(sqrt(up)),ceil(sqrt(low)));
            write_file("Case #"+ to_string(i+1) +": "+to_string(result)+"\n");
    
        }
        
        
    }
    else
    {
        cout << "Unable to open input file";
        
    }
    
    cout<<"\nDone!";
    infile.close();
    outfile.close();
    
}

int file_op::opr(int up, int low )
{
    int r=0;
    vector<int> n;
   
    for (int x=low;x<=up;x++)
    {
        n.clear();
        int n1=x;
        while(n1)
        {
            n.insert(n.end(), n1%10);
            n1=n1/10;
        }
        if(pali(n)==1)
        {
            n.clear();
            n1=x*x;
            while(n1)
            {
                n.insert(n.end(), n1%10);
                n1=n1/10;
            }
            if(pali(n)==1)
            {
                r++;
            }
            
        }
    }
    
    return r;
}

int file_op::pali(vector<int> n )
{
    int y=(int)n.size();
    int f_half=0,l_half=0;
    for(int i=0;i<floor(y/2);i++)
    {
        f_half+=n[i];
        l_half+=n[n.size()-i-1];
    }
    if(f_half==l_half)
    {
        return 1;
    }
    else
        return 0;
}

void file_op::write_file(string s)
{
    if (outfile.is_open())
    {
        outfile<<s;
        
    }
    else
    {
        cout << "Unable to open file";
        
    }
}

int main(int argc, const char * argv[])
{
    string s;
    file_op f;
    f.read_file();
    return 0;
}


