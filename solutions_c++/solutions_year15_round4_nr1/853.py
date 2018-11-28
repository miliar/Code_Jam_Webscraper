#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair <int,int> ii;
#define N 100
char s[N + 5][N + 5];
int mark[N + 5][N + 5];
int Move(int i,int j,int r,int c,int id,char ch)
{
    //printf("%d %d %c\n",i,j,ch);
    if(i == 0 || j == 0 || i>r || j > c)
    {
        return 1;
    }
    //printf("%d %d %c %d\n",i,j,ch,mark[i][j]);
    if(s[i][j] != '.' && mark[i][j] != 0) return 0;
    mark[i][j] = id;
    char dir = ch;
    if(s[i][j] != '.') dir = s[i][j];
    int val = 0;

    switch(dir)
    {
        case '^':
        val = Move(i-1,j,r,c,id,'^');
        break;
        case '>':
        val = Move(i,j+1,r,c,id,'>');
        break;
        case 'v':
        val = Move(i+1,j,r,c,id,'v');
        break;
        case '<':
        val = Move(i,j-1,r,c,id,'<');
        break;
    }
    return val;
}
int main()
{
    freopen("C:\\Users\\dell\\Downloads\\inputa.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputa2.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++)
    {
        int ans = 0,i,j,r,c,k;
        scanf("%d %d",&r,&c);
        for(i = 1 ; i<=r ; i++)
        {
            scanf("%s",s[i]+1);
            for(j = 1 ; j<=c ; j++)
            {
                mark[i][j] = 0;
            }
        }
        int flag = 1;
        for(i = 1 ; i<=r ; i++)
        {
            for(j = 1 ; j<=c ; j++)
            {
                if(s[i][j] == '.') continue;

                int cntc = 0;
                for(k = 1 ; k<=c ; k++)
                {
                    if(s[i][k] != '.') cntc++;
                }

                int cntr = 0;
                for(k = 1 ; k<=r ; k++)
                {
                    if(s[k][j] != '.') cntr++;
                }

                if(cntc == 1 && cntr == 1)
                flag = 0;
            }
        }

        if(flag == 1)
        {
            int id = 0;
            for(i = 1 ; i<=r ; i++)
            {
                for(j = 1 ; j<=c ; j++)
                {
                    if(s[i][j] != '.')
                    {
                        id++;
                        ans = ans + Move(i,j,r,c,id,s[i][j]);
                        //printf("--------------\n");
                    }
                }
            }
        }








        // Printing Starts here for the Test Case
        printf("Case #%d: ",t);
        // Print the result of the code here
        if(flag)printf("%d",ans);
        else printf("IMPOSSIBLE");
        //Don't do anything after this.
        printf("\n");

    }
    return 0;
}


