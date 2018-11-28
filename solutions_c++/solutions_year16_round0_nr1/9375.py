#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<bool> arr(10,0);
bool missionComplete = false ;
void lenght (long long x)
{
  while(x!=0)
  {
      arr[x%10]=true ;
  // cout<< x% 10 <<endl;
      x/=10;
  }
   int res =0;
   for(int i=0 ;i<10;i++)
      res+= arr[i];
   missionComplete=(res==10)? 1 : 0;
}

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int n ,testCase , number ;fin>>testCase;
    number = testCase ;
    while(testCase--)
    {
     fin >>n ;
     for(int i=1;i<1000000;i++)
        if(missionComplete||n==0)
     {
         if(n!=0)
         fout<<"Case #"<<number-testCase<<": "<<n*(i-1)<<endl;
         else
            fout <<"Case #"<<number-testCase<<": "<<"INSOMNIA"<<endl;

         vector<bool> ar(10,0) ;
         arr=ar ;
         missionComplete =0 ;
         break ;
     }
     else
        lenght(n*i);
    }
    fin.close();
    fout.close();
    return 0;
}
