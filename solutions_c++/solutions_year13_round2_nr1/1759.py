#include<iostream>
using namespace std;
int main()
{
 //freopen("input.txt","r",stdin);
 //freopen("output.txt","w",stdout);
 int t,z=1;
 cin>>t;
 while(t--)
 {
        int a,n;
        cin>>a>>n;
        int m[n];
        for(int i=0;i<n;++i)
                cin>>m[i];
        for(int i=0;i<n;++i)
                for(int j=i+1;j<n;++j)
                        if(m[i]>m[j])
                        {
                         int temp=m[i];
                         m[i]=m[j];
                         m[j]=temp;             
                        }   
        int count=0,count1=0,a1=a;
        for(int i=0;i<n;++i)
        {
         if(a>m[i])
         {
          //count++;
          a+=m[i];          
         }        
         else if((a+a-1)>m[i])
         {
          count+=1;
          a+=a-1+m[i];     
         }
         else
         {
          count+=n-i;
          break;    
         }
        }
        for(int i=0;i<n;++i)
        {
         if(a1>m[i])
         {
          //count++;
          a1+=m[i];          
         }        
         else if((a1+a1-1)>m[i])
         {
          count1+=1;
          a1+=a1-1+m[i];     
         }
         else
         {
          count1+=1;
          a1+=a1-1;
          i--;
          //break;    
         }
        }
        int ans;
        if(count>count1)
        ans=count1;
        else
        ans=count;
        cout<<"Case #"<<z++<<": "<<ans<<endl;
 }
 return 0;    
}
