#include<iostream.h>
#include<conio.h>
#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
     freopen("outp.in","w",stdout);
    
    int rf,ri,i,j,k,c,n,m,val;
    int a[4][4],b[4][4];
    
    cin>>n;
    
    for( m=0;m<n;m++)
    {
         c=0;
            cin>>ri;
            
            for(i=0;i<4;i++)
            for( j=0;j<4;j++)
            cin>>a[i][j];
            
            cin>>rf;
            
            for(i=0;i<4;i++)
            for( j=0;j<4;j++)
            cin>>b[i][j];
            
           
             
             for(i=0;i<4;i++)
             {
                    for(j=0;j<4;j++)         
             {
                             if(a[ri-1][i]==b[rf-1][j])
                             {
                                                 if(c==0)
                                                 {
                                                     val=a[ri-1][i];       
                                                 }
                             c++;
                             }
                             
             }
             }
             
             if(c==0)
             cout<<"Case #"<<m+1<<": Volunteer cheated!"<<"\n";
            
             
             if(c>1)
             cout<<"Case #"<<m+1<<": Bad magician!"<<"\n";
             
             if (c==1)
             cout<<"Case #"<<m+1<<": "<<val<<"\n";
            
            
    }
    
    getch();
    return 0;
}
