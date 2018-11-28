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
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)

using namespace std;


int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt","w",stdout);
ios_base::sync_with_stdio(0);

long long t;
cin>>t;
for(int j=1;j<=t;j++)
{
  cout<<"Case #"<<j<<": ";
string s;
cin>>s;
list<char>temp;
temp.pb(s[0]);
for(int i=1;i<s.size();i++)
{
  if(s[i]>=temp.front())
  temp.push_front(s[i]);
  else
  temp.push_back(s[i]);
}

for(list<char>::iterator it=temp.begin();it!=temp.end();it++)
cout<<*it;
cout<<endl;
}
return 0;}
