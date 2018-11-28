#include<iostream>
using namespace std;

int main()
{
    int i,n,m,t,j,k,flag,cnt1,cnt2,emp;
    char a[10][10];
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cin>>t;
    k=1;
    while(t--)
    {
              
    for(i=0;i<4;i++)
    {
    for(j=0;j<4;j++)
    {cin>>a[i][j];}
    }
    
    
    flag=0;emp=0;
    for(i=0;i<4;i++)
    {
                    cnt1=0;cnt2=0;
                    for(j=0;j<4;j++)
                    {
                                    if(a[i][j]=='T')
                                    {cnt1++;cnt2++;}
                                    
                                    else if(a[i][j]=='X')
                                    cnt1++;
                                    
                                    else if(a[i][j]=='O')
                                    cnt2++;    
                                    else 
                                    emp++;                                
                    }
                    
                    if(cnt1==4) 
                    {cout<<"Case #"<<k<<": X won"<<endl; flag=1;break;}
                    
                    if(cnt2==4) 
                    {cout<<"Case #"<<k<<": O won"<<endl; flag=1;break;}
                    
    }
//    cout<<"hii0";cout<<"flag="<<flag;
    if(!flag)
    {
    for(j=0;j<4;j++)
    {//cout<<"j="<<j<<"\t";
                    cnt1=0;cnt2=0;
                    for(i=0;i<4;i++)
                    {
                                    if(a[i][j]=='T')
                                    {cnt1++;cnt2++;}
                                    
                                    else if(a[i][j]=='X')
                                    cnt1++;
                                    
                                    else if(a[i][j]=='O')
                                    cnt2++;                                    
                    }
                    
                    if(cnt1==4) 
                    {cout<<"Case #"<<k<<": X won"<<endl; flag=1;break;}
                    
                    if(cnt2==4) 
                    {cout<<"Case #"<<k<<": O won"<<endl; flag=1;break;}//cout<<"j="<<j<<"\t";
    }    
 //                   cout<<"hii1bc";cout<<"j="<<j;

    }   
    
    if(!flag)
    {
             i=0;j=0;cnt1=0;cnt2=0;
    while(i<4 && j<4)
    {
               if(a[i][j]=='T')
               {cnt1++;cnt2++;}
                                    
               else if(a[i][j]=='X')
               cnt1++;
                                    
               else if(a[i][j]=='O')
               cnt2++;
               i++;j++;        
                                  
    }
    if(cnt1==4) 
    {cout<<"Case #"<<k<<": X won"<<endl; flag=1;}
                   
    if(cnt2==4) 
    {cout<<"Case #"<<k<<": O won"<<endl; flag=1;}
   //                     cout<<"hii2";

    }
    

    if(!flag)
    {
             i=0;j=3;cnt1=0;cnt2=0;
    while(i<4 && j>=0)
    {
               if(a[i][j]=='T')
               {cnt1++;cnt2++;}
                                    
               else if(a[i][j]=='X')
               cnt1++;
                                    
               else if(a[i][j]=='O')
               cnt2++;
               i++;j--;           
    }
    if(cnt1==4) 
    {cout<<"Case #"<<k<<": X won"<<endl; flag=1;}
                   
    if(cnt2==4) 
    {cout<<"Case #"<<k<<": O won"<<endl; flag=1;}

     //               cout<<"hii3";

    }
    
    if(!flag)
    {
             if(emp==0)
             cout<<"Case #"<<k<<": Draw"<<endl;
             else 
             cout<<"Case #"<<k<<": Game has not completed"<<endl;
               
    }   
    k++;
}
    return 0;    
}
