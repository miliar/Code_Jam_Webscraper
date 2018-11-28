#include<iostream>
using namespace std;
int rowcheck(int,int);
int columncheck(int,int);
int a[101][101],b,b1,c,t,m,f,n,k=1;
int main()
{
    int i,j;
  freopen("B-large.in","r",stdin);
  freopen("output121.in","w",stdout);
    cin>>t;
    do
    {
              f=0;
              cin>>n>>m;
              for(i=0;i<n;i++)
              {
                   for(j=0;j<m;j++)
                      cin>>a[i][j];
              }
              for(i=0;i<n;i++)
              {
                   for(j=0;j<m;j++)
                    {
                                     b=rowcheck(i,j);
                                     b1=columncheck(i,j);                          
      //                                             cout<<b<<" "<<b1<<endl; 
                                     if(!(b==1 || b1==1 )){   f=1;}
                                     if(f==1)
                                     {
                                             cout<<"Case #"<<k<<": NO\n";
                                             j=m;
                                             i=n;
                                     }
                    }    
              }
              if(f==0)
               cout<<"Case #"<<k<<": YES\n";             
     }while(k++!=t);
     return 0;
}
int rowcheck(int p,int q)
{   c=0;
    int j;
    //cout<<p<<" "<<q<<endl;
    for(j=0;j<m;j++)
    {
                    if(a[p][j]>a[p][q])   return 0;//    c++;
    }
    //cout<<"c r ="<<c<<endl;
    return 1;   
}
int columncheck(int p,int q)
{   c=0;
    int i;
  //  cout<<p<<" "<<q<<endl;
    for(i=0;i<n;i++)
    {
                    if(a[i][q]>a[p][q]) return 0;//          c++;
    }//cout<<"  c c="<<c<<endl;
    return 1;
}              
                      
    
