#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<map>
using namespace std;

int lawn[20][20];
int row_has_two[20];
int col_has_two[20];

int main()
{
    freopen("C:\\Users\\vivek\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\vivek\\Desktop\\out.txt","w",stdout);
    int i,j,t,T,N,M,cnt=0;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        for(i=0;i<20;i++) {row_has_two[i]=0; col_has_two[i]=0; }
        cin>>N>>M;
        for(i=0;i<N;i++)
        {
           for(j=0;j<M;j++) 
           {
              cin>>lawn[i][j];
              if(lawn[i][j]==2) { row_has_two[i]=1; col_has_two[j]=1; }
           }
        }
        
        for(i=0;i<N;i++)
        {
           if(row_has_two[i]==1)
           {
              for(j=0;j<M;j++)
              {
                 if(lawn[i][j]==1 && col_has_two[j]==1) cnt++;
              }
           }
        }
        cout<<"Case #"<<t<<": ";
        if(cnt>0) cout<<"NO"<<endl;
        else cout<<"YES"<<endl;                
        cnt=0;
    }
    return 0;
}

                     
