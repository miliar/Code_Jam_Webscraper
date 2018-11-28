#include<iostream>
#include<fstream>
using namespace std;
int ar1[4][4];

int ar2[4][4];
int t1[100],t2[100];
int ans[100];
int card[100];
 ifstream cinn;
   ofstream coutt;
void input(int cse)
{ans[cse]=0;
cinn>>t1[cse];
for(int i=0;i<4;i++)
{for(int j=0;j<4;j++)
{
cinn>>ar1[i][j];
}
}
cinn>>t2[cse];
for(int i=0;i<4;i++)
{
for(int j=0;j<4;j++)
{cinn>>ar2[i][j];    }
}
for(int i=0;i<4;i++)
{for(int j=0;j<4;j++)
{
if(ar1[t1[cse]-1][i]==ar2[t2[cse]-1][j])
{ans[cse]++;
card[cse]=ar1[t1[cse]-1][i];
}
}
}
}
int main()
{coutt.open("d:/codejam/answer.txt");
cinn.open("d:/codejam/in.in");
int test;
cinn>>test;
for(int i=0;i<test;i++)
{    input(i);
}
for(int i=0;i<test;i++)
{   if(ans[i]==1)
   {coutt<<"Case #"<<(i+1)<<": "<<card[i]<<endl;
   }
else if(ans[i]==0)
   {
coutt<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
   }
   else
    {         coutt<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
    }
}
}
