#include <cstdio>
#include <cassert>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <utility>
#include <cinttypes>

int ind(char c)
{
  return (int)c-(int)'A';
}

void check(int thenumber,
           char c,std::string also, std::vector<int>& num, std::vector<int>& res)
{
/*  for (int i=0;i<'Z'-'A'+1;++i)
  {
    if ( num[i] )
      printf("%c%d",'A'+i,num[i]);
  }
  printf("\n");*/
  while ( num[ind(c)] > 0 )
  {
//    printf("%d-",thenumber);
    --num[ind(c)];
    for ( char x:also)
    {
      assert(num[ind(x)]>0);
      --num[ind(x)];
    }
    ++res[thenumber];
  }
}

void solve(std::string s)
{
//  printf("%s\n",s.c_str());
  std::vector<int> num;
  num.resize( 'Z'-'A' + 1 );
  std::vector<int> res(10);
  for ( char a: s)
    ++num[ind(a)];

  //0
  check(0,'Z',"ERO",num,res);
  check(2,'W',"TO",num,res);
  check(4,'U',"FOR",num,res);
  check(6,'X',"SI",num,res);
  check(8,'G',"EIHT",num,res);

  check(5,'F',"IVE",num,res);

  check(1,'O',"NE",num,res);

  check(7,'V',"SEEN",num,res);

  check(3,'T',"HREE",num,res);

  check(9,'N',"INE",num,res);

  for (int i=0;i<res.size();++i)
  {
    while (res[i]--)
      printf("%d",i);
  }

}

int main(int arng, char**argv)
{
  int ncase;
  scanf("%d",&ncase);
  for (int icase=0;icase<ncase;++icase)
  {
    char s[2001];
    scanf("%2000s",s);
    printf("Case #%d: ",icase+1);
    solve(s);
    printf("\n");
  }
  return 0;
}
