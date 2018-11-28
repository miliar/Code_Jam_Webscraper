#include<iostream>
#include<algorithm>
int N,M;
using namespace std;
int a[1000][1000];
int columncheck(int element,int j)
{
    int flag=0;
    for(int i=0;i<N;i++)
            if(a[i][j]>element)flag=1;
    if(flag==1)return 0;
    else return 1;
}
int rowcheck()
{
    int count =0;
    for(int i=0;i<N;i++)
    {
            int *t = max_element(a[i],a[i]+M);
            int max = *t;
            
            int flag1,flag2;
            int col=1;
            flag1=flag2=0;
            for(int j=0;j<M;j++)
            {
                    if(a[i][j]<max){flag1 =1;col = columncheck(a[i][j],j);}
                    if(col!=1){ flag2 = 1;   break; }        
            }
            if(flag2==0)count++;
    }
    if(count==N)return 1;
    else return 0;
}
int main()
{
    
    int T;
    cin>>T;
    int I=1;
    while(T--)
    {
              
              cin>>N;
              cin>>M;
              for(int i=0;i<N;i++)
                      for(int j=0;j<M;j++)
                              cin>>a[i][j];
              int sol = rowcheck();
              cout<<"Case #"<<I<<": ";
              I++;
              if(sol==1)cout<<"YES"<<endl;
              else cout<<"NO"<<endl;
    }
    return 0;
}
              
