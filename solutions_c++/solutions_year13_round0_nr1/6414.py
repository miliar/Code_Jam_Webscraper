#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
using namespace std;
string s[8];
int main()
{
    int T,t=0;
    scanf("%d",&T);
    while(t++<T)
    {
        cin>>s[0]>>s[1]>>s[2]>>s[3];
        int i,j,l=0,dot=0;
        for(i=0;i<4;i++)
        {
            int brx=0,bro=0,brt=0;
            for(j=0;j<4;j++)
            if(s[i][j]=='.')
            {dot=1;}
            else
            if(s[i][j]=='X')brx++;
            else
            if(s[i][j]=='O')bro++;
            else
            if(s[i][j]=='T')brt++;
            if(brx==4||(brx==3&&brt==1))
            {l=1;printf("Case #%d: X won\n",t);}
            if(bro==4||(bro==3&&brt==1))
            {printf("Case #%d: O won\n",t);l=1;}
        }
        if(l==1)continue;
        for(j=0;j<4;j++)
        {
            int brx=0,bro=0,brt=0;
            for(i=0;i<4;i++)
            if(s[i][j]=='.')
            {dot=1;}
            else
            if(s[i][j]=='X')brx++;
            else
            if(s[i][j]=='O')bro++;
            else
            if(s[i][j]=='T')brt++;
            if(brx==4||(brx==3&&brt==1))
            {l=1;printf("Case #%d: X won\n",t);break;}
            if(bro==4||(bro==3&&brt==1))
            {printf("Case #%d: O won\n",t);l=1;break;}
        }
        int brx=0,brt=0,bro=0;
        if(l)continue;
        
        for(i=0;i<4;i++)
        if(s[i][i]=='.')
        {dot=1;}
        else
        if(s[i][i]=='X')brx++;
        else
        if(s[i][i]=='O')bro++;
        else
        if(s[i][i]=='T')brt++;
        if(brx==4||(brx==3&&brt==1))
        {l=1;printf("Case #%d: X won\n",t);}
        if(bro==4||(bro==3&&brt==1))
        {printf("Case #%d: O won\n",t);l=1;}
        
        if(l)continue;
        brx=brt=bro=0;
        for(i=0;i<4;i++)
        if(s[i][3-i]=='.')
        {dot=1;}
        else
        if(s[i][3-i]=='X')brx++;
        else
        if(s[i][3-i]=='O')bro++;
        else
        if(s[i][3-i]=='T')brt++;
        if(brx==4||(brx==3&&brt==1))
        {l=1;printf("Case #%d: X won\n",t);}
        if(bro==4||(bro==3&&brt==1))
        {printf("Case #%d: O won\n",t);l=1;}
        if(l)continue;
        if(dot){printf("Case #%d: Game has not completed\n",t);continue;}
        printf("Case #%d: Draw\n",t);
    }
    return 0;
}