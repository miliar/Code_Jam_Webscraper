#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<algorithm>
#include <iomanip>
#include<cmath>
#include<map>
#include<set>
#include <sstream>
using namespace std;

#define PB push_back
#define F0(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for( auto i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
#define NOT_FOUND 11111
//////////////////////////////////////////////////
int rc[100][100];
int N,M;
set<int> st;
void display()
{
 cout<<"--------------"<<endl;
 F0(j,N)
	{
	 F0(k,M)
	 {
	   cout<<rc[j][k]<<"  ";
	  }
	  cout<<endl;
	}
 cout<<"--------------"<<endl;
 for(auto it=st.begin();it!=st.end();it++)
  cout<<*it<<" - "<<endl;
  cout<<"--------------"<<endl;
}
typedef struct
{
 int r;
 int c;
 int m;
}field;
field f1;
int r;
void getpos(int i,int j,int m)
{
     f1.m=NOT_FOUND;
	 f1.r=0;
	 f1.c=0;
  for(int k=0;k<M;k++)
  {
     if(rc[i][k]==m)
	 {
	  f1.r=i;
	  f1.c=k;
	  f1.m=rc[i][k];
	  //m=f1.m;
	  //cout<<" R1 "<<f1.r<<" C1 "<<f1.c<<" min "<<f1.m<<endl;
	 }
	  
  }
	 return ;
}

void getposv(int i,int j,int m)
{
     f1.m=NOT_FOUND;
	 f1.r=0;
	 f1.c=0;
  for(int k=0;k<N;k++)
  {
     if(rc[k][i]==m)
	 {
	  //f1.r=i;
	  f1.r=k;
	  //f1.c=k;
	  f1.c=i;
	  //f1.m=rc[i][k];
	  f1.m=rc[k][i];
	  //m=f1.m;
	  //cout<<" R2 "<<f1.r<<" C2 "<<f1.c<<" min "<<f1.m<<endl;
	 }
	  
  }
	 return ;
}


int checkv(int i,int j, int m)
{
   int x=0;
   for(int k=0;k<N;k++)
   {
     if(rc[k][j]<=m)
	 {
	  x++;
	 }
  }
  if(x==N)
   return 0;
  else 
   return 1;

}
int checkh(int i,int j, int m)
{
   int x=0;
   for(int k=0;k<M;k++)
   {
     if(rc[i][k]<=m)
	 {
	  x++;
	 }
  }
  if(x==M)
   return 0;
  else 
   return 1;
}
/*void check(int i,int j, int m)
{
 for(int k=0;k<M;k++)
 {
  if(rc[j][k]>m)
  {
    cout<<" Retrun "<<i <<" "<<k<<"  "<<m<<endl;
    r=1;
	return;
  }
 }
 if(r==0)
   return;
 
  for(int a=i;a<N;a++)
  {
    for(int b=j;b<M;b++)
   {
    if(r!=1)
	{
     getmin(a,b,m);
	 check(f1.r,f1.c,f1.m);
	}
   }
  }
}*/

int main()
{
  int T;
  cin>>T;
  FOR(i,1,T)
  {
    cin>>N>>M;
	F0(j,N)
	{
	 F0(k,M)
	 {
	   cin>>rc[j][k];
	   st.insert(rc[j][k]);
	  }
	}
	//display();
	r=0;
	//check(0,0,1001);
	int p=0;
	for(auto it=st.begin();it!=st.end();it++)
	{
	 p=0;
	// cout<<" search = "<<(*it)<<endl;
	 //getpos(0,0,(*it));
	 F0(p,N)
	 {
	  F0(q,M)
	  {
	   if(rc[p][q]==(*it))
	   {
	    f1.r=p;
		f1.c=q;
		f1.m=(*it);
		//cout<<" R2 "<<f1.r<<" C2 "<<f1.c<<" min "<<f1.m<<endl;
	    if(checkh(f1.r,f1.c,f1.m))
	    {
	    // cout<<"H1"<<endl;
	    if(checkv(f1.r,f1.c,f1.m))
	    {
	     //cout<<"V1"<<endl;
	     r=1;
		 break;
		}
	   }
	   }
	  }
	  if(r==1)
	   break;
	  }
	  /*if(f1.m==NOT_FOUND)
	   p++;
	  getposv(0,0,(*it));
	  if(checkh(f1.r,f1.c,f1.m))
	  {
	   //cout<<"H2"<<endl;
	   if(checkv(f1.r,f1.c,f1.m))
	   {
	    //cout<<"V2"<<endl;
	     r=1;
		 break;
		}
	  }
	  if(f1.m==NOT_FOUND)
	  p++;
	  if(p==2)
	  {
	    r=1;
		break;
	  }*/
	   
	}
	
	if(r==0)
     cout<<"Case #"<<i<<": YES"<<endl;
	else
	 cout<<"Case #"<<i<<": NO"<<endl;
	 st.clear();
  }

return 0;
}