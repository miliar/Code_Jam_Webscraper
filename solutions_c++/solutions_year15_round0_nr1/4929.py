#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
main()
{
     ifstream fin("audi.txt");
     ofstream fout("resultLarge.txt");
     int tt;
     fin >> tt;
     int no=1;
     while(tt--)
     {
        int Smax;
        fin >> Smax;
        string audience;
        fin >> audience;
        int total_clapped=0 , invitation=0;
        for(int i=0; i<=Smax; i++)
        {
           int persons = audience[i]-'0';
           if(total_clapped >= i)
              total_clapped += persons;
           else
           {
               invitation += i-total_clapped;
               total_clapped += i - total_clapped + persons;
           }  
        }
        fout << "Case #" << no++  << ": "<< invitation <<endl;
     }
    //system("pause"); 
}
