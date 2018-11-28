#include<cstdio>
#include<string>
#include<vector>
using namespace std;

char s[7][7];

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    
    int T,k=0;
    
    scanf("%d",&T);
    
    while(T--)
    {
        k++;
        
        for(int i=0;i<4;i++)
            scanf("%s",s[i]);
        
        printf("Case #%d: ",k);
        
        bool dots=0,flag=0;
        
        for(int i=0;i<4;i++)
        {
            int c=0,t=0;
            for(int j=0;j<4;j++)
                if(s[i][j]=='X' || s[i][j]=='T')
				{
					if(s[i][j]=='T')t++;
                    c++;
				}
            
            if(c==4 && t<=1)
            {
				printf("X won\n");
				flag=1;
				break;
            }
        }
        
        if(flag)continue;
        
        for(int i=0;i<4;i++)
        {
            int c=0,t=0;
            for(int j=0;j<4;j++)
                if(s[i][j]=='O' || s[i][j]=='T')
				{
					if(s[i][j]=='T')t++;
                    c++;
				}
            
            if(c==4 && t<=1)
            {
				printf("O won\n");
				flag=1;
				break;
            }
        }
        
        if(flag)continue;
        
        for(int i=0;i<4;i++)
        {
            int c=0,t=0;
            for(int j=0;j<4;j++)
                if(s[j][i]=='X' || s[j][i]=='T')
				{
					if(s[j][i]=='T')t++;
                    c++;
				}
            
            if(c==4 && t<=1)
            {
				printf("X won\n");
				flag=1;
				break;
            }
        }
        
        if(flag)continue;
        
        for(int i=0;i<4;i++)
        {
            int c=0,t=0;
            for(int j=0;j<4;j++)
                if(s[j][i]=='O' || s[j][i]=='T')
				{
					if(s[j][i]=='T')t++;
                    c++;
				}
            
            if(c==4 && t<=1)
            {
				printf("O won\n");
				flag=1;
				break;
            }
        }
        
        if(flag)continue;
        
        int c=0,t=0;
		for(int j=0;j<4;j++)
			if(s[j][j]=='X' || s[j][j]=='T')
			{
				if(s[j][j]=='T')t++;
				c++;
			}
		
        if(c==4 && t<=1)
		{
			printf("X won\n");
			flag=1;
		}
        
        if(flag)continue;
        
        c=0,t=0;
		for(int j=0;j<4;j++)
			if(s[j][j]=='O' || s[j][j]=='T')
			{
				if(s[j][j]=='T')t++;
				c++;
			}
		
        if(c==4 && t<=1)
		{
			printf("O won\n");
			flag=1;
		}
        
        if(flag)continue;
        
		c=0,t=0;
		for(int j=0;j<4;j++)
			if(s[j][3-j]=='X' || s[j][3-j]=='T')
			{
				if(s[j][3-j]=='T')t++;
				c++;
			}
		
        if(c==4 && t<=1)
		{
			printf("X won\n");
			flag=1;
		}
        
        if(flag)continue;
        
        c=0,t=0;
		for(int j=0;j<4;j++)
			if(s[j][3-j]=='O' || s[j][3-j]=='T')
			{
				if(s[j][3-j]=='T')t++;
				c++;
			}
		
        if(c==4 && t<=1)
		{
			printf("O won\n");
			flag=1;
		}
        
        if(flag)continue;
        
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(s[i][j]=='.')
                    dots=1;
        
        if(dots)printf("Game has not completed\n");
        else printf("Draw\n");
    }
}
