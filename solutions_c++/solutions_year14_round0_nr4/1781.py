#include <iostream>
#include <algorithm>
using namespace std;
double A[1005];
double B[1005];
int flag[1005]; 
int N;
int war()
{
    int sum=0;
    int i;
    int j;
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
           if(B[j]>A[i]&&flag[j]!=1)
           {
              break;
           }
        }
        if(j==N)//
        {
           return N-sum;
        }
        else
        {
           flag[j]=1;
           sum++;
        }
    }
    return N-sum;
}
int deceitwar()
{
    int sum=0;//lose time
    int i=0;
    int j=0;
    
    while(i<N)
    {
           if(A[i]<B[j])
           {
              sum++;
              i++;
           }
           else
           {
               i++;
               j++;
           }
    }
    return N-sum;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("xx4large.out","w",stdout);
    int i;
    int T;
    int x;
    int y;
    int z;
    cin>>T;
    x=0;
    while(T--)
    {
        y=0;z=0;
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
        memset(flag,-1,sizeof(flag));
        cin>>N;
        for(i=0;i<N;i++)
          cin>>A[i];
        for(int i=0;i<N;i++)
          cin>>B[i];
        sort(A,A+N);  
        sort(B,B+N);  
        
        y=deceitwar();
        z=war();
        
        x++;
        printf("Case #%d: %d %d\n",x,y,z);
    }
  fclose(stdin);
  fclose(stdout);
    return 0;
}
