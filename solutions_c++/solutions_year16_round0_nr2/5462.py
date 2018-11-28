#include <iostream>

using namespace std;


long long int insol(char inp[],int lo, int hi)
{
  if(lo==hi)
    {
      if(inp[lo]=='+')
	return 0;
      else
	return 1;
    }  
  int i=lo;
  char first=inp[i];
  while(((i+1)<=hi) && (inp[i+1]==first))
    {
      i++;      
    }
  if(i==hi)
    {
      if(first=='+')
	return 0;
      else
	return 1;
    }  
  return 1+insol(inp, i+1, hi);
}
void solve(char inp[])
{
  int len=strlen(inp);
  cout << insol(inp, 0, len-1) << "\n";
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen ("myfilebigone22.txt","w",stdout);
  int t;
  cin >> t;
  char inp[102];
  for(int i=0;i<t;i++)
    {
      scanf("%s",inp);
      printf("Case #%d: ", i+1);
      solve(inp);
    }
  return 0;
}
