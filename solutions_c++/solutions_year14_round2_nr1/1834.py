#include<iostream>
using namespace std;
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<stdio.h>
int main()
 {
 	char s[105];
 	freopen("in.txt","r",stdin);
 	freopen("out.txt","w",stdout);
 	
 	int t,n,i,j,tes,flag;
 	cin>>t;
 	for(tes=1;tes<=t;tes++)
 	  {
 	  	
 	  	cin>>n;
 	  	gets(s);
 	    int a[102][102][2]={{{0}}};
 	    int p[102]={0};
 	  	for(i=0;i<n;i++)
 	  	  {
 	  	  	gets(s);
 	  	  	int l=strlen(s);
 	  	  	p[i]=1;
 	  	  	a[i][0][0]=s[0];
 	  	  	a[i][0][1]=1;
 	  	  	
 	  	  	for(j=1;j<l;j++)
 	  	  	   {if(s[j]==a[i][p[i]-1][0])
 	  	  	      a[i][p[i]-1][1]++;
 	  	  	    else
 	  	  	       {a[i][p[i]][0]=s[j];
 	  	      	    a[i][p[i]][1]=1;
 	  	      	    p[i]++;
 	  	  	       }
 	  	  	   }
 	  	  }
 	  	flag=1;
 	  	int std=p[0];
 	  	for(i=0;i<n;i++)
 	  	  {
 	  	  	if(p[i]!=p[0])
 	  	  	   {flag=0;
 	  	  	    break;
 	  	  	   }
 	  	  }
 	  	for(i=0;i<std && flag;i++)
 	  	  {
 	  	  	for(j=0;j<n;j++)
 	  	  	   {if(a[j][i][0]!=a[0][i][0])
 	  	  	      {flag=0;
 	  	  	       break;
 	  	  	      }
 	  	  	   }
 	  	  }
 	  	int m;
 	  	int count=0;
 	  	for(i=0;i<std && flag;i++)
 	  	  {m=0;
 	  	  	for(j=0;j<n;j++)
 	  	  	  {m+=a[j][i][1];
 	  	  	  }
 	  	    m/=n;
 	  	    for(j=0;j<n;j++)
 	  	  	  {count+=abs(a[j][i][1]-m);
 	  	  	  }
 	  	  }
 	  	cout<<"Case #"<<tes<<": ";
 	  	if(!flag)
 	  	   cout<<"Fegla Won"<<endl;
 	  	else
 	  	  cout<<count<<endl;
 	  	
 	  }
 	
 	
 	
 }
