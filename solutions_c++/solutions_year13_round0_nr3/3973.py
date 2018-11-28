/* Author :  Jay Pandya */

// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>

#include <iomanip>
#include <locale>
#include <sstream>
//Macros
#define all(c) c.begin(),c.end() //all element in container c

#define tr(container, it) \
   for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //to iterate in container

#define stringswap(swstingA, swstringB) swstringA.swap(swstringB) //to swap string

#define present(container, element) (container.find(element) != container.end()) //to check whether a element is in a set or a map
#define cpresent(container, element) (find(all(container),element) != container.end()) //to check whether  a element is in container like vector

#define CLR(x,v) memset(x,v,sizeof(x)) //memset

#define print(x) cout<<#x<<" is "<<x<<endl;//for printing
#define sz(a) int((a).size()) 
#define pb push_back 
#define vi vector<int> 
#define vvi  vector<vi> //2D string 
#define ii pair<int,int> 
#define mp(typeA,typeB)  make_pair<typeA,typeB> //maing pair

//macros for limits

#define MAX 1123456
#define LLI long long int
#define ULLI unsigned long long int

using namespace std;

string getS(LLI n){ // this function will return filename as output1.txt for n=1 and so on
   string num = static_cast<ostringstream*>( &(ostringstream() << n) )->str();
   return num;
}
LLI A[10000010];
bool isPal(string S)
{
   for(int i=0;i<(sz(S)/2);i++)
   {
      if(S[i]!=S[S.size()-i-1])
	 return false;
   }
   return true;
}
void gen()
{
   for(LLI i=1;i<=10000000;i++)
 //  for(LLI i=1;i<=122;i++)
   {
      A[i]=A[i-1];
      if(isPal(getS(i)) && isPal(getS(i*i)))
      {
//      	cout<<"here "<<i<<endl;
	 A[i]++;
      }
   }
   return;
}
int main()
{
   gen();
   int test;
   scanf("%d",&test);
   for(int cas=1;cas<=test;cas++)
   {
      printf("Case #%d: ",cas);
      LLI A1,B1;
      cin>>A1>>B1;
//      cout<<A[(int)(floor(sqrt((long double)B1)))]<<" "<<A[(int)(ceil((sqrt((long double)(A1-1)))))]<<endl;
      printf("%lld\n",A[(int)(floor(sqrt((long double)B1)))]-A[(int)(floor(sqrt((long double)(A1-1))))]);
   }
   return 0;
}


