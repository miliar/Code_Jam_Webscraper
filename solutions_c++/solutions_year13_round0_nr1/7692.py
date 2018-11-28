#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
using namespace std;

/*
char str[10005][80];
int nex[10005];
int gcd(int a,int b)
{
    int c=a%b;
    while(c)
    {
        a=b;b=c;
        c=a%b;
    }
    return b;
}
int main()
{
    freopen("1.txt","r",stdin);
    int r,c;
    nex[0]=-1;
    scanf("%d%d",&r,&c);
    for(int i=0;i<r;i++)
        scanf("%s",str[i]);
    int j=0,k=-1;
    while(str[0][j])
    {
        while(k!=-1 && str[0][j]!=str[0][k]) k=nex[k];
        k++;j++;
        nex[j]=k;
    }
    int fu=nex[c];
    int ans,temp;
    for(int i=0;i<c;i++)
    {
        j=0,k=-1;
        while(str[j][i])
        {
            while(k!=-1 && str[j][i]!=str[k][i]) k=nex[k];
            k++;j++;
            nex[j]=k;
        }
        temp=nex[r];
        if(i) ans=ans*temp/gcd(ans,temp);
        else ans=temp;
    }
    printf("%d\n",ans*fu);
    return 0;
}*/





#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
char str[5][5];
int main()
{
	scanf("%d",&T);
	int cnt_a=0,cnt_b=0,cnt_c=0,cnt_d=0;
	int flag=-1;//标注是那种情况
	for(int y=1;y<=T;y++)
		{
		memset(str,0,sizeof(str));
		for(int i=0;i<4;i++)
			scanf("%s",str[i]);
		flag=-1;
		for(int i=0;i<4;i++)
			{
				cnt_a=0,cnt_b=0,cnt_c=0,cnt_d=0;
				for(int j=0;j<4;j++)
				{
				if(str[i][j]=='X')
					cnt_a++;
				if(str[i][j]=='O')
					cnt_b++;
				if(str[i][j]=='.')
					cnt_c++;
				if(str[i][j]=='T')
					cnt_d++;
				}
			if((cnt_a+cnt_c+cnt_d==4&&cnt_c!=0)||(cnt_b+cnt_c+cnt_d==4&&cnt_c!=0))
				{
				flag=1;
				}
			if((cnt_d==1&&cnt_a==3)||cnt_a==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: X won\n",y);
				break;
				}
			if((cnt_d==1&&cnt_b==3)||cnt_b==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: O won\n",y);
				break;
				}
			}
		if(flag==2)
			continue;
		for(int i=0;i<4;i++)
			{
				cnt_a=0,cnt_b=0,cnt_c=0,cnt_d=0;
				for(int j=0;j<4;j++)
				{
				if(str[j][i]=='X')
					cnt_a++;
				if(str[j][i]=='O')
					cnt_b++;
				if(str[j][i]=='.')
					cnt_c++;
				if(str[j][i]=='T')
					cnt_d++;
				}
			if((cnt_a+cnt_c+cnt_d==4&&cnt_c!=0)||(cnt_b+cnt_c+cnt_d==4&&cnt_c!=0))
				{
				flag=1;
				}
			if((cnt_d==1&&cnt_a==3)||cnt_a==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: X won\n",y);
				break;
				}
			if((cnt_d==1&&cnt_b==3)||cnt_b==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: O won\n",y);
				break;
				}
			}
		if(flag==2)
			continue;
		cnt_a=0,cnt_b=0,cnt_c=0,cnt_d=0;
		for(int i=0;i<4;i++)
			{
			if(str[i][i]=='X')
				cnt_a++;
			if(str[i][i]=='O')
				cnt_b++;
			if(str[i][i]=='.')
				cnt_c++;
			if(str[i][i]=='T')
				cnt_d++;
			}
			if((cnt_a+cnt_c+cnt_d==4&&cnt_c!=0)||(cnt_b+cnt_c+cnt_d==4&&cnt_c!=0))
				{
				flag=1;
				}
			if((cnt_d==1&&cnt_a==3)||cnt_a==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: X won\n",y);
				continue;
				}
			if((cnt_d==1&&cnt_b==3)||cnt_b==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: O won\n",y);
				continue;
				}
			if(flag==2)
				continue;
			cnt_a=0,cnt_b=0,cnt_c=0,cnt_d=0;
			for(int i=0;i<4;i++)
			{
			if(str[i][3-i]=='X')
				cnt_a++;
			if(str[i][3-i]=='O')
				cnt_b++;
			if(str[i][3-i]=='.')
				cnt_c++;
			if(str[i][3-i]=='T')
				cnt_d++;
			}
			if((cnt_a+cnt_c+cnt_d==4&&cnt_c!=0)||(cnt_b+cnt_c+cnt_d==4&&cnt_c!=0))
				{
				flag=1;
				}
			if((cnt_d==1&&cnt_a==3)||cnt_a==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: X won\n",y);
				continue;
				}
			if((cnt_d==1&&cnt_b==3)||cnt_b==4)
				{
				flag=2;//有人赢了
				printf("Case #%d: O won\n",y);
				continue;
				}
			if(flag==1)
				printf("Case #%d: Game has not completed\n",y);
			if(flag==-1)
				printf("Case #%d: Draw\n",y);
		}
	return 0;
}



























