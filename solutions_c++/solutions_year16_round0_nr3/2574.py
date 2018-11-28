#include<iostream>
#include<bitset>
#include<math.h>
#define lld long long int
using namespace std;
lld chprim(lld n)
{ lld i;
for(i=2;i<=sqrt(n);i++)
 if(n%i==0)
  return i;
  return 0;
}

lld power(int a[],int n,int p)
{  int i; lld sum=0,flag;
 for(i=n-1;i>=0;i--)
  { if(a[i]==1)
   sum+=pow(p,n-1-i);
 } //cout<<"sum"<<sum<<endl;
    flag=chprim(sum); //cout<<" flag"<<flag<<endl;
    if(flag!=0)
      return flag;
   else
     return 0;
}

int main()
{ int t;
cin>>t;
while(t--)
{ int x,l,n,q,i,k,w=0,j,p,I,flag=1; lld ans[11];  
 cin>>n; cin>>j; 
  p=1<<n;
 cout<<"Case #1:"<<endl;
 for(i=1,q=1;i<p && q<=j;i++)
  { flag=1; 
     bitset<32>b(i); 
         if(b[0]==1 || b[n-1]==1)
	        continue;
	     else
	         b[0]=1; b[n-1]=1;
	//cout<<"#"<<q<<" "<<b<<endl;
	 int a[35]={0}; w=0; 
     for(l=n-1;l>=0;l--)
       a[w++]=b[l]; 
       for(I=2;I<=10;I++)
	     { ans[I]=power(a,n,I);
	        if(ans[I]==0)
	         { flag=0;  break; }
	     }
	     if(flag==0)
	     continue;
	     else
    {  for(k=0;k<n;k++)
         cout<<a[k];
        for(x=2;x<11;x++)
          cout<<" "<<ans[x];
          cout<<endl; q++; //cout<<" @@@@hello "<<"$$$"<<q;
    }
       
 }
}
}
             
            