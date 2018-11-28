#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#define S second
#define F first
#define pb push_back
using namespace std;
int a1,b1,a[4][4],b[4][4];
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,test;
	cin>>t;
	test=t;
	while (t--)
	{
		vector <int> c;
		cin>>a1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)  
			{
				scanf("%d",&a[i][j]);
				if (i==a1-1) c.pb(a[i][j]); 
		    }

		cin>>b1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				scanf("%d",&b[i][j]);
			if (i==b1-1) c.pb(b[i][j]);
			}
	vector <int> f;
	sort(c.begin(),c.end());
	int cur=0,last=0;
	for (int i = 1; i < 8; i++)
		if (c[i]==c[i-1]) cur++,last=c[i];
	printf("Case #%d: ",test-t);
	if (cur==1)
		printf("%d",last);
	if (cur>1)
		printf("Bad magician!");
	if (cur==0)
		printf("Volunteer cheated!");
	cout<<endl;
	}

return 0;
}
