#include<stdio.h>
int main()
{

int t;
scanf("%d",&t);
for(int l=1;l<=t;l++)
{

    int arr1[4][4],arr2[4][4];
    int first,second;

    scanf("%d",&first);

    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        scanf("%d",&arr1[i][j]);

    scanf("%d",&second);

    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        scanf("%d",&arr2[i][j]);
    bool flag=false;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
    {
        if(arr2[second-1][i]==arr1[first-1][j])
        {
            flag=true;
            break;
        }
    }

    if(flag==true)
        break;

    }

if(flag==false){
    printf("Case #%d: Volunteer cheated!\n",l);
    continue;}



    int count=0;
    for(int j=0;j<4;j++)
    {
        for(int k=0;k<4;k++)
        if(arr2[second-1][j]==arr1[first-1][k])
        {
            count++;
        }

    }

    if(count!=1)
    {
    printf("Case #%d: Bad magician!\n",l);
    continue;
    }




int ans=0;
for(int i=0;i<4;i++){
    for(int j=0;j<4;j++)
    if(arr1[first-1][i]==arr2[second-1][j]){
    ans=arr1[first-1][i];
    break;}
    if(ans!=0)
        break;

}

printf("Case #%d: %d\n",l,ans);


}
return 0;}
