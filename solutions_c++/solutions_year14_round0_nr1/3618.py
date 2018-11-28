#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{ ifstream f1;
    ofstream f2;
  f1.open("A.in",ios::in);
  f2.open("B.in",ios::out);
	int t,a1,a2,p=1;
   f1>>t;
	//scanf("%d",&t);
	while(p<=t)
	{
  int map1[17]={0},map2[17]={0},av=0,val=0,cnt=0;
   f1>>a1;
  //scanf("%d",&a1);
  for(int i=1;i<=4;i++)
  {for(int j=1;j<=4;j++)
   {
	f1>>av;
  //scanf("%d",&av);
   if(i==a1)
   map1[av]=1;
   }
  }
  f1>>a2;
  //scanf("%d",&a2);
  for(int i=1;i<=4;i++)
  {for(int j=1;j<=4;j++)
   {
f1>>av;
  //scanf("%d",&av);
   if(i==a2)
   map2[av]=1;
   }
  }cnt=0;
   for(int i=1;i<=16;i++)
   {if(map1[i]==1 && map2[i]==1)
	 {cnt++;
	 val=i;
	 }
    }
    if(cnt==1)
    f2<<"Case #"<<p<<": "<<val<<"\n";
    //printf("Case #%d:%d\n",p,val);
    else if(cnt>0)
    f2<<"Case #"<<p<<": Bad magician!\n";
    //printf("Case #%d:Bad magician!\n",p);
    else
	 f2<<"Case #"<<p<<": Volunteer cheated!\n";
	//printf("Case #%d:Volunteer cheated!",p);
    p++;
	}
}
