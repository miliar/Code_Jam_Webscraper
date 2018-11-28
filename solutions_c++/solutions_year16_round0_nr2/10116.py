#include<iostream>

using namespace std;


    int main()
    {
       // Scanner sc=new Scanner(System.in);
        //String k=sc.nextLine();
      
      freopen("B-small-attempt0.in","r",stdin);
	    freopen("B-small-attempt0.out","w",stdout);
       
       int c,y=-1,j;
       
       cin>>j;
       
       c=j;
       string k;
         int p[j]={0};
         
         
         while(j--)
         {	y++;
		 	cin>>k;
    
        int t=0,u=0;
        
     
        
        for(int i=0;k[i]!='\0';i++)
        {
            
            if(k[i]=='-')
           { t=i;
               
               if(t==0)
               {
               u=0;
               for(int r=t;r<k[r]!='\0';r++)
               if(k[r]=='-')
               {k[r]='+';
               u++;
            }
            else break;
               i=i+u;
               p[y]++;
               
            } 
               else{
       
       // for(int i=0;i<t;i++)
       u=0;
        //k.setCharAt(i)='-';
        for(int r=t;k[r]!='\0';r++)
               if(k[r]=='-')
               {k[r]='+';
               u++;
            }
            else break;
               i=i+u;
        
        p[y]=p[y]+2;
    }}
    
    
    }
}
for(int g=0;g<c;g++)
    cout<<"Case #"<<g+1<<": "<<p[g]<<endl;

}
    
