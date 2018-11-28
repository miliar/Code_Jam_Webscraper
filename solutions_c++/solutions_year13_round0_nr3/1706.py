/*-------------------------------------------------------------*/
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <stack>
#include <memory.h>

using namespace std;

#define memset0(x) memset((x),0,sizeof(x)) // 0
#define memsetN(x) memset((x),-1,sizeof(x))  // 0xffffffff = -1
#define memsetM(x) memset((x),0x3f,sizeof(x)) // 0x3f3f3f3f = 1061109567
typedef long long llg;

template<class T>inline void OUTLN(T &arr,int len){
	for(int i=0;i < len;i++)
		cout << arr[i] << " ";
	cout << endl;
}

#define MOD 1000000009
#define EPS 1e-6

/*--------------------------------------------------------------*/

#define int107 10000005
llg num[50000],t;
vector<int> pri;

int huiwen(llg x) 
{	
	llg m=x,nm;
	nm=0;
	while(x)
	{
		nm=nm*10+x%10;
		x/=10;
	}
	if(nm == m)
		return 1;
	return 0;
}
void init()
{
	t=0;
	for(llg i=1;i < int107;i += 1){
		if(!huiwen(i))
			continue;
		llg p=i*i;
		if(huiwen(p))
			num[t++] = p;
	}
}
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	init();
	int T;
	cin >> T;
	llg a,b;
	int ca=1;
	while(T--){
		scanf("%lld%lld",&a,&b);
		int tot=0;
		for(int i=0;i < t;i++)
			if(num[i] >= a && num[i] <= b)
				tot++;
		printf("Case #%d: %d\n",ca++,tot);
	}
	return 0;
}
