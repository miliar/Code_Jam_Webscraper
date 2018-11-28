
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool palindrome(int x)
{
if(x<0)return false;
int Len=0, Data[10];
while(x){Data[Len++]=x%10;x/=10;}
for(int i = 0 , j=Len-1;i<j;i++,j--)
if(Data[i]!=Data[j])return false;
return true;
}
int main()
{
	freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
	int tr; scanf( "%d", &tr );

	for(int i = 0 ; i < tr;i++)
	{
		int r1, r2, count = 0, tmp;
		cin>>r1>>r2;
		for(int j = r1 ; j <= r2 ; j++) 
		{
			tmp = (int)sqrt((double)j);
			if(tmp*tmp == j && palindrome(j) && palindrome(tmp))
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	fclose (stdout);
	return 0;
}