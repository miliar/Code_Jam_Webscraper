#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

vector<string> solve_A(vector<string> &inputs)
{
   vector<string> s;
   int case_n = 1;
   int N = stoi(inputs[0]);
   for(vector<string>::iterator it=inputs.begin()+1;it<inputs.end();it++)
   {
       int idx=0;
       string tmp_s = *it;
       for(int i=0;i<tmp_s.size();i++)
       {
           if(tmp_s[i]==' ')
           {
               idx=i;
               break;
           }
       }
       int max_val = stoi(tmp_s.substr(0,idx));
       
       int total=0;
       int needed=0;
       for(int i=idx+1;i<tmp_s.size();i++)
       {
          total+=stoi(tmp_s.substr(i,1));
          needed = max(needed, i-idx-1)+stoi(tmp_s.substr(i,1));
       }
       
      s.push_back( "Case #" + to_string( case_n ) + ": " + to_string(needed-total));
      case_n++;
   }
   return s;
}

int main()
{
   vector<string> inputs;
   
   ifstream i_file;
   i_file.open ("inputs/small.in",ios::in);
   string line;
   if (i_file.is_open())
   {
      while ( getline (i_file,line) )
      {
         inputs.push_back(line);
      }
      i_file.close();
   }
  
   vector<string> results;
   
   results = solve_A(inputs);
   
   ofstream o_file;
   o_file.open ("inputs/small.out",ios::out);
   for(vector<string>::iterator it=results.begin();it<results.end();it++)
   {
      o_file << *it;
      if(it+1<results.end())
      {
          o_file << endl;
      }
   }
   o_file.close();
  
   return 0;
}