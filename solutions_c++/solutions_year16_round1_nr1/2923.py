#include<stdio.h>
#include<string.h>
#include<deque>

using namespace std;
int main()
{

  char ch[1005],s;
  int t;
  long long n,rnd,d;
  FILE * fin, * fot;
  fin = fopen ("largeA.in","r");
  fot = fopen ("ans.out","w");
  fscanf(fin,"%d",&t);

for(int j=0;j<t;j++)
{
  deque<char> samp;
  fscanf(fin,"%s",&ch);
  samp.push_back(ch[0]);
  for(int i=1;ch[i]!='\0';i++)
  {
      if(ch[i]>=samp.front())
      {
          samp.push_front(ch[i]);
      }
      else
      {
          samp.push_back(ch[i]);
      }
  }
  for(int i=0;ch[i]!='\0';i++)
  {
      ch[i]=samp.front();
      samp.pop_front();
  }
  fprintf(fot,"Case #%d: %s\n",j+1,ch);
}

  fclose(fin);
  fclose(fot);

}
