#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>

using namespace std;
int main()
{

  char ch[2005],s;
  int t;
  long long n,rnd,d;
  FILE * fin, * fot;
  fin = fopen ("largeA.in","r");
  fot = fopen ("ans.out","w");
  fscanf(fin,"%d",&t);

for(int j=0;j<t;j++)
{
  map<char,int> samp;
  vector<int> num(10,0);
  fscanf(fin,"%s",&ch);
  for(int i=0;ch[i]!='\0';i++)
  {
      samp[ch[i]]++;
  }
  if(samp.find('Z')!=samp.end())
  {
      num[0]=samp['Z'];
      samp['Z']-=num[0];
      samp['E']-=num[0];
      samp['R']-=num[0];
      samp['O']-=num[0];
  }
  if(samp.find('X')!=samp.end())
  {
      num[6]=samp['X'];
      samp['S']-=num[6];
      samp['I']-=num[6];
      samp['X']-=num[6];
  }
  if(samp.find('S')!=samp.end())
  {
      num[7]=samp['S'];
      samp['S']-=num[7];
      samp['E']-=num[7];
      samp['V']-=num[7];
      samp['E']-=num[7];
      samp['N']-=num[7];
  }
  if(samp.find('V')!=samp.end())
  {
      num[5]=samp['V'];
      samp['F']-=num[5];
      samp['I']-=num[5];
      samp['V']-=num[5];
      samp['E']-=num[5];
  }
  if(samp.find('G')!=samp.end())
  {
      num[8]=samp['G'];
      samp['E']-=num[8];
      samp['I']-=num[8];
      samp['G']-=num[8];
      samp['H']-=num[8];
      samp['T']-=num[8];
  }
  if(samp.find('I')!=samp.end())
  {
      num[9]=samp['I'];
      samp['N']-=num[9];
      samp['I']-=num[9];
      samp['N']-=num[9];
      samp['E']-=num[9];
  }
  if(samp.find('N')!=samp.end())
  {
      num[1]=samp['N'];
      samp['O']-=num[1];
      samp['N']-=num[1];
      samp['E']-=num[1];
  }
  if(samp.find('W')!=samp.end())
  {
      num[2]=samp['W'];
      samp['T']-=num[2];
      samp['W']-=num[2];
      samp['O']-=num[2];
  }
  if(samp.find('O')!=samp.end())
  {
      num[4]=samp['O'];
      samp['F']-=num[4];
      samp['O']-=num[4];
      samp['U']-=num[4];
      samp['R']-=num[4];
  }
  if(samp.find('T')!=samp.end())
  {
      num[3]=samp['T'];
  }
  fprintf(fot,"Case #%d: ",j+1);
  for(int i=0;i<10;i++)
  {
      while(num[i]-->0)
        fprintf(fot,"%d",i);
  }
  fprintf(fot,"\n");
}

  fclose(fin);
  fclose(fot);

}
