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
    setprecision(5);
    for(int i=0;i<case_no;i++)
    {
        int N=atoi(f.fileread()[0].c_str());
        vector<string> s=f.fileread();
        vector<long double> naomi;
        for(int i=0;i<N;i++)
        {
            naomi.push_back(atof(s[i].c_str()));
        }
        vector<string> r=f.fileread();
        vector<long double> ken;
        for(int i=0;i<N;i++)
        {
            ken.push_back(atof(r[i].c_str()));
        }
        
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        int deciet_win=0,natural_win=0;
        int freeze=0;
        for(int i=0;i<N;i++)
        {
            for(int j=freeze;j<N;j++)
            {
                
                if(naomi[j]>ken[i])
                {
                    ++deciet_win;
                    freeze=j+1;
                    break;
                }
                
            }
        }
        freeze=0;
        for(int i=0;i<N;i++)
        {
            for(int j=freeze;j<N;j++)
            {
                
                if(ken[j]>naomi[i])
                {
                    ++natural_win;
                    freeze=j+1;
                    break;
                }
                
            }
        }
        
        f.filewrite("Case #"+to_string(i+1)+": "+to_string(deciet_win)+" "+to_string(N-natural_win)+"\n");
        
       /* cout<<"\n"<<deciet_win<<" "<<(N-natural_win)<<"\n";
        
        
        for(int i=0;i<N;i++)
        {
         cout<<naomi[i]<<" ";
        }
        cout<<"\n";
        for(int i=0;i<N;i++)
        {
            cout<<ken[i]<<" ";
        }
        cout<<"\n";*/
        /*long double max_ken=ken[0];
        long double min_ken=ken[0];
        long double max_naomi=naomi[0];
        long double min_naomi=naomi[0];
        
        for(int i=0;i<N;i++)
        {
            if(max_ken<ken[i])
            {
                max_ken=ken[i];
            }
            if(min_ken>ken[i])
            {
                min_ken=ken[i];
            }
            if(max_naomi<naomi[i])
            {
                max_naomi=naomi[i];
            }
            if(min_naomi>naomi[i])
            {
                min_naomi=naomi[i];
            }
        }
       // cout<<max<<" "<<min<<"\n";
        int low_naomi=0,high_naomi=0,low_ken=0,high_ken=0;;
        for(int i=0;i<N;i++)
        {
            if(naomi[i]<min_ken)
            {
                ++low_naomi;
            }
            if(naomi[i]>max_ken)
            {
                ++high_naomi;
            }
            if(ken[i]>max_naomi)
            {
                high_ken++;
            }
            
        }
        
        cout<<N-low_naomi<<" "<<high_naomi<<"\n";*/
        

    
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



