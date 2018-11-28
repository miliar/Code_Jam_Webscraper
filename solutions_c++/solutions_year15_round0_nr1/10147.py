#include<iostream>
#include<string.h>
#include<vector>
#include <sstream>
#include <cstdio>
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORR(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
typedef unsigned long long ull;

int main()
{
  freopen("in.in", "r", stdin);
  freopen("out.out", "w", stdout);
  freopen("log.txt", "w", stderr);
  int tt;
 cin>> tt;
  for (int qq=1;qq<=tt;qq++) {
    cout<<"Case #"<< qq <<": ";
	string n;
    int Sm, tot=0, min=0, S[2001];
	cin>> Sm >> n;
		
	FOR(i,0,Sm)
		S[i] = n[i] - 48;
	tot = S[0];
	//cout <<"tot val:"<< tot << " ";
	FOR(i,1,Sm)
	{
		if(S[i]!= 0 && i > tot)
		{
			min+=(i- tot);
			tot+=(min+S[i]);
			//cout << i <<" "<< min << "\n";
			continue;
		}
		tot+=S[i];
	}
	cout << min<<"\n";
  }
return 0;
}




