#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)

using namespace std;
bool check[1000005];
vector <int > arr22;
void functi(int);
ll binar(int,int);
int main()
{
	//#ifndef ONLINE_JUDGE
		//freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
	//#endif
	ios::sync_with_stdio(false);cin.tie(0);
	 
	
	ll result=0;
	
	int test,ze,n,j,i,l,r,lola;
	
	 int arr[18];
	 //for(int u=0;u<l;u++);

	cin>>test;
	functi(1000005);
	for(ze=1;ze<=test;ze++)
	{
		cout<<"Case #"<<ze<<": \n";
		int c=0;
		vector <int > vec;
		cin>>n>>j;
		for(i=1<<(n-1);i<(1<<n);i++)
		{	if(i%2==1)
			{
				lola=0;
				int number=i;
				while(number!=0)
				{
					arr[lola]=number%2;
					number=number/2;
					lola++;
				}
				vec.clear();
				for(r=2;r<=10;r++)
				{
					result=0;
					for(l=0;l<lola;l++)
					{
						result=result+arr[l]*binar(r,l);
					}
					//cout<<result<<"\n";
					for(l=0;l<arr22.size();l++)
					{
						if(result%arr22[l]==0)
						{
							vec.push_back(arr22[l]);
							break;
						}
					}
				}
				if(vec.size()==9)
				{
					for(l=lola-1;l>=0;l--)
						cout<<arr[l];
					cout<<" ";
					for(l=0;l<vec.size();l++)
					{
						cout<<vec[l]<<" ";
					}
					cout<<"\n";
					c++;
					if(c>=j)
						break;
				}
			}
		}
	}
	return 0;
}
void functi(int N) {
    for(int i = 0; i <= N;++i) {
        check[i] = true;
    }
    check[0] = false;
    check[1] = false;
    for(int i = 2; i * i <= N; ++i) {
         if(check[i]==true) {
         	arr22.push_back(i);
             for(int j = i * i; j <= N ;j += i)
                 check[j]=false;
        }
    }
}
ll binar(int a, int b)
{
	ll x=1,y=a; 
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
		}
		y = (y*y);
		b /= 2;
	}
	return x;
}
