#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    int t,u,i,j,x,flag,a[5][5]={0},count;
    char temp[10],c;
    cin>>t;
    for(u=0;u<t;u++)
    {
        count=0;
        flag=1;
        for(i=0;i<4;i++)
        {
            cin>>temp;
            for(j=0;j<4;j++)
            {
                if(temp[j]=='X')
                a[i][j]=1;
                else
                if(temp[j]=='O')
                a[i][j]=0;
                else
                if(temp[j]=='.')
                {
                    a[i][j]=-1;
                    count++;
                }
                else
                if(temp[j]=='T')
                a[i][j]=2;
                else
                {
                flag=0;
                a[i][j]=-2;
                }
            }
        }
        //cout<<temp[5];
        c=getchar();
       // cout<<c;
        //for(i=0;i<4;i++)
        //{
          //  for(j=0;j<4;j++)
            //cout<<a[i][j]<<" ";
            //cout<<endl;
        //}
        if(!flag)
        printf("Case #%d: Game has not completed",u+1);
        else
        {
           // cout<<"hi"<<endl;
                    flag=0;j=0;
            for(i=0;i<4;i++)
            {
                if(((a[i][j]==1)||(a[i][j]==2))&&((a[i][j+1]==1)||(a[i][j+1]==2))&&((a[i][j+2]==1)||(a[i][j+2]==2))&&((a[i][j+3]==1)||(a[i][j+3]==2)))
                {
                    //cout<<"hi"<<endl;
                    flag=1;
                    printf("Case #%d: X won",u+1);
                    break;
                }
                else
                if(((a[i][j]==0)||(a[i][j]==2))&&((a[i][j+1]==0)||(a[i][j+1]==2))&&((a[i][j+2]==0)||(a[i][j+2]==2))&&((a[i][j+3]==0)||(a[i][j+3]==2)))
                {
                    flag=1;
                    printf("Case #%d: O won",u+1);
                    break;
                }            
            }
            if(!flag)
            {
                i=0;
                for(j=0;j<4;j++)
                {
                if(((a[i][j]==1)||(a[i][j]==2))&&((a[i+1][j]==1)||(a[i+1][j]==2))&&((a[i+2][j]==1)||(a[i+2][j]==2))&&((a[i+3][j]==1)||(a[i+3][j]==2)))
                {
                    flag=1;
                    printf("Case #%d: X won",u+1);
                    break;
                }
                else
                if(((a[i][j]==0)||(a[i][j]==2))&&((a[i+1][j]==0)||(a[i+1][j]==2))&&((a[i+2][j]==0)||(a[i+2][j]==2))&&((a[i+3][j]==0)||(a[i+3][j]==2)))
                {
                    flag=1;
                    printf("Case #%d: O won",u+1);
                    break;
                }            
                }
            }
            if(!flag)
            {
                if(((a[0][0]==0)||(a[0][0]==2))&&((a[1][1]==0)||(a[1][1]==2))&&((a[2][2]==0)||(a[2][2]==2))&&((a[3][3]==0)||(a[3][3]==2)))
                {
                    flag=1;
                    printf("Case #%d: O won",u+1);
                    break;
                }            
                else
                if(((a[0][3]==0)||(a[0][3]==2))&&((a[1][2]==0)||(a[1][2]==2))&&((a[2][1]==0)||(a[2][1]==2))&&((a[3][0]==0)||(a[3][0]==2)))
                {
                    flag=1;
                    printf("Case #%d: O won",u+1);
                    break;
                }
                else
                if(((a[0][0]==1)||(a[0][0]==2))&&((a[1][1]==1)||(a[1][1]==2))&&((a[2][2]==1)||(a[2][2]==2))&&((a[3][3]==1)||(a[3][3]==2)))
                {
                    flag=1;
                    printf("Case #%d: U won",u+1);
                    break;
                }            
                else
                if(((a[0][3]==1)||(a[0][3]==2))&&((a[1][2]==1)||(a[1][2]==2))&&((a[2][1]==1)||(a[2][1]==2))&&((a[3][0]==1)||(a[3][0]==2)))
                {
                    flag=1;
                    printf("Case #%d: U won",u+1);
                    break;
                }            
            }
            if((!flag)&&(count==0))
            printf("Case #%d: Draw",u+1);
            else
            if(!flag)
            printf("Case #%d: Game has not completed",u+1);
        }
        cout<<endl;
    }
	return 0;
}