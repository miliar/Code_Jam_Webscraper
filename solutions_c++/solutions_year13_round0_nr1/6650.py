// codejam2013.1.cpp : 定义控制台应用程序的入口点。

#include<iostream>
#include<stdio.h>
using namespace std;
int check_colume(char game[4][4],int &x,int &o,int &t,bool &uncompleted,bool &xwin,bool &owin)
{
    xwin = owin = false;
    int i,j;
    for(i = 0; i < 4; i++)
    {
		x = o = t = 0;
        for(j = 0; j < 4; j++)
        {
                x += (game[i][j] == 'X')? 1:0;
     			o += (game[i][j] == 'O')? 1:0;
     			t += (game[i][j] == 'T')? 1:0;
     			if (game[i][j] == '.')	uncompleted = true;
        }
       	if (x+t == 4)
        {
     			xwin  = true;
     			return 1;
  		}
  		if (o+t == 4)
        {
     			owin = true;
     			return 1;
  		}
    }
    return 0;
}
int check_raw(char game[4][4],int &x,int &o,int &t,bool &uncompleted,bool &xwin,bool &owin)
{
    int i,j;
    xwin = owin = false;
    for(i = 0; i < 4; i++)
    {
		x = o = t = 0;
        for(j = 0; j < 4; j++)
        {
                x += (game[j][i] == 'X')? 1:0;
     			o += (game[j][i] == 'O')? 1:0;
     			t += (game[j][i] == 'T')? 1:0;
     			if (game[j][i] == '.')	uncompleted = true;
        }
       	if (x+t == 4)
        {
     			xwin  = true;
     			return 1;
  		}
  		if (o+t == 4)
        {
     			owin = true;
     			return 1;
  		}
    }
    return 0;
}
int check_diagonal1(char game[4][4],int &x,int &o,int &t,bool &uncompleted,bool &xwin,bool &owin)
{
    int j;
	x = o = t = 0;
    for(j = 0; j < 4; j++)
    {

  		x += (game[j][j] == 'X')? 1:0;
  		o += (game[j][j] == 'O')? 1:0;
  		t += (game[j][j] == 'T')? 1:0;
   	}
   	if (x+t == 4)
    {
        xwin = true;
        return 1;
    }
    if (o+t == 4)
    {
        owin = true;
        return 1;
    }
    return 0;
}
int check_diagonal2(char game[4][4],int &x,int &o,int &t,bool &uncompleted,bool &xwin,bool &owin)
{
    int j;
    x = o = t = 0;
    for(j = 0; j < 4; j++)
    {
  		x += (game[j][3-j] == 'X')? 1:0;
  		o += (game[j][3-j] == 'O')? 1:0;
  		t += (game[j][3-j] == 'T')? 1:0;
   	}
   	if (x+t == 4)
    {
        xwin = true;
        return 1;
    }
    if (o+t == 4)
    {
        owin = true;
        return 1;
    }
    return 0;
}
int main()
{  
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int T,num,x,t,o;
	string s;
    bool uncomplete,xwin,owin;
	cin>>T;
    num = 1;
    const char *str[4] = {"X won","O won","Draw","Game has not completed"};
    while(num <= T)
    {
        char game[4][4];
        int i,j;
//		if(num != 1)
//			getchar();
        for(i = 0; i < 4; i++)
        {
				getchar();
                for(j = 0;j < 4;j++)
                game[i][j] = getchar();
        }
        x = t = o = 0;
        uncomplete = xwin = owin = false;
        if(check_colume(game,x,o,t,uncomplete,xwin,owin))
        {
            if(xwin)
			{
				printf("Case #%d: %s\n",num,str[0]);
				getchar();
			}
            else if(owin)
			{
				printf("Case #%d: %s\n",num,str[1]); 
				getchar();
			}
                          
        }
        else if(check_raw(game,x,o,t,uncomplete,xwin,owin))
        {
                if(xwin)
				{
					printf("Case #%d: %s\n",num,str[0]);
					getchar();
				}   
                else if(owin)
				{
					printf("Case #%d: %s\n",num,str[1]);
					getchar();
				}
                               
        }
        else if(check_diagonal1(game,x,o,t,uncomplete,xwin,owin))
        {
                if(xwin)
				{
					printf("Case #%d: %s\n",num,str[0]);
					getchar();
				}
                               
                else if(owin)
				{
					printf("Case #%d: %s\n",num,str[1]);
					getchar();
				}
                                
                
        }
        else if(check_diagonal2(game,x,o,t,uncomplete,xwin,owin))
        {
                if(xwin)
				{
					printf("Case #%d: %s\n",num,str[0]);
					getchar();
				}
                                
                else if(owin)
				{
					printf("Case #%d: %s\n",num,str[1]);
					getchar();
				}
                                
                
        }
        else
        {
                if(uncomplete)
				{
					printf("Case #%d: %s\n",num,str[3]);
					getchar();
				}
                               
                else 
				{
					printf("Case #%d: %s\n",num,str[2]);
					getchar();
				}
        }
        num++;
    }
	fclose(stdin);
	fclose(stdout);
    system("pause");
    return 0;
}


