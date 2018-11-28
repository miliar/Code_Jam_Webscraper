#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
#include <iomanip>   

using namespace std;

class file_op
{
    
    ifstream infile;
    ofstream outfile;
    
public:
    bool isopen;
    vector<string> fileread();
    void closefiles();
    void filewrite(string);
    
};

int main(int argc, const char * argv[])
{
    file_op f;
    f.isopen=false;
    //vector<long long> result;
    vector<string> op=f.fileread();
    int case_no=atoi(op[0].c_str());
    // insert code here...
    setprecision(7);
    for(int i=0;i<case_no;i++)
    {
        long double cookies=2.0000000;
        vector<string> times=f.fileread();
        long double max_time=atof(times[2].c_str())/cookies;
        long double time_buy=0.0000000, new_time_test=0.0000000;
        do
        {
            
            time_buy+=atof(times[0].c_str())/cookies;
            cookies+=atof(times[1].c_str());
            new_time_test=atof(times[2].c_str())/cookies+time_buy;
            if(max_time>(new_time_test))
            {
                max_time=(new_time_test);
                //time_buy=max_time;
            }
        }while(max_time>=new_time_test);
        cout<<fixed<<setprecision(7);
        f.filewrite("Case #"+to_string(i+1)+": "+to_string(max_time)+"\n");
        //cout<<fixed<<setprecision(7)<<max_time<<"\n";
        
    }
    return 0;
    
}


vector<string> file_op::fileread()
{
    vector<string> ret;
    string line;
    char* ch;
    if(!(isopen))
    {
        infile.open ("/Users/tusharsingh/Documents/Tushar/workspace/Input.in");
        isopen=true;
    }
    
    getline(infile,line);
    ret.push_back(((string(strtok((char *)line.c_str(), " "))).c_str()));
    ch=strtok (NULL, " ");
    while(ch!=NULL)
    {
        ret.push_back(((string(ch)).c_str()));
        ch=strtok (NULL, " ");
    }
    
    return ret;
}


void file_op::closefiles()
{
    infile.close();
    outfile.close();
}

void file_op::filewrite(string s)
{
    
    
    if (!(outfile.is_open()))
    {
        outfile.open ("/Users/tusharsingh/Documents/Tushar/workspace/Output.in");
    }
    outfile<<s;
    
    
}



