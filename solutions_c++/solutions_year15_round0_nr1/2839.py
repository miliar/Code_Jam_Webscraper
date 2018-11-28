//qscqesze
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <queue>
#include <typeinfo>
#include <fstream>
#include <map>
typedef long long ll;
using namespace std;
//freopen("D.in","r",stdin);
//freopen("D.out","w",stdout);
#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define maxn 200001
#define mod 10007
#define eps 1e-9
//const int inf=0x7fffffff;   //无限大
const int inf=0x3f3f3f3f;
/*
inline ll read()
{
	int x=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	return x*f;
}
int buf[10];
inline void write(int i) {
  int p = 0;if(i == 0) p++;
  else while(i) {buf[p++] = i % 10;i /= 10;}
  for(int j = p-1; j >=0; j--) putchar('0' + buf[j]);
  printf("\n");
}
*/
//**************************************************************************************

int main()
{
    freopen("A-small-attempt0.in.txt","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0;
        int temp=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]>'0')
            {
                //cout<<temp<<" "<<s[i]<<endl;
                if(temp<i)
                {
                    ans+=i-temp;
                    temp=i;
                }
                temp+=s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
