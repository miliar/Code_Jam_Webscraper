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
ll q[20];
int main()
{
   // cout.precision(4);
   // cout<<fixed;
   int a;
   ll d,r,l=0,f=0,k;
   cin>>a;
   for(int i=1;i<=a;i++)
   {
	   cin>>d;
	   if(d!=0)
	   {
		   l++;
		   f=0;
		   k=0;
		   while(f!=55)
		   {
				   k+=d;
				   r=k;
			   while(r>0)
			   {
				   if(q[r%10]!=l)
				   {
					   f+=r%10+1;
					   q[r%10]=l;
				   }
				   r/=10;
			   }
		   }
		   cout<<"Case #"<<i<<": "<<k<<endl;
      }
      else
      cout<<"Case #"<<i<<": INSOMNIA"<<endl;
   }
   return 0;
}

