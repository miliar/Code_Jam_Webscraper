#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int c=1;c<=cases;c++)
    {
        int i,j,res=0,ans,ans1,ret;
        int a[4][4],a1[4][4];
        vector <int>e,e1;
        scanf("%d",&ans);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        for(i=0;i<4;i++)
            e.push_back(a[ans-1][i]);
        scanf("%d",&ans1);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a1[i][j]);
        for(j=0;j<4;j++)
            e1.push_back(a1[ans1-1][j]);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {    if(e[i]==e1[j])
                 {
                    ret=e[i];    
                    res++;
                    break;
                 }
            }
        }
        //cout<<"res "<<res<<"\n";
        if(res==1)
            printf("Case #%d: %d\n",c,ret);
        else if(res>1)
            printf("Case #%d: Bad magician!\n",c);
        else
            printf("Case #%d: Volunteer cheated!\n",c);
    }
    //system("pause");
}   
