#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
const long long int INF=1000*1000*1000;
const int MAXN=1000*1000;
using namespace std;
int t,i,j,k;
char a[10][10],cur;
bool tochka;
string ans[1005];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>t;
	for(i=0;i<t;i++)
	{
		ans[i+1]="";
		tochka=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>a[j][k];
				if(a[j][k]=='.')tochka=1;
			}	
		}
		for(j=0;j<4;j++)
		{
			for(k=1;k<4;k++)
			{
				if((a[j][k]!=a[j][k-1]&&a[j][k]!='T')||a[j][k]=='.')
				{
					goto qwe;
				}
				if(a[j][k]!='T'&&a[j][k]!='.')cur=a[j][k];
			}
			ans[i+1]+=cur;
			ans[i+1]+=" won";
			goto wer;
			qwe:;
		}	
		for(k=0;k<4;k++)
		{
			for(j=1;j<4;j++)
			{
				if((a[j][k]!=a[j-1][k]&&a[j][k]!='T')||a[j][k]=='.')
				{
					goto ert;
				}
				if(a[j][k]!='T'&&a[j][k]!='.')cur=a[j][k];
			}
			ans[i+1]+=cur;
			ans[i+1]+=" won";
			goto wer;
			ert:;
		}
		for(j=1;j<4;j++)
		{
			if((a[j][j]!=a[j-1][j-1]&&a[j][j]!='T')||a[j][j]=='.')
			{
				goto rty;
			}
			if(a[j][j]!='T'&&a[j][j]!='.')cur=a[j][j];
		}
		ans[i+1]+=cur;     
		ans[i+1]+=" won";
		goto wer;
		rty:;
		k=2;
		for(j=1;j<4;j++)
		{
			if((a[j][k]!=a[j-1][k+1]&&a[j][k]!='T')||a[j][k]=='.')
			{
				goto tyu;
			}
			if(a[j][k]!='T'&&a[j][k]!='.')cur=a[j][k];
			--k;
		}
		ans[i+1]+=cur;     
		ans[i+1]+=" won";
		goto wer;
		tyu:;			
		if(tochka==1)ans[i+1]="Game has not completed";
		else ans[i+1]="Draw";
		wer:;
	}
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": "<<ans[i]<<endl;
	}
	return 0;
}

	