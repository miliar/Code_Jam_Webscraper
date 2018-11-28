#include<vector>
#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
  int num_cases;
  int s_max;
  char t;

  vector<int> s(1001);
  scanf("%d",&num_cases);

  for(int nc=1;nc<=num_cases;nc++)
  {
    int orthioi=0;
    int news=0;
    scanf("%d",&s_max);
    scanf("%c",&t);
    for(int i=0;i<s_max+1;i++)
    {
      scanf("%c",&t);
      s[i]=t-'0';
    }
    scanf("%c",&t);
    orthioi=s[0];
    for(int i=1;i<s_max+1;i++)
    {
     /* cout<<"i: "<<i<<"|s[i] "<<s[i]<<endl;
      cout<<"orthioi"<<orthioi<<endl;
      cout<<"news"<<news<<endl;*/
      if(orthioi>=i)
      {
	orthioi+=s[i];
      }
      else if(s[i]>0)
      {
	news+=i-orthioi;
	orthioi+=s[i]+i-orthioi;
      }
    }
    printf("Case #%d: %d\n",nc,news);
  }
}
