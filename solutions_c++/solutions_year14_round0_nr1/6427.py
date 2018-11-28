// ccc.cpp : 定义控制台应用程序的入口点。
//



#include<iostream>
#include<fstream>
using namespace std;
const int MAX=10000;
const int Max1=4;
typedef struct re{
	int count;
	int flag;
};
re fun(int a1[Max1][Max1],int a2[Max1][Max1],int t1,int t2)
{
	int k=0;
	int c1=0,Count=0;
	re r={0,0};
	for(int i=0;i<Max1;i++)
	{
		for(int j=0;j<Max1;j++)
		{
			if(a1[t1][i]==a2[t2][j])
			{
				r.flag=a1[t1][i];
				r.count++;
			}
		}
	}
	return r;
}
void write()
{  
  ifstream fileinput;
  fileinput.open("d:\\1a.in");
  ofstream output;
  output.open("d:\\output.in");
  int Num=0;
  int a1[Max1][Max1], a2[Max1][Max1];
  int res[MAX]={0};
  fileinput>>Num;
  cout<<Num<<endl;
  int aa=0,bb=0;
   int n=0;
   re cou;
   for(int i=0;i<Num;i++)
    {
       fileinput>>aa;
       cou.count=0;
       cou.flag=0;
       for(int i1=0;i1<Max1;i1++)
       {
       	 for(int j1=0;j1<Max1;j1++)
         {
       	    fileinput>>a1[i1][j1];
         }
       }
       fileinput>>bb;
	    for(int i1=0;i1<Max1;i1++)
       {
       	 for(int j1=0;j1<Max1;j1++)
         {
       	    fileinput>>a2[i1][j1];
         }
       }
       cou=fun(a1,a2,aa-1,bb-1);
       if(cou.count==0)
       {
       	 output<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		  cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
       }else if(cou.count==1)
       {
       	 output<<"Case #"<<i+1<<": "<<cou.flag<<endl;
		  cout<<"Case #"<<i+1<<": "<<cou.flag<<endl;
       }else if(cou.count>1)
       {
       	 output<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		 cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
       }
    }
  fileinput.close();
}
int main()
{
 write();
}