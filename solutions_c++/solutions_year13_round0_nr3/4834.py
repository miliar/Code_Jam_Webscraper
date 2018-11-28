#include<cstdio>
bool ispalin(int i);
int main()
{
    
    int a[1002]={0};
    /*for(int i=1;i<=3;i++)
    {
            a[i*i]=1;
            //if(ispalin(i)==true)a[i*i]=1;
    }*/
    a[1]=1;a[4]=1;a[9]=1;
    a[121]=1;a[484]=1;
    for(int i=1;i<1002;i++)
    {
            a[i]+=a[i-1];
    }
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
    int x,y;
    scanf("%d%d",&x,&y);
    printf("Case #%d: %d\n",i,a[y]-a[x-1]);
}}
/*bool ispalin(int i)
{
     int j=0,x=i;
     while(x!=0)
     {
                j*=10;
                j+=x%10;
                x/=10;
     }
     if(i==j)return true;
     else return false;
}*/
