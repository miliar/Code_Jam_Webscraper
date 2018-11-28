


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
                vector <long long int> bubbles;
                long long int armin_bubble_sz=0,other_mot=0;
                int result=0;
                armin_bubble_sz=atoi((string(strtok((char *)line.c_str(), " "))).c_str());
                other_mot=atoi((string(strtok(NULL, " "))).c_str());
                getline (infile,line);
                bubbles.push_back(atoi((string(strtok((char *)line.c_str(), " "))).c_str()));

                for(int r=1;r<other_mot;r++)
                {
                    bubbles.push_back(atoi((string(strtok(NULL, " "))).c_str()));

                }
                
                long long int temp;
                for(int j=0;j<bubbles.size();j++)
                {
                    for(int i=0;i<bubbles.size()-1;i++)
                    {
                        if(bubbles[i]>bubbles[i+1])
                        {
                            temp=bubbles[i];
                            bubbles.erase(bubbles.begin()+i);
                            bubbles.insert(bubbles.begin()+i+1,temp);
                            
                        }
                    }
                }
                result=opr(bubbles,armin_bubble_sz);
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

int file_op::opr(vector<long long int> bubbles,long long int armin_bubble_sz )
{
    
    int add_buuble=0,rem_buuble=0, mem=0, min=0;
    vector <int> steps_m;
    
    while(bubbles.size()!=0)
    {
        if(armin_bubble_sz>bubbles[0])
        {
            armin_bubble_sz+=bubbles[0];
            bubbles.erase(bubbles.begin()+0);
        }
        else if((2*armin_bubble_sz - 1)>bubbles[0])
        {
            armin_bubble_sz=2*armin_bubble_sz - 1;
            add_buuble++;
            armin_bubble_sz+=bubbles[0];
            bubbles.erase(bubbles.begin()+0);
            
        }
        else if((2*armin_bubble_sz - 1)<=bubbles[0])
        {
            
            if(armin_bubble_sz>1)
            {
                mem=add_buuble+rem_buuble+bubbles.size();
                steps_m.push_back(mem);
            
            int steps = 0;
            steps=floor(log2((double)((bubbles[0]-1)/(armin_bubble_sz-1))));
            steps=steps+1;
            if(steps<=bubbles.size())
            {
               
                armin_bubble_sz=2*armin_bubble_sz - 1;
                add_buuble++;
            }
            else{
                bubbles.erase(bubbles.begin()+0);
                rem_buuble++;
            }
            }
            else{
                bubbles.erase(bubbles.begin()+0);
                rem_buuble++;
            }
            
            
        }
        
    }
    
    min=add_buuble+rem_buuble;
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





