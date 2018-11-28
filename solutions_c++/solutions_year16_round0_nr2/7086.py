#include<iostream>
#include<fstream>


using namespace std;


int fip(int s[], int po,int need)
{
    if(po == 0)
    {
      if(need != s[po])
      {
    
         return 1;
      }
      else return 0;
    }
    else 
    {
       int same = 0;
       for(int i = 0;i < po;i++)
       {
          if(s[i] != s[po])same = 1;
       }
    
       if(same == 1)
       {
               if(need != s[po])return fip(s,po -1,s[po]) + 1;
               else return fip(s,po - 1,s[po]);
       }
       else
       {
               if(need != s[po])return  1;
               else return 0;           
       }
    
    }
}



int main()
{
    ifstream fin("B.in");
    ofstream fout("O.txt"); 
    int T,counter= 0;
    fin >> T;
    while(counter != T)
    {
        string s;
        
        fin >> s;
         
        int ints[s.length()];
        
        for(int i =0; i < s.length(); i++)
        {
                if(s[i] == '+')ints[i] = 1;
                else ints[i] = 0;
        }
       
        
        fout << "Case #" << (counter++) + 1 << ": " <<  fip(ints,s.length() - 1, 1) << endl;

    }
    
    
    
    
    
    system("pause");
}
