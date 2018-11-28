#include <iostream>
#include <queue>
#include <string>
using namespace std;

#define DBG(x) cout<<#x<<" = "<<x<<"\n";
/*int is_palindrome(unsigned long orig)
{
  unsigned long reversed = 0, n = orig;

  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return orig == reversed;
}
*/
int main()
{
	/*long long pole[100000];
	//long long prefix[4 294 967 296];
	long long uka=0,t,a,b,nas;
	long long pocet=0;
	for(long long i=1;i*i<100000001000000 && uka<1010;i++)
		{
			if(is_palindrome(i)) 
				{if(is_palindrome(i*i)) 
					{
						cout<<i*i<<", "<<endl;
						/*pocet++;prefix[i]=pocet;;pole[uka]=i*i;uka++;
						nas=i*i;
						while(i<nas) {prefix[i]=pocet;i++;}
					}
		}*/
long long pole[50]={1, 
4, 
9, 
121, 
484, 
10201, 
12321, 
14641, 
40804, 
44944, 
1002001, 
1234321, 
4008004, 
100020001, 
102030201, 
104060401, 
121242121, 
123454321, 
125686521, 
400080004, 
404090404, 
10000200001, 
10221412201, 
12102420121, 
12345654321, 
40000800004, 
1000002000001, 
1002003002001, 
1004006004001, 
1020304030201, 
1022325232201, 
1024348434201, 
1210024200121, 
1212225222121, 
1214428244121, 
1232346432321, 
1234567654321, 
4000008000004, 
4004009004004} ;

			
	/*for(long long i=0;i<1010 && uka<1010;i++)
		{
			cout<<pole[i]<<" ";
		}
	*/
	long long a,b,t;
	cin>>t;
	long long pocet=0;
	for(long long i=0;i<t;i++)
	{
		pocet=0;
		cin>>a>>b;
		long long x=0;
		while(pole[x]<a) x++;
		//	DBG(pole[x-1]);
		//cout<<x;
		while(pole[x]<(b+1)) {x++;pocet++;}
		cout<<"Case #"<<i+1<<": "<<pocet<<"\n";			
	}
	//cout<<"konieeeeeeeeeeeeec";    	
	return 0;
}
