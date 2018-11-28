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

int main()
{
    freopen("A-large.out","w",stdout);
	freopen("A-large.in","r",stdin);
	int testCases,n;
	testCases=getint();
	string s;
	for(int t=1 ; t<=testCases ; t++){
        n=getint();
        cin>>s;
        int cumu=0,ans=0;
        for(int i=0 ; i<s.size() ; i++){
            if(cumu<i){
                ans+=(i-cumu);
                cumu=i+s[i]-'0';
            }else
                cumu+=s[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
