


#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include<iomanip>

using namespace std;

class file_op
{
    int case_no;
    ifstream infile ;
    ofstream outfile;
    void write_file(string);
    long long int opr(long long int,long long int);
    
    
public:
    void read_file();
    
};



void file_op::read_file()
{
    
    string line;
    
    //Variables final_line,med_line;
    int i=0;
    vector <double> result;
    
    infile.open ("/Downloads/Input.in");
    outfile.open("/Downloads/Output.in");
    if (infile.is_open())
    {
        
        while (getline (infile,line))
        {
            
            if (i==0)
            {
                case_no=  atoi(line.c_str());
                i++;
                
            }
            
            else
            {
                
                // line parameters
                //logic to get the number of enteries per case, can be avoided
                vector <int> a;
                
                long long int r=0,t=0,result;
                r=atoll((string(strtok((char *)line.c_str(), " "))).c_str());
                t=atoll((string(strtok(NULL, " "))).c_str());
                result=opr(r,t);

                 write_file("Case #"+ to_string(i) +": "+to_string(result)+"\n");
                 
                
                i=i+1;
                
            }//end of else
            
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

long long int file_op::opr(long long int r,long long int t )
{
    
    long long int result=0;
    long long int i=r;
    long long int req=((i+1)*(i+1))-(i*i);
    t=t-req;
    while(t>=0)
    {
        result++;
        i=i+2;
        req=((i+1)*(i+1))-(i*i);
        t=t-req;
        
    }
    return result;
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





