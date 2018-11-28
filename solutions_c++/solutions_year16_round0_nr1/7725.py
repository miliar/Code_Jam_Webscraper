#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>

#define ll long long

using namespace std;

ll A[21],B[105],BB[105],C[105];

int main()
{ll n,t,count,dig,c,carry,length; 
 string ch;
 ofstream fout;
 ifstream fin;
 fin.open("code_1.txt");
 fout.open("code1");
 if(!fin.is_open())
  {cout<<"lol";return 0;}
  
  fin>>t;
  getline(fin,ch);
  
   for(ll popo=1;popo<=t;popo++)
    { getline(fin,ch);
        for(ll i=0;i<=9;i++)
        A[i]=0;
        c=100;
	  count=0;
	  
	  for(ll i=0;i<ch.size();i++)
        {dig=ch[i]-48;
        if(A[dig]==0)
         count++;
		A[dig]=1;
		BB[c]=dig;
		c--;
        
	   }
	     c++;
	     ll p=0;
	     for(ll i=c;i<=100;i++)
	      if(BB[i]==0)
	       p++;
	       
	       if(p==100-c+1)
	        {fout<<"Case #"<<popo<<": "<<"INSOMNIA"<<"\n";continue;}
	     
	     length=c;
	   for(ll i=c,j=100;i<=100;i++,j--)
	    {B[i]=BB[j];C[i]=BB[j];}
    	
    	while(1)
    	{ carry=0;
    	   ll i;
    	    for(i=100;i>=c;i--)
        	 {C[i]=C[i]+B[i]+carry;
    	      if(C[i]>9)
    	       {   carry=C[i]/10;
    	           C[i]=C[i]%10;
    	       }
    	        else
    	         carry=0;
    	         
    	         if(A[C[i]]==0)
    	          count++;
    	          A[C[i]]=1;
        	 }
        	 
        	 for(ll j=i;j>=length;j--)
        	  {C[j]=C[j]+carry;
        	    if(C[j]>9)
        	     {carry=C[j]/10;
        	      C[j]=C[j]%10;
        	     }
        	      else 
        	       carry=0;
        	    if(A[C[j]]==0)
        	     count++;
        	     A[C[j]]=1;
        	  }
        	  
        	   if(carry!=0)
        	    {length--;
        	     C[length]=carry;
        	      if(A[carry]==0)
        	       {count++;A[carry]=1;}
        	    }
    	          if(count==10)
    	           break;
    	    
    	}
    	fout<<"Case #"<<popo<<": ";
		for(ll i=length;i<=100;i++)
		 fout<<C[i];
		 fout<<"\n";
	   }
	   
	   fin.close();
	   fout.close();
	   return 0;
	   
}
	   	  	
	   
