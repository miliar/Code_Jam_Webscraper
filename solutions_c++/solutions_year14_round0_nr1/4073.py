#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>

using namespace std;

class file_op
{
    
    ifstream infile;
    ofstream outfile;
    
public:
    bool isopen;
    vector<int> fileread();
    void closefiles();
    void filewrite(string);
    
};

int main(int argc, const char * argv[])
{
    file_op f;
    f.isopen=false;
    //vector<long long> result;
    vector<int> op=f.fileread();
    int case_no=op[0];
    // insert code here...
    for(int i=0;i<case_no;i++)
    {
        int first_row=f.fileread()[0];
        vector<int> first_row_data;
        for(int i=0;i<4;i++)
        {
            vector<int> x=f.fileread();
            if(i==(first_row-1))
            {
                first_row_data=x;
            }
        }
        
        int second_row=f.fileread()[0];
        vector<int> second_row_data;
        for(int i=0;i<4;i++)
        {
            vector<int> x=f.fileread();
            if(i==(second_row-1))
            {
                second_row_data=x;
            }
        }
        int count=0;
        int pos;
        
        for ( int k=0;k<first_row_data.size();k++)
        {
        
            for (int l=0;l<second_row_data.size();l++)
            {
                if(first_row_data[k]==second_row_data[l])
                {
                    ++count;
                    pos=k;
                }
                
            }
        }
        
        switch(count)
        {
            case 0: cout<<"Case #"+to_string(i+1)+": "+"Volunteer cheated!\n";
                f.filewrite("Case #"+to_string(i+1)+": "+"Volunteer cheated!\n");
                break;
                
            case 1:cout<<"Case #"+to_string(i+1)+": "+to_string(first_row_data[pos])+"\n";
                f.filewrite("Case #"+to_string(i+1)+": "+to_string(first_row_data[pos])+"\n");
                break;
                
            default:cout<<"Case #"+to_string(i+1)+": "+"Bad magician!"+"\n";
                f.filewrite("Case #"+to_string(i+1)+": "+"Bad magician!"+"\n");
                break;
        }
        
        
    }
           return 0;
        
}


vector<int> file_op::fileread()
{
    vector<int> ret;
    string line;
    char* ch;
    if(!(isopen))
    {
        infile.open ("/Users/tusharsingh/Documents/Tushar/workspace/Input.in");
        isopen=true;
    }
    
    getline(infile,line);
    ret.push_back(atoi((string(strtok((char *)line.c_str(), " "))).c_str()));
    ch=strtok (NULL, " ");
    while(ch!=NULL)
    {
        ret.push_back(atoi((string(ch)).c_str()));
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



