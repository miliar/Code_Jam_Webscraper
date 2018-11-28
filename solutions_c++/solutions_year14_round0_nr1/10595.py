#include<iostream>
using namespace std;
#include<map>
int a[4][4],b[4][4];
int val1,val2;
int res()
{
       int count = 0;
       int i;
       map<int,int> m;
       bool flag = false;
       int r;
       for(i=0;i<4;i++)
              m[ a[val1-1][i] ] = 1;
       for(i=0;i<4;i++)
              if(m [ b[val2-1][i] ])
       {
              count++;
              flag = true;
              r = b[val2-1][i];
       }
       if(flag == false)
              return -1;
       else if(count>1)
              return 0;
       else
              return r;
}
int main()
{
       int t,k,i,j;
       cin>>t;
       for(k=1;k<=t;k++)
       {
              cin>>val1;
              for(i=0;i<4;i++)
                     for(j=0;j<4;j++)
                     cin>>a[i][j];
              cin>>val2;
              for(i=0;i<4;i++)
                     for(j=0;j<4;j++)
                     cin>>b[i][j];
              cout<<"Case #"<<k<<": ";
              int re = res();
              if(re == -1)
                     cout<<"Volunteer cheated!"<<endl;
              else if(re == 0)
                     cout<<"Bad magician!"<<endl;
              else
                     cout<<re<<endl;
       }
       return 0;
}
