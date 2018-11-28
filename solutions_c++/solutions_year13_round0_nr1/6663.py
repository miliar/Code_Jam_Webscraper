#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int n,j,i,k,d,c1,c2,c3,f=0;
    string str[4];
    cin>>n;
    for(j=1;j<=n;j++)
    {
    for(i=0;i<4;i++)
    {
         cin>>str[i];
    }
    for(d=0;d<4;d++)
    {
    c1=0;c2=0;c3=0;
    for(k=0;k<4;k++)
    {
         if(str[d][k]=='X')
         c1++;
         else if(str[d][k]=='O')
         c2++;
         else if(str[d][k]=='T')
         c3++;   
    }       
    if((c1==3 && c3==1) || c1==4){
    f=1;
    break;
    }
    else if((c2==3 && c3==1) || c2==4){
    f=2;
    break;
    }
    else
    f=0;
    }
    if(f==0){
    for(d=0;d<4;d++)
    {
    c1=0;c2=0;c3=0;
    for(k=0;k<4;k++)
    {
         if(str[k][d]=='X')
         c1++;
         else if(str[k][d]=='O')
         c2++;
         else if(str[k][d]=='T')
         c3++;   
    }       
    if((c1==3 && c3==1) || c1==4){
    f=1;
    break;
    }
    else if((c2==3 && c3==1) || c2==4){
    f=2;
    break;
    }
    else
    f=0;
    }
    }
    if(f==0){
    c1=0;c2=0;c3=0;
    k=3;
    for(d=0;d<4;d++)
    {
         if(str[d][k]=='X')
         c1++;
         else if(str[d][k]=='O')
         c2++;
         else if(str[d][k]=='T')
         c3++;   
         k--;
    }       
    if((c1==3 && c3==1) || c1==4)
    f=1;
    else if((c2==3 && c3==1) || c2==4)
    f=2;
    else
    f=0;    
    } 
    if(f==0){      
    c1=0;c2=0;c3=0;
    k=0;
    for(d=0;d<4;d++)
    {
         if(str[d][k]=='X')
         c1++;
         else if(str[d][k]=='O')
         c2++;
         else if(str[d][k]=='T')
         c3++;   
         k++;
    }       
    if((c1==3 && c3==1) || c1==4)
    f=1;
    else if((c2==3 && c3==1) || c2==4)
    f=2;
    else
    f=0;           
    }
    if(f==1)
    cout<<"Case #"<<j<<": X won\n";
    else if(f==2)
    cout<<"Case #"<<j<<": O won\n";
    else
    {
        for(d=0;d<4;d++)
        {
          for(k=0;k<4;k++)
          { 
              if(str[d][k]=='.'){
              f=4;
              cout<<"Case #"<<j<<": Game has not completed\n";
              d=4;
              }  
          }
        }      
        if(f!=4)
        cout<<"Case #"<<j<<": Draw\n";
    }
    }
    system("pause");
}
                  
                     
                        
