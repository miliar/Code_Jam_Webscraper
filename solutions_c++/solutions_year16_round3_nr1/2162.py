#include<iostream>

#include<vector>


 using namespace std;
int main()
{
int t,n,p[27],i,j=0,k,l,max,f,m,c;
cin>>t;
while(t--)
{   j++;
    cin>>n;
    cout<<"Case #"<<j<<": ";
    m=0;c=n;
    for(i=0;i<n;i++)
    {
        cin>>p[i];
        m+=p[i];
    }
    while(m>0)
    {
  
    if(m==3 && c==3)
    {
          max=0;k=-1;l=-1;f=0;
           for(i=0;i<n;i++)
            {
                if(p[i]>max)
                {
                    max=p[i];
                    k=i;f=0;
                }
              
            }
              cout<<(char)(65+k)<<" ";
                p[k]-=1;
                if(p[k]==0)
                c-=1;;
                m-=1;
    }     
    else
    if(c==2 && m%2==1)
    {
         
              max=0;k=-1;l=-1;f=0;
        for(i=0;i<n;i++)
        {
            if(p[i]>0 && f==0)
            {
               
                k=i;f=1;
            }
            else
            if(p[i]>0 && f==1)
            {
                l=i;
                f=1;break;
            }
        }
            if(p[k]>p[l])
             { cout<<(char)(65+k)<<" ";
                    p[k]-=1;   
                    if(p[k]==0)
                    c--;
                    
                    m-=1;
             }
             else
             {cout<<(char)(65+l)<<" ";
                    p[l]-=1;   
                    if(p[l]==0)
                    c--;
                    
                    m-=1;
                 
             }
    }
    else
    if(c==1 && m==1)
    {
               max=0;k=-1;l=-1;f=0;
        for(i=0;i<n;i++)
        {
            if(p[i]>0 && f==0)
            {
               
                k=i;f=1;break;
            }
           
        }
         cout<<(char)(65+k)<<" ";
          p[k]-=1;   
                if(p[k]==0)
                c--;
               
                m-=1;
         
    }
    else
    {
          max=0;k=-1;l=-1;f=0;
        for(i=0;i<n;i++)
        {
            if(p[i]>max)
            {
                max=p[i];
                k=i;f=0;
            }
            else
            if(p[i]==max)
            {
                l=i;
                f=1;
            }
        }
        
        if(f==0)
            {
                cout<<(char)(65+k)<<(char)(65+k)<<" ";
                p[k]-=2;
                if(p[k]==0)
                c-=2;;
                m-=2;
            }
        else
            {
                cout<<(char)(65+k)<<(char)(65+l)<<" ";
                p[k]-=1;    p[l]-=1;
                if(p[k]==0)
                c--;
                if(p[l]==0)
                c--;
                m-=2;
            }
    }
    
    }
    cout<<"\n";
}


return 0;
} 
