#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <cmath>
 #define CodeJam
#ifdef CodeJam
#include "BruteForce.hh"
#include "Partion.hh"
#endif
#include <cstdio>
#include <bitset>
#include <stdexcept>
using namespace std;
// #define codechef

#define FILE
 // #define testcase1

// #define prime
int finde(vector<int>answer,int sum);
int isprime(int num);
int palindrome(string a);
int main()
{
    int t;
#ifdef testcase1
t=1;
#endif // testcase1
#ifdef codechef
scanf("%d",&t);
#endif // codechef
    #ifdef FILE
   freopen("i.txt","r+",stdin);
    freopen("o.txt","w+",stdout);
    #endif // FILE
 #ifdef prime
 int prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313};
#endif
int c5(0);
cin >> t;
string my="0123456789";
for (;c5<t;c5++){
int a,b,k;
cin >> a >> b >> k;
int total(0);
for (int c(0);c<a;c++){
    for (int c1(0);c1<b;c1++)if ((c&c1)<k)total++;
}
cout << "Case #" << c5+1 << ": " << total << endl;

}
      return 0;
}
int palindrome(string a){
string b(a);
reverse(a.begin(),a.end());
if (a==b)return 1; else return 0;






}

int isprime(int num){

	if(num<=1)
		return false;
	if(num==2)
		return true;
	if(num%2==0)
		return false;
	int sRoot = sqrt(num*1.0);
	for(int i=3; i<=sRoot; i+=2)
	{
		if(num%i==0)
			return 1;
	}
	return 1;






}
