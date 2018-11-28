


#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include<iomanip>
#include <math.h>

using namespace std;

class file_op
{
    int case_no;
    ifstream infile ;
    ofstream outfile;
    void write_file(string);
    int opr(vector<long long int>,long long int);
    
    
public:
    void read_file();
    
};



void file_op::read_file()
{
    
    string line;
    
    //Variables final_line,med_line;
    int i=0;
    
    
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
                vector <long long int> a_sz;
                long long int armin_sz=0,other_mot=0;
                int result=0;
                armin_sz=atoi((string(strtok((char *)line.c_str(), " "))).c_str());
                other_mot=atoi((string(strtok(NULL, " "))).c_str());
                getline (infile,line);
                a_sz.push_back(atoi((string(strtok((char *)line.c_str(), " "))).c_str()));

                for(int r=1;r<other_mot;r++)
                {
                    a_sz.push_back(atoi((string(strtok(NULL, " "))).c_str()));

                }
                
                long long int temp;
                for(int j=0;j<a_sz.size();j++)
                {
                    for(int i=0;i<a_sz.size()-1;i++)
                    {
                        if(a_sz[i]>a_sz[i+1])
                        {
                            temp=a_sz[i];
                            a_sz.erase(a_sz.begin()+i);
                            a_sz.insert(a_sz.begin()+i+1,temp);
                            
                        }
                    }
                }
                result=opr(a_sz,armin_sz);
                write_file("Case #"+ to_string(i) +": "+to_string(result)+"\n");
              /*  cout<<armin_sz<<endl;
                for(int k=0;k<a_sz.size();k++)
                {
                    cout<<a_sz[k]<<" ";
                }
                cout<<endl;
                
                
                cout<<result<<endl<<endl;*/
                
                /*   string print;
                 print="Case #"+ to_string(i) +": ";
                 for(int s=0;s<contestants;s++)
                 {
                 print= print+to_string(result[s])+" ";
                 }
                 write_file(print+"\n");
                 */
                
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

int file_op::opr(vector<long long int> a_sz,long long int armin_sz )
{
    
    int add=0,rem=0, mem=0, min=0;
    vector <int> steps_m;
    
    while(a_sz.size()!=0)
    {
        if(armin_sz>a_sz[0])
        {
            armin_sz+=a_sz[0];
            a_sz.erase(a_sz.begin()+0);
        }
        else if((2*armin_sz - 1)>a_sz[0])
        {
            armin_sz=2*armin_sz - 1;
            add++;
            armin_sz+=a_sz[0];
            a_sz.erase(a_sz.begin()+0);
            
        }
        else if((2*armin_sz - 1)<=a_sz[0])
        {
            
            if(armin_sz>1)
            {
                mem=add+rem+a_sz.size();
                steps_m.push_back(mem);
            
            int steps = 0;
            steps=floor(log2((double)((a_sz[0]-1)/(armin_sz-1))));
            steps=steps+1;
            if(steps<=a_sz.size())
            {
               
                armin_sz=2*armin_sz - 1;
                add++;
            }
            else{
                a_sz.erase(a_sz.begin()+0);
                rem++;
            }
            }
            else{
                a_sz.erase(a_sz.begin()+0);
                rem++;
            }
            
            
        }
        
    }
    
    min=add+rem;
    if(steps_m.size()!=0)
    {
    
        for(int i=0;i<steps_m.size();i++)
        {
            if (min>steps_m[i])
            {
                min=steps_m[i];
            }
        }
    }
    
    return (min);

    
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





