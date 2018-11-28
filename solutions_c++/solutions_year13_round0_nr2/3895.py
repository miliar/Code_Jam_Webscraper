#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main()
{   int t,f,i,j,k,n,m;
    int L[101][101];
    vector<int> a(101),b(100);
    FILE *in,*out;
    
    in = fopen("in.in","r");
    out = fopen("out.out","w");
    
    fscanf(in,"%d",&t);
    k=0;
    while(k<t)
   {k++;
    
    fscanf(in,"%d %d",&n,&m);
    //a.clear(); b.clear();      
     a.assign(101,0);
     b.assign(101,0);
     //cout<<b[0]; 
    for(i=0;i<n;i++){ for(j=0;j<m;j++){
    fscanf(in,"%d",&L[i][j]);
    a[i]=max(a[i],L[i][j]);
    b[j]=max(b[j],L[i][j]);
       
       }}
       f=0;
       
    for(i=0;i<n && f==0;i++){ for(j=0;j<m;j++){
                      if(L[i][j]!=min(a[i],b[j])){
                                                 f=1; break;}
    }
    }   
       
       if(f==1)
       {fprintf(out,"Case #%d: NO\n",k);}
       else
       {fprintf(out,"Case #%d: YES\n",k);}   
       
}cin>>n; 
return 0;}
