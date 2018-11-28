#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<algorithm>
#include<numeric>
#include<map>
#include<math.h>

using namespace::std;

int check( int frow[] , int srow[] )
{
  vector <int> ans;
  
  for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
	{
	  if(frow[i] == srow[j])
	    {
	      ans.push_back(frow[i]);
	    }
	}
    }
  int ans_s = ans.size();
  
  if(ans_s == 0)
    {
      return ans_s;
    }
  else if(ans_s >= 2)
    {
      return -1;
    }
  else
    {
      return ans[0];
    }

}

void init_row(int row[4] , int q)
{
  int num;
  
  for(int i = 1; i <= 4; i++)
    {
      for(int j = 0; j < 4; j++)
	{
	  cin >> num;
	  if(i == q)
	    {
	      row[j] = num;
	    }
	}
    }
}

int main(void)
{
  int frow[4],srow[4];
  int T;
  int fq,sq;
  cin >> T;

  for(int i = 0; i < T; i++)
    {
      cin >> fq;
      init_row(frow , fq);

      cin >> sq;
      init_row(srow , sq);

      int dsize = check(frow , srow);
      char ans_mes[24];
      memset(ans_mes , '\0' , 24);
      
      if(dsize == 0)
	{
	  sprintf(ans_mes,"%s","Volunteer cheated!");
	}
      else if(dsize == -1)
	{
	  sprintf(ans_mes,"%s","Bad magician!");
	}
      else
	{
 	  sprintf(ans_mes,"%d",dsize);
	}
      printf("Case #%d: %s\n",i+1,ans_mes);
    }

  return 0;
}
