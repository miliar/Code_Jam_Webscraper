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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int T,R,N,M,K;
int p[10];
set<int> ss;
int main()
{
	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);	
	cin >> T;
	cin >> R >> N >> M >> K;
	cout <<"Case #1:"<<endl;
	for (int kk=1;kk<=R;++kk)
	{		
		for (int i=0;i<K;++i)
		{
			cin>>p[i];
		}
		int b=0;
		for (int i=2;i<=M;++i)
		{
			for (int j=i;j<=M;++j)
			{
				for (int k=j;k<=M;++k)
				{
					ss.clear();
					ss.insert(i*j);
					ss.insert(1);
					ss.insert(i*j*k);
					ss.insert(i*k);
					ss.insert(i);
					ss.insert(j*k);
					ss.insert(j);
					ss.insert(k);
					int ok=1;
					for (int l=0;l<k;++l)
					{
						if (!ss.count(p[l]))
						{
							ok=0;
							break;
						}
					}
					if (ok)
					{
						b=1;
						cout << i << j << k << endl;
						break;
					}

				}
				if (b==1)
				{
					break;
				}
			}
			if (b==1)
			{
				break;
			}
		}
	}
	
	return 0;
}