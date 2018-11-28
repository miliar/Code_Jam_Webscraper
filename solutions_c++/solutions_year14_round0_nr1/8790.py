#include<stdio.h>
#include<iostream>
using namespace std;
int grid1[5][5];
int grid2[5][5];
int ans[2];
int main()
{
    bool flag;
    int t;
    cin>>t;
    int testcase=1;
    while(t--)
    {
        flag=0;
        cin>>ans[0];
ans[0]--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        cin>>grid1[i][j];

        cin>>ans[1];
ans[1]--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        cin>>grid2[i][j];

int count=0;
int answer;
for(int i=0;i<4;i++)
{
if(count>1)break;
    for(int j=0;j<4;j++)
    {
//cout<<grid1[ans[0]][i]<<" "<<grid2[ans[1]][j]<<"\n";
        if(grid1[ans[0]][i]==grid2[ans[1]][j])
        {
            count++;
            answer=grid1[ans[0]][i];
            break;

        }
    }
}
//cout<<answer<<"\n";


if(count==0)
printf("Case #%d: Volunteer cheated!\n",testcase++);
else if(count==1)
printf("Case #%d: %d\n",testcase++,answer);
else if(count>1)
printf("Case #%d: Bad magician!\n",testcase++);

    }

    return 0;
}
