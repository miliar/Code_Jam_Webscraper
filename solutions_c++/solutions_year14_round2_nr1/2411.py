#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;

int main()
{ char str1[104],str2[104];
  int i,j,t,l1,l2,c1,c2,moves,c=0,n;
   
  cin>>t;
  while(t--)
   { cin>>n;
     ++c; 
        cin>>str1;
        cin>>str2;
       
         l1=strlen(str1);
         l2=strlen(str2);
         int flag=0,moves=0,diff;
	
		 for(i=0,j=0;i<l1 || j<l2;)
		   	{ if(str1[i]!=str2[j] || (i<l1 && j>=l2) || (i>=l1 && j<l2)) { flag=1; break;}
		   	  c1=c2=0;
		   	  while(str1[i+1]==str1[i] && i+1<l1){++i; ++c1; /*cout<<"A";*/ }
			  while(str2[j+1]==str2[j] && j+1<l2){++j; ++c2; /*cout<<"B";*/ }	
			  diff=c1-c2;
			  ++i; ++j;
			  //system("pause");
		   	  if(diff<0)moves+=(diff*-1);
		   	  else moves+=diff;
		   	  //cout<<"hello "<<moves<<endl;
		   	  //system("pause");
		   	}
		if(flag==0)cout<<"Case #"<<c<<": "<<moves<<endl;
		else cout<<"Case #"<<c<<": Fegla Won"<<endl;   	
    }
   return 0;	
}
