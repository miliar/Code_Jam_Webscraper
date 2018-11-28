#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
//		freopen("a.in","r",stdin);
//		freopen("aa.out","w",stdout);
		int t;
		int a[4][4],b[4][4];
		cin >> t;
		int x,y;
		for(int i=1;i<=t;i++)
		{
				cin >> x;
				for(int i=0;i<4;i++)
						for(int j=0;j<4;j++)
								cin >> a[i][j];
				cin >> y;
				for(int i=0;i<4;i++)
						for(int j=0;j<4;j++)
								cin >> b[i][j];
				printf("Case #%d: ",i);
				int num=0;
				int ans;
				for(int i=0;i<4;i++)
						for(int j=0;j<4;j++)
								if(a[x-1][i]==b[y-1][j])
								{
										num++;
										ans=a[x-1][i];
								}
		//		cout << num << endl;
				if(num==0)
						cout <<"Volunteer cheated!" << endl;
				else if(num>1)
						cout <<"Bad magician!" << endl;
				else cout << ans << endl;
		}
//		fclose(stdin);
//		fclose(stdout);
		return 0;
}
