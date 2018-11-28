#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <vector>
using namespace std;

class file_op
{
    int case_no;
    ifstream infile ;
    ofstream outfile;
    void write_file(string);
    int opr(vector<vector <int> >);
    
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
  
        for(i=0;i<case_no;i++)
        {
           
            getline (infile,line);
            int n=0,m=0,l=0;
            string s;
            n=atoi(string(strtok((char *)line.c_str(), " ")).c_str());
            m=atoi(string(strtok(NULL, " ")).c_str());

            vector<vector <int> > args;
            for(int s=0;s<n;s++)
            {
                vector<int> row;
                args.push_back(row);
            }
            
            do
            {

                getline (infile,line);
                args[l].push_back(atoi(string(strtok((char *)line.c_str(), " ")).c_str()));
              
                
                for(int x=1;x<m;x++)
                {
                   args[l].push_back(atoi(string(strtok(NULL, " ")).c_str()));
                   
                }
                
                ++l;
            }while(l<n);
          
            cout<<i<<" "<<n<<" "<<m<<endl;
            for(int row=0;row<n;row++)
            {
                for (int col=0;col<m;col++)
                {
                    cout<<args[row][col]<<" ";
                    
                }
                cout<<endl;
            }

            result=opr(args);
            cout<<result;
            cout<<endl<<endl;
           cout<<endl<<endl;
            if(result==1)
            {
                write_file("Case #"+ to_string(i+1)+": YES\n");

            }
            else
            {
                write_file("Case #"+ to_string(i+1)+": NO\n");
            }
      
            
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

int file_op::opr(vector<vector <int> > args)
{
    int min=-1;
    vector<vector<int>>::iterator it;
    
    while(args.size()>1 && args[0].size()>1)
    {     
        vector<int> x=*(min_element(args.begin(),args.end()));
        min=*(min_element(x.begin(),x.end()));
        
        for(int i=0;i<args.size();i++)
        {
            for(int j=0;j<args[0].size();j++)
            {
                if(args[i][j]==min)
                {
                    if(i!=0 && j!=0)
                    {
                        return 0;
                    }
                    else
                    {
                        if(i==0 && j==0)
                        {
                            int flag=0;
                            for(int t=0;t<args[0].size();t++)
                            {
                                if(args[i][t]!=min)
                                {
                                    for(int t=0;t<args.size();t++)
                                    {
                                        if(args[t][j]!=min)
                                        {
                                            return 0;
                                        }
                                        
                                        
                                    }
                                    flag=1;
                                    
                                    for(int c=0;c<args.size();c++)
                                    {
                                        args[c].erase(args[c].begin()+j);   
                                        
                                    }
                                    i=(int)args.size()+1;
                                    j=(int)args[0].size();
                                    break;
                                }
                                
                            }
                            if(flag==0)
                            {
                                args.erase(args.begin()+i);
                               
                            }
                            
                            if(args.size()< 2 || args[0].size()< 2)
                            {
                                return 1;
                            }
                            i=(int)args.size()+1;
                            j=(int)args[0].size();

                        }
                        else if(i==0 && j!=0)
                        {
                            
                            for(int t=0;t<args.size();t++)
                            {
                               if(args[t][j]!=min)
                               {
                                   return 0;
                               }
                                
                            }
                            for(int c=0;c<args.size();c++)
                            {
                                args[c].erase(args[c].begin()+j);
                                
                                
                            }
                            if(args.size()< 2 || args[0].size()< 2)
                            {
                                return 1;
                            }
                            i=(int)args.size()+1;
                            j=(int)args[0].size();
                            
                        }
                        else 
                        {
                            for(int t=0;t<args[0].size();t++)
                            {
                                if(args[i][t]!=min)
                                {
                                    return 0;
                                }
                                
                            }
                            
                            args.erase(args.begin()+i);
                            if(args.size()< 2 || args[0].size()< 2)
                            {
                                return 1;
                            }
                            i=(int)args.size()+1;
                            j=(int)args[0].size();

                        }
                        
                    }
                }
            }
        
        }
    }
    return 1;
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


