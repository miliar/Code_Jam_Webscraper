#include<iostream>
#include <iomanip>
#include<vector>
#include<set>
#include<map>

using namespace std;
typedef vector<float> doublevec;
typedef doublevec::iterator  doubleveciter;
typedef doublevec::reverse_iterator doublevecreviter;
int main()
{
    int T;
    cin >> T;
   
    for(int n =0; n<T; ++n)
    {
       int N;
       cin >> N;
       doublevec ken, naomi;
       for(int i =0 ; i < N;++i)
       {
               float F;
               cin >> F;
               naomi.push_back(F);
       }
       for(int i =0 ; i < N;++i)
       {
               float F;
               cin >> F;
               ken.push_back(F);
       }
       sort(naomi.begin(), naomi.end());
       sort(ken.begin(), ken.end());
       
       int z =0;
       doubleveciter keniter = ken.begin();
       doubleveciter naomiiter = naomi.begin();
       for(int i=0; i< N; ++i)
       {
          while(keniter != ken.end())
          {     
              if(*keniter <*naomiiter)
              {
                ++z;          
                ++keniter;
              }
              else
              { 
                break;
              }            
          }
          if(keniter != ken.end())
          {
            ++keniter;
          }
          ++naomiiter;   
       }
       
       int y =0;
       doublevecreviter keniter1 =  ken.rbegin();
       doublevecreviter naomiiter1 = naomi.rbegin();
        naomiiter = naomi.begin();
       for(int i=0; i< N; ++i)
       {
          //cout <<"debug " <<*naomiiter1 << " "<< *keniter1 <<"\n";
          if(*naomiiter1 < *keniter1)
          {   
              ++naomiiter;
              ++keniter1; 
          } 
          else
          {
              ++y;
              ++naomiiter1;
              ++keniter1;
          }
       }
       
       cout << "Case #" <<n+1<<": "<< y <<" "<<z <<"\n"; 
    }
    
}
