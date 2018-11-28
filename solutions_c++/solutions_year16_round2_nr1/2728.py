// @ nk17kumar ;)

#include <iostream>
#include <math.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <list>
#include <bits/stdc++.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#define fastinput()     ios_base::sync_with_stdio(false);cin.tie(0);
#define arrin(ax,l)    for(int i=0;i<l;i++) cin>>ax[i];
#define rocknroll()     int t;cin>>t;while(t--)
#define gc              getchar_unlocked
#define ui              unsigned int
#define ll              long long
#define ld              long double
#define mod             1000000007
#define rep(i,a,b)      for(__typeof(a) i=a; i<b; ++i)
#define repr(i,a,b)     for(__typeof(a) i=a; i>=b; --i)
#define fill(a,b)       memset(a, b, sizeof(a))
#define l(a)           int((a).size())
#define pb              push_back
//#define mp              make_pair
#define X               first
#define Y               second
#define all(c)          (c).begin(),(c).end()
#define loop(c,i)       for(typeof(c.begin()) i = c.begin(); i != c.end(); i++)
//#define exeTime()       cout << "Execution time : " << ticktock() << " seconds" ;

 int alphabets[30];
 int ans[15];
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int tt = 0;
	while(t--)
	{ tt++;
		memset(ans,0,sizeof(ans));
		memset(alphabets,0,sizeof(alphabets));
		string s;cin >>s;
		int l = s.length();
		for(int i=0; i< l ;++i)
		{
			alphabets[s[i]-'A']++;
			if(s[i]=='W')   ans[2]++;    if(s[i]=='Z')   ans[0]++;  if(s[i]=='G')   ans[8]++;  if(s[i]=='U')   ans[4]++;    if(s[i]=='X')   ans[6]++;
		}
		ans[3]=alphabets['T'-'A']-ans[2]-ans[8];ans[7]=alphabets['S'-'A']-ans[6];ans[5]=alphabets['V'-'A']-ans[7];ans[9]=alphabets['I'-'A']-ans[8]-ans[6]-ans[5];ans[1]=alphabets['O'-'A']-ans[2]-ans[0]-ans[4];
		
printf("Case #%d: ",tt);		for(int i=0;i<10;++i)
			for(int j=0;j<ans[i];j++)
				printf("%d",i);
		printf("\n");
	}
	return 0;
}
 

