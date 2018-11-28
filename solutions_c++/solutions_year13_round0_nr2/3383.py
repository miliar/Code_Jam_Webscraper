#include<iostream.h>
#include<string>
#include<fstream>
#include<list>
using namespace std;
int s[100][100],temp[100][100];int T,N,M,num1,num2;


void scan(int num,int x,int y)
{   bool check=0;//cout<<x<<y<<endl;
    for(int i=0;i<N;i++) if ((s[i][y]!=num)&&(s[i][y]!=0))   check=1;
    if (check==0)       {for(int i=0;i<N;i++)s[i][y]=0;return ;} check=0;
    for(int i=0;i<M;i++) if ((s[x][i]!=num)&&(s[x][i]!=0)) check=1;
    if (check==0) {for(int i=0;i<M;i++)s[x][i]=0;return ;}
}

int minim()
{int min1=1000;
 for(int i1=0;i1<N;i1++)for(int i2=0;i2<M;i2++) if(min1>s[i1][i2]){min1=s[i1][i2];num1=i1;num2=i2;}
 return min1;
}

void findmakeM(int num3)
{
    for(int i1=0;i1<N;i1++)for(int i2=0;i2<M;i2++) if(s[i1][i2]==num3) scan(num3,i1,i2);
}

int main()
{
    ifstream fin("in.IN");ofstream fo("out.txt");
    fin>>T;string s1;
    for(int i=0;i<T;i++)
    {   fin>>N>>M;
        for(int i1=0;i1<N;i1++)for(int i2=0;i2<M;i2++) fin>>s[i1][i2];
       num1=minim();cout<<num1<<endl;
for(int i=1;i<=100;i++) findmakeM(i);s1="YES";
       for(int i1=0;i1<N;i1++)for(int i2=0;i2<M;i2++) if(s[i1][i2]!=0)s1="NO";
     fo<<"Case #"<<i+1<<": "<< s1<<endl;

    }
}
