#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<string>
#include<sstream>

using namespace std;

int palindrome(string num)
{
  int len = num.size();
  int i,j;
  for(i=0, j=len-1; i<len && i<j; i++, j--)
    if(num[i] != num[j])  return 0;
  return 1;
}

string tostring(double num)
{
  ostringstream s;
  s<<num;
  return s.str();
}
int main()
{
  int tcases;
  long double down, up, sqdown, squp, temp, it, sze, sqrs[1000], tpal;
  unsigned long long pl, print;
  cin>>tcases;
  print = 1;
  while(tcases--)
  {
    cout<<"Case #"<<print<<": ";
    print++;
    temp=tpal=0;
    cin>>down>>up;
    sqdown = sqrt(down);
    sqdown = ceil(sqdown);
    squp = sqrt(up);
    squp = floor(squp);
    sze = squp-sqdown+1;
    //sqrs = new double[sze];
    //sqrs = (long double *) malloc(sze);
    for(pl=0,it=sqdown;it<=squp;it++)
    {
      if(palindrome(tostring(it)))
      {
       sqrs[pl] = it*it;
       temp++;
       pl++;
      }
    }
    for(pl=0;pl<temp;pl++)
    {
      if(palindrome(tostring(sqrs[pl])))
        tpal++;
    }
    cout<<tpal<<endl;
  }
  return 0;
}
