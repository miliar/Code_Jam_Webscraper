/*
ID: diptesh1
TASK:
LANG: C++
*/

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

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define PB(X) push_back(X)
#define fill(x,v) memset(x,v,sizeof(x))
int getint()
{
	char ch;
	do
	{
		ch=getchar();
	}while (ch!='-'&&(ch<'0'||ch>'9'));
	int ans=0,f=0;
	if (ch=='-') f=1; else ans=ch-'0';
	while (isdigit(ch=getchar())) ans=ans*10+ch-'0';
	if (f) ans*=-1;
	return ans;
}
#define MOD 1000000007

int getAns(vector<int> numbers){
    int mx=0;
    for(int i=0 ; i<numbers.size() ; i++){
        mx=max(mx,numbers[i]);
    }
    int ans=MOD;
    for(int i=1 ; i<=mx ; i++){
        int curAns=0;
        int maxNum=0;
        for(int j=0 ; j<numbers.size()  ; j++){
            int mult=1;
            int num=numbers[j];
            while(num>i){
                curAns++;
                num-=i;
            }
        }
        ans=min(ans,curAns+i);
    }
    return ans;
}
int main()
{
    freopen("B-large (1).out","w",stdout);
	freopen("B-large (1).in","r",stdin);
	int testCases,n,num;
	testCases=getint();
	vector<int> temp;
	for(int t=1 ; t<=testCases ; t++){
        n=getint();
        temp.clear();
        for(int i=1 ; i<=n ; i++){
            num=getint();
            temp.push_back(num);
        }
        int xx=getAns(temp);
        printf("Case #%d: %d\n",t,xx);
	}
	return 0;
}
