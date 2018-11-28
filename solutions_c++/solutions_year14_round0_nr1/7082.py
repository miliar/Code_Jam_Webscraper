#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int w,n,test,ii,ans,i,j;
int flag[20];
int a[5][5];
int main()
{

	scanf("%d",&test);
	while (test)
	{
		test--;
		ii++;
		memset(flag,0,sizeof(flag));
		ans=0;
		scanf("%d",&n);
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		for (i=1;i<=4;i++)
			flag[a[n][i]]++;

		scanf("%d",&n);
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		for (i=1;i<=4;i++)
			flag[a[n][i]]++;

		for (i=1;i<=16;i++)
		{
			if (flag[i]) ans++;
            if (flag[i]==2) w=i;
		}
        cout<<"Case #"<<ii<<": ";
		if (ans==8) cout<<"Volunteer cheated!"<<endl;
		else
		if (ans<7) cout<<"Bad magician!"<<endl;
		else
		cout<<w<<endl;
	}

}
		
	

