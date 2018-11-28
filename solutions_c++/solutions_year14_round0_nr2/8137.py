#include<iostream>
#include<iomanip>
#include<string>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#define for(i, a, b) for( int i = (a); i < (b); i++ )
#define all(a) (a.begin(), a.end())
#define set(a, s) memset(a, s, sizeof (a))
#define pb push_back
#define mp make_pair
typedef long long ll;
using namespace std;

int main() 
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int kase = 0;
	int t;
	cin>>t;
	while(t--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double rate = 2.0;
		double res= 0;
		double mini= 1e9;
		double sum= 0;
		cout<<"case #"<<++kase <<": ";
		while(1)
		{
			double target = x/rate;


			if(sum+target<mini)
			{
				mini = sum+target;
			}
			else
			{
				cout << setprecision(7) <<fixed << mini <<endl;
				break;			
			}
			sum = sum+c/rate;
			rate +=f;
		}
	}
	return 0;
}