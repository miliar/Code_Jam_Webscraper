#include<iostream>
using namespace std;
int a[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
       int n;
       cin>>n;
       int x;
       memset(a,0,sizeof(a));
       for(int i=1;i<=4;i++)
       {
         for(int j=1;j<=4;j++)
         {
          scanf("%d",&x);
          if(i==n)
           a[x]++;
         }
       }
       cin>>n;
       for(int i=1;i<=4;i++)
       {
         for(int j=1;j<=4;j++)
         {
          scanf("%d",&x);
          if(i==n)
           a[x]++;
         }
       }
       int key=0;
       int sum=0;
       for(int i=1;i<=16;i++)
         if(a[i]==2)
           sum++,key=i;
       printf("Case #%d: ",cas++);
       if(sum==0)
           cout<<"Volunteer cheated!"<<endl;
       else if(sum>=2)
           cout<<"Bad magician!"<<endl;
       else
           cout<<key<<endl;
    }
    return 0;
}
                 
           
