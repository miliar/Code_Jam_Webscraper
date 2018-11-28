#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int process_case(vector<string> s, int out)
{
    int pos = 1+ (out*10);
    int row_1;
    int row_2;
    int a[4];
    int b[4];
    
    row_1 = stoi(s[pos]);
    row_2 = stoi(s[pos+5]);
    
    string input_1 = s[pos+row_1];
    istringstream(input_1) >> a[0] >> a[1] >> a[2] >> a[3];
    
    input_1 = s[pos+5+row_2];
    istringstream(input_1) >> b[0] >> b[1] >> b[2] >> b[3];
    
    int count = 0;
    int number = 0;
    for (int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            if (a[i] == b[j])
            {
                count++;
                number = a[i];
            }
        }
    }
    
    if(!count)
    {
        cout<<"Case #"<<out+1<<": Volunteer cheated!\n";
    }
    else if (count == 1)
    {
        cout<<"Case #"<<out+1<<": "<<number<<endl;
    }
    else
    {
        cout<<"Case #"<<out+1<<": Bad magician!\n";
    }
    return 0;
    
}
int main(int argc, char *argv[]) 
{
    
    string line;
    vector <string> s;
    ifstream myfile;
    myfile.open ("input.txt");
    if (myfile.is_open())
    {
        while (true) 
        {
            getline(myfile, line);
        //  getline(cin, line);
                
            if (line.empty())
            {
                    break;
            }
            else
            {
                s.push_back(line);
            }
        }
    }
    else
    {
        cout<<"siva unable to open the file"<<endl;
    }
    
    int num_case = stoi(s[0]);
    
    for (int i =0 ; i< num_case; i++)
    {
        process_case(s,i);
    }
    
   return 0;
}