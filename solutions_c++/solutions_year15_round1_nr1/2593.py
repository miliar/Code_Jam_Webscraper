#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <gmpxx.h>
#include <iomanip>

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"

using namespace std;

int main()
{
    string s;
    int T;
    ifstream in;
    in.open(INPUT, ios::in);
    ofstream out;
    out.open(OUTPUT, ios::out);
    getline(in, s);
    T = stoi(s);

    for(int T_iter=1; T_iter<=T;T_iter++)
    {
        getline(in, s);
        int N = stoi(s);
        getline(in, s);
        istringstream tempA(s);
        vector<int> m((istream_iterator<int>(tempA)), istream_iterator<int>());
        int y=0, min=-1, z=0;
        for(int i=0;i<N-1;i++)
        {
            if(m[i+1]<m[i])
            {
                y+=m[i]-m[i+1];
                if(min==-1 || (m[i]-m[i+1])>min)
                    min = m[i]-m[i+1];
            }


        }
        if(min==-1||min==0)
            z=0;
        else
           {
            //if(min>10)
                int rate = min/10;
              //  min = rate*10;
           for(int i=0;i<N-1;i++)
            {
               if(m[i]<min)
                   z+=m[i];
               else
                   z+=min;
             /*  if(m[i]!=0)
               {
                   if(m[i]<min)
                   {
                       int cnt=0;
                       while(cnt<m[i])
                       {
                           cnt+=rate;
                           z+=rate;
                       }
                       if(cnt>m[i])
                           z-=rate;
                   }
                   else z+=min;
               } */
            }
        }
        out<<"Case #"<<T_iter<<": "<<y<<" "<<z<<endl;
    }
    in.close();
    out.close();
    return 0;
}

