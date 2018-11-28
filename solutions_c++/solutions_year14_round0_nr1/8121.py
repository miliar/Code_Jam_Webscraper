


#include <iostream>

using namespace std;

int findSameNum(int a[4],int b[4],int & r)
{
    int count = 0;
    for(int i = 0;i < 4;++i)
    {
        for(int j = 0;j < 4;++j)
        {
              if(a[i] == b[j])
              {
                      count++;
                      r = a[i];
                      break;        
              }        
        }        
    
    }    
    return count;    
}

int main()
{
    int n,m;
    int a[4];
    int b[4];
    int x;
    cin>>n;
    int iNth = 0;
    while(iNth < n)
    {
              for(int k = 0;k<2;++k)
              {
                  cin>>m;         
                  for(int i = 0;i < 4;++i)
                  {
                          for(int j = 0;j < 4;++j)
                          {
                              cin>>x;
                              if(i == m-1 && 0 == k)
                              {
                                   a[j] = x;    
                              }
                              else if(i == m-1 && 1 == k)                                        
                              {
                                   b[j] = x;
                              }
                          }
                  }                      
              }
              int  r = 0;
              cout<<"Case #"<<iNth+1<<": ";
              switch(findSameNum(a,b,r))
              {
               case 0:
                      cout<<"Volunteer cheated!"<<endl;
                      break;
               case 1:
                      cout<<r<<endl;         
                      break;
               default:
                      cout<<"Bad magician!"<<endl;
              }
              iNth++;
    }    
    return 0;   
}
