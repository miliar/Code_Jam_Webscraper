//program C

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int Get()
{
  char c;
  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
  bool Flag=(c=='-');
  if(Flag)
    c=getchar();
  int X=0;
  while(c>='0'&&c<='9')
    {
      X=X*10+c-48;
      c=getchar();
    }
  return Flag?-X:X;
}

void Output(int X)
{
  if(X<0)
    {
      putchar('-');
      X=-X;
    }
  int Len=0,Data[10];
  while(X)
    {
      Data[Len++]=X%10;
      X/=10;
    }
  if(!Len)
    Data[Len++]=0;
  while(Len--)
    putchar(Data[Len]+48);
  putchar('\n');
}

int N;
int Ans[2000];
bool Flag[2000];
vector<int> G[2000];

int main()
{
  int TotalTest=Get();
  for(int Test=1;Test<=TotalTest;Test++)
    {
      printf("Case #%d: ",Test);
      N=Get();
      static int A[2000],B[2000];
      for(int i=0;i<N;i++)
        A[i]=Get();
      for(int i=0;i<N;i++)
        B[i]=Get();
      for(int i=0;i<N;i++)
        G[i].clear();
      for(int i=0;i<N;i++)
        for(int j=i+1;j<N;j++)
          {
            if(A[i]>=A[j])
              G[i].push_back(j);
            if(B[i]<=B[j])
              G[j].push_back(i);
          }
      for(int i=0;i<N;i++)
        if(A[i]>1)
          {
            int j=i-1;
            while(A[j]!=A[i]-1)
              j--;
            G[i].push_back(j);
          }
      for(int i=0;i<N;i++)
        if(B[i]>1)
          {
            int j=i+1;
            while(B[j]!=B[i]-1)
              j++;
            G[i].push_back(j);
          }
      memset(Flag,0,sizeof(Flag));
      set<int> All;
      All.clear();
      static int Degree[2000];
      memset(Degree,0,sizeof(Degree));
      for(int i=0;i<N;i++)
        for(int j=0;j<G[i].size();j++)
          Degree[G[i][j]]++;
      for(int i=0;i<N;i++)
        if(!Degree[i])
          All.insert(i);
      for(int i=N;i;i--)
        {
          set<int>::iterator P=All.end();
          P--;
          int V=*P;
          All.erase(V);
          Ans[V]=i;
          for(int j=0;j<G[V].size();j++)
            if(!--Degree[G[V][j]])
              All.insert(G[V][j]);
        }
      for(int i=0;i<N;i++)
        {
          printf("%d",Ans[i]);
          putchar((i+1==N)?'\n':' ');
        }
    }
  return 0;
}
