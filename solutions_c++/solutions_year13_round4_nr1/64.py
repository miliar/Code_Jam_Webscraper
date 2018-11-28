//program A

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

struct Event
{
  int Time,Number;
};

bool operator <(Event A,Event B)
{
  return (A.Time==B.Time)?(A.Number>B.Number):(A.Time<B.Time);
}

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

const int Mod=1000002013;

long long Cost(long long N,long long X)
{
  return X*N-X*(X-1)/2;
}

int main()
{
  int TotalTest=Get();
  for(int Test=1;Test<=TotalTest;Test++)
    {
      printf("Case #%d: ",Test);
      int N=Get(),M=Get();
      static Event E[2000];
      long long Ans=0;
      for(int i=0;i<M;i++)
        {
          int X=Get(),Y=Get(),P=Get();
          E[i*2]=(Event){X,P};
          E[i*2+1]=(Event){Y,-P};
          Ans=(Ans-(long long)(Y-X)*(Y-X)%Mod*P)%Mod;
        }
      sort(E,E+M*2);
      int Top=1;
      for(int i=1;i<M*2;i++)
        if(E[i].Number>0)
          E[Top++]=E[i];
        else
          {
            int T=-E[i].Number;
            while(T)
              {
                int Min=min(T,E[Top-1].Number);
                Ans=(Ans+(long long)(E[i].Time-E[Top-1].Time)*(E[i].Time-E[Top-1].Time)%Mod*Min)%Mod;
                T-=Min;
                E[Top-1].Number-=Min;
                if(!E[Top-1].Number)
                  Top--;
              }
          }
      if(Ans<0)
        Ans+=Mod;
      if(Ans&1)
        Ans+=Mod;
      cout<<Ans/2<<endl;
    }
  return 0;
}
