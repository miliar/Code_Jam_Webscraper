#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <list>
#include <ctime>
#include <memory.h>
#include <bitset>
#include <climits>

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pi 3.141592653589793
#define endl "\n"
#define fill2d(l, nm) fill_n(*l, sizeof l / sizeof **l, nm);
#define MOD 1000000007
#define REP(i,a,b) for(int i=a;i<b;i++)
#define DEBUG(v,i,n) for(i,0,n){cout<<v[i]<<" ";}
#define all(v) (v.begin(),v.end())

using namespace std;

map<int,bool>jarvis;
void shadow(long long n)
{
 while(n!=0)
 {
     int r=n%10;
     jarvis[r]=true;
     n/=10;
 }

}

int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt","w",stdout);
ios_base::sync_with_stdio(0);

long long test;
cin>>test;
for(long long  ma=1;ma<=test;ma++)
{
	long long n;
	cin>>n;
	cout<<"Case #"<<ma<<": ";
	if(n==0)
	{
	    cout<<"INSOMNIA"<<endl;
	    continue;
	}
	jarvis.clear();
	for(long long  j=1; ;j++)
	{

	        shadow(n*j);if(jarvis.size()==10){cout<<n*j<<endl; break;}
	        }
	    }

return 0;}
