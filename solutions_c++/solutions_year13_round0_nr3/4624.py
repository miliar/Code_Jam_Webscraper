#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <bitset>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <functional>
#include <utility>
#include <ctime>
#include <numeric>
#include <iomanip>
#include <stdexcept>
#include <cmath>
#include <algorithm>



using namespace std;

#define LINT long long


int PLD(LINT num)
{
  LINT temp = num;
  std::string str, rev;
  int i =0;
  //cout<<"PLd : "<<num<<endl;
  while(temp)
  {
     char ch = (temp%10)+48;
//     cout<<ch<<endl;
     str.push_back(ch);
     rev.insert(rev.begin(),ch);
     temp  = temp/10;
  }
  
//  cout<<str.c_str()<<"   "<<rev.c_str()<<endl;
  if(str.compare(rev) == 0)
  {
    
     return 1;
  }

  return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
  
int T;
cin>>T;
LINT A, B;
int  CNT = 0;

for(int k = 0; k<T; k++)
{
   cin>>A>>B;
//   cout<<A<<" "<<B<<endl;
   CNT = 0;
   LINT x, sqX;
   double H = (double)A;
  // cout<<H<<endl;
   double sqrtA = sqrt(H);
//   cout<<sqrtA<<endl;
   x = (LINT)sqrtA;
   
   sqX = x*x;
   x = sqX==A?x:x+1;
   sqX = x*x;
//   cout<<x<<endl;
   
   while(sqX <= B)
   {
  //   cout<<"sqX : "<<sqX<<endl;
     if(PLD(sqX) == 1)
     {
        if(PLD(x) == 1)
        {
    //       cout<<x<<endl;
           CNT++;
        }
     }
     
     x = x+1;
     sqX = x*x;
     
   }
   cout<<"Case #"<<k+1<<": "<<CNT<<endl;
} 


int y ;
cin>>y;

  return 0;
	}

