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

int main()
{
   // cout.precision(4);
   // cout<<fixed;
   int a,x,y,z;
   cin>>a;
   for(int i=1;i<=a;i++)
   {
	   cin>>x>>y>>z;
	   cout<<"Case #"<<i<<": ";
	   for(int j=1;j<=z;j++)
	   cout<<j<<" ";
	   cout<<endl;
   }
   return 0;
}

