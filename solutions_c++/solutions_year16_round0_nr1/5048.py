/*input

*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007

int main() 
{
    std::ios::sync_with_stdio(false);
 ll t;
 cin>>t;
 ll count = 1;
 while(t--)
 {

ll x,y=0;
cin>>x;
bool flag[10] ; 
ll counter = 1;
//bool flag0 = false , flag1 = false ,flag2 = false,flag3 = false,flag4 = false,flag5 = false,flag6 = false,flag7 = false,flag8 = false,flag9 = false;
//flag0=true&&flag1=true&&flag2=true&&flag3=true&&flag4=true&&flag5=true&&flag6=true&&flag7=true&&flag8=true&&flag9=true
for (int i = 0; i < 10; ++i)
{
	/* code */flag[i]=false;
}
if(x==0)
	{cout<<"Case #"<<count++<<": "<<"INSOMNIA"<<endl;
		continue;
		}	
while(flag[0]!=true||flag[1]!=true||flag[2]!=true||flag[3]!=true||flag[4]!=true||flag[5]!=true||flag[6]!=true||flag[7]!=true||flag[8]!=true||flag[9]!=true)
{	ll z = counter*x;
 y = z;
	while(z!=0)
	{
		int num = z % 10;
		z = z / 10;
		flag[num]=true;
	}
	counter++;
}

cout<<"Case #"<<count<<": "<<y<<endl;
count++;
}

    return 0;
}
