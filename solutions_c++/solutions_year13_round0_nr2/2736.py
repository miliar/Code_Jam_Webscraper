#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
using namespace std;
int main()
{
    int t,it=1;
    int one=1,two=2;
    int r,c,i,j;
    
    scanf("%d",&t);
    
	
	while(t--)
    {
        scanf("%d%d",&r,&c);
        
		int a[r+1][c+1];
        
		bool foo[r+1][c+1];
        
		
		memset(foo,false,sizeof(foo));
        
		
		for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                scanf("%d",&a[i][j]);
                if(a[i][j]==2)
                    foo[i][j]=true;
            }
        }
        
        
           bool flag;
        for(i=0;i<c;i++)
        {
			flag=true;
            if(a[0][i]==1)
            {
                
                for(j=0;j<r;j++)
                    if(a[j][i]!=1)flag=false;
                    
             if(flag)
				for(j=0;j<r;j++)
					foo[j][i]=true;   
             
        	}
        
		}
		
		 for(i=0;i<r;i++)
        {
			flag=true;
            if(a[i][0]==1)
            {
                
                for(j=0;j<c;j++)
                    if(a[i][j]!=1)flag=false;
                    
             if(flag)
				for(j=0;j<c;j++)
					foo[i][j]=true;   
             
        	}
        
		}
		
        
        bool final=true;
        
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(!foo[i][j])final=false;
            }
        }
        
        if(final) printf("Case #%d: YES\n",it++);
        else printf("Case #%d: NO\n",it++);
        
        
    
    
    }
return 0;

}
