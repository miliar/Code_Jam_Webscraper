//Author: Jaydeep
//
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define vec vector<ll>
#define matrix vector<vector<ll> >
#define pritnf printf
#define pb push_back


char s[100005];

char p[50][50]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

ll l;



void del(ll i1)
{
    int i;
    
    for(i=i1;i<l-1;i++)
        s[i]=s[i+1];
    
    l--;
    s[l]='\0';
    
    
}


void dele(char *s1)
{
    int i,j;
    
    int x[10]={0};
    
    ll l1=strlen(s1);
    
    for(i=0;i<l;)
    {
        ll k=0;
        
        for(j=0;j<l1;j++)
        {
            if(s[i]==s1[j] && x[j]==0)
            {
                del(i);
                k++;
                x[j]=1;
                break;
            }
            
        }
        
        
        i=i+1-k;
        
    }
    
    
    
}





int main()
{
	ll a[200005],t,i=0,j,x,y,z,count=0,flag=0,ans=0,sum=0,n,t1;
 	
	
	scanf("%lld",&t);
	
    for(t1=0;t1<t;t1++)
	{
	    scanf("%s",&s);
	    
	    l=strlen(s);
	    
	    
	    ll c[10]={0};
	    
	    for(i=0;i<l;)
	    {
	        
	        if(s[i]=='Z')
	            dele(p[0]),c[0]++,i=i+1-strlen(p[0]);
	        
	        else if(s[i]=='W')
	            dele(p[2]),c[2]++,i=i+1-strlen(p[2]);
	        
	        else if(s[i]=='U')
	            dele(p[4]),c[4]++,i=i+1-strlen(p[4]);
	        
	        
	        else if(s[i]=='X')
	            dele(p[6]),c[6]++,i=i+1-strlen(p[6]);
	            
	        else if(s[i]=='G')
	            dele(p[8]),c[8]++,i=i+1-strlen(p[8]);
	        
	        else
	            i++;
	        
	  //      printf("*%s ",s);
	    }
	    
	    
	    
	 //   printf("%s ",s);
	    
	    for(i=0;i<l;)
	    {
	        
	        if(s[i]=='O')
	            dele(p[1]),c[1]++,i=i+1-strlen(p[1]);
	        
	        else if(s[i]=='T')
	            dele(p[3]),c[3]++,i=i+1-strlen(p[3]);
	            
	        else if(s[i]=='F')
	            dele(p[5]),c[5]++,i=i+1-strlen(p[5]);
	        
	        else if(s[i]=='S')
	            dele(p[7]),c[7]++,i=i+1-strlen(p[7]);
	        
	        else
	            i++;
	        
	    }
	    
	  //  printf("%s ",s);
	    
	    for(i=0;i<l;)
	    {
	        if(s[i]=='I')
	            dele(p[9]),c[9]++,i=i+1-strlen(p[9]);
	        
	        else
	            i++;
	    }
	    
	  //  printf("%s ",s);
	    
	    
	    
	    
	    
	    
		pritnf("Case #%lld: ",t1+1,ans);
		
		for(i=0;i<10;i++)
		{
		    for(j=0;j<c[i];j++)
		        printf("%lld",i);
		    
		    
		}
		pritnf("\n");
		
	}
	
	
	return 0;
}
