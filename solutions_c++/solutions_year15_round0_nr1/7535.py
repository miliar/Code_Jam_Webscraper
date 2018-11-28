#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;
int A[1005];
int main()
{
    freopen("C:\\Users\\Admin\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\Admin\\Desktop\\output.txt","w",stdout);
    int T;
    cin>>T;
    int Smax = 0;
    string S;
    for(int zz = 0; zz<T; zz++)
    {
		int sum = 0, cnt = 0;
		cin>>Smax;
		cin>>S;
		for(int i = 0; i<Smax+1; i++)
			A[i] = (S[i] - '0');
			
		for(int i = 0; i<Smax+1; i++)
		{
			if(i > cnt)
			{
				sum += (i - cnt);
				cnt = i;
			}
			cnt += A[i];
		}
		cout<<"Case #"<<zz+1<<": "<<sum<<"\n";
	}
	return 0;
}
		
