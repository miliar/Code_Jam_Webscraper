#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <queue>
#include <vector>
#include <set>
#define maxn
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

int a[5][5];
int cnt[20];

void input()
{
	for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
			cin >> a[i][j];
}

int main()
{
    freopen("H:\\Users\\Yun\\Desktop\\input.txt","r",stdin);
    freopen("H:\\Users\\Yun\\Desktop\\output.txt","w",stdout);

    int tt;
    cin >> tt;
    int x;
    int id=0;
    while (tt--)
    {
    	id++;
    	clearAll(cnt);
    	cin >> x;
    	input();
    	for (int i=1;i<=4;i++)
    		cnt[a[x][i]]++;
    	cin >> x;
    	input();
    	for (int i=1;i<=4;i++)
    		cnt[a[x][i]]++;
    	int num,ans;
    	num=0;
    	for (int i=1;i<=4;i++)
    		if (cnt[a[x][i]]==2)
    			ans=a[x][i],num++;
    	printf("Case #%d: ",id);
    	if (num==0)
    		cout <<"Volunteer cheated!" <<endl;
    	else if (num>1)
    		cout <<"Bad magician!" <<endl;
    	else cout << ans <<endl;
    }

   	 
    return 0;
}
