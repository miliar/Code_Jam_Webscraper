#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <string>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,l,m) for(int i=l;i<=m;i++)
#define iter(c,m) for(c=m.begin();c!=m.end();c++)
#define make_pair MP
#define push_back PB

using namespace std;
char a[4][4];
int dflag=0;
int flag=0;
void test(int i,int test,int level)
{
	int c1=0,c2=0,t,k=0,d=0;
	if(!flag)
	{
	
	REP(j,4)
	{
		switch (test) 
		{
		case 1: t=a[i][j];break;
		case 2: t=a[j][i];break;
		case 3: t=a[j][j];break;
		case 4: t=a[j][3-j];break;
		}
		switch (t)
		{
			case 'X':c1++;break;
			case 'O':c2++;break;
			case '.':d++;break;
			case 'T':k++;break;
		}
		//printf("c1 %d c2 %d d %d k %d\n",c1,c2,d,k);
		if(c1==4 || (c1==3 && k)) {cout<<"Case #"<<level<<": "<<"X won\n";flag=1;}
		else if(c2==4 || (c2==3 && k)) {cout<<"Case #"<<level<<": "<<"O won\n";flag=1;}
		else if(d) dflag=1;
	}
	}
}
int main()			
{
	int T;
	cin>>T;
	REP(t,T)
	{
		char temp[5];
		REP(i,4)
		{
		scanf("%s",temp);
		REP(j,4) a[i][j]=temp[j];
		}
		//REP(i,4){cout<<endl;REP(j,4) cout<<a[i][j]<<" ";}
		FOR(j,1,4)
		{
			REP(i,4)
			test(i,j,t+1);
		}
		if(!flag) 
		{
			if(dflag) cout<<"Case #"<<t+1<<": "<<"Game has not completed\n";
			else
			cout<<"Case #"<<t+1<<": "<<"Draw\n";
		}
		//(flag)?cout<<"Case #"<<t<<": "<<"Game has not completed\n";:cout<<"Case #"<<t<<": "<<"Draw\n";
		dflag=0;flag=0;
	}
	
	
	
	return 0;
}
	
