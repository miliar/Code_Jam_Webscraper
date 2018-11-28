#include<iostream>
#include<cstdlib>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<algorithm>
using namespace std;
#define DEBUG_FLAG 0
#define PRINT(c) (DEBUG_FLAG)?c<<endl:cout<<"";

int main()
{
  int T;
  cin >> T;
  int F,S;
  vector<int> first(4,0);
  vector<int> second(4,0);
  vector<int> useless(4,0);

  for(int i=0;i<T;i++)
  {
    cin >> F;
    for(int j=0;j<4;j++)
    {
      if(F-1==j)
      {
        cin >> first[0] >> first[1] >> first[2] >> first[3];
      }
      else
      {
        cin >> useless[0] >> useless[1] >> useless[2] >> useless[3];
      } 
    }
    cin >> S;
    for(int j=0;j<4;j++)
    {
      if(S-1==j)
      {
        cin >> second[0] >> second[1] >> second[2] >> second[3];
      }
      else
      {
        cin >> useless[0] >> useless[1] >> useless[2] >> useless[3];
      }
    }
    PRINT(cout<<first[0]<<" "<<first[1]<<" "<<first[2]<<" "<<first[3]);
    int found_no=0;
    int number;
    for(int t=0;t<4;t++)
    {
      for(int k=0;k<4;k++)
      {
        if(first[t]==second[k])
        {
          number=first[t];
          found_no++;
        }
      }
    }
    PRINT(cout<<found_no)
    if(found_no==0)
    {
      cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }
    else if(found_no==1)
    {
      cout<<"Case #"<<i+1<<": "<<number<<endl;
    }
    else
    {
      cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    }
  }
  return 0;
}
