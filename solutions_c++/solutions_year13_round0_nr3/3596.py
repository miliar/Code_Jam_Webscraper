#include<iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
int palin(unsigned long long p)
{unsigned long long b,n,i;
    b=p;
i=1;n=0;
int c[100];
while(b/i)
{
c[n]=b/i;
c[n]=c[n]%10;
i=i*10;
n++;
}
for(i=0;i<n/2;i++)
{if(c[i]!=c[n-i-1])
{return 0;}
}

return 1;
}
int main()
{   int f,c,i,j,k;
    FILE *in,*out;
    int t,n,m;
    //vector<int> p;
    in = fopen("in.in","r");
    out = fopen("out.out","w");
    
     fscanf(in,"%d",&t);
     k=0;
     
     while(k<t){k++;
                 fscanf(in,"%d %d",&n,&m);  
                 cout<<n<<m;
                 i=sqrt(n);
                 if(i*i<n)i++;
                 
                   for(c=0;i*i<=m;i++)
                   {if(palin(i))
                     {if(palin(i*i)) {
                                    //cout<<"hel";cin>>f;
                                     c++;} }
                   
                   }//cout<<"b";
                   fprintf(out,"Case #%d: %d\n",k,c);
                    }
    
    

return 0;}
