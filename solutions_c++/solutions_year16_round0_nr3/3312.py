#include<fstream>
// #include<stdio.h>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<set>
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define ll long long
#define maxN 100009

using namespace std;

// srand((unsigned)time(NULL));
// int r=rand()%10+1;

ifstream cin("1.in");
 ofstream cout("1.out");

// priority_queue<int, vector<int>, geator<int> > p; 

int d[17],f=0;

int main()
{
   // cout.precision(4);
   // cout<<fixed;
   d[1]=1;
   d[2]=1;
   d[16]=1;
   
   int l=15;
   cin>>f>>f>>f;cout<<"Case #"<<1<<": "<<endl;
   f=0;
   while(1)
   {
	   d[l]=1;
	   for(int i=3;i<l;i+=2)
	   {
		   for(int j=4;j<l;j+=2)
		   {
			   f++;
			   d[i]=1;
			   d[j]=1;
			   
			   for(int k=1;k<=16;k++)
			   {
				   cout<<d[k];
			   }
			   cout<<" ";
			   for(int k=2;k<=10;k++)
			   cout<<k+1<<" ";
			   cout<<endl;
			   if(f==50)
			   {
				   return 0;
			   }
			   d[i]=0;
			   d[j]=0;
		   }
	   }
	   d[l]=0;
	   l-=2;
   }
      
   return 0;
}

