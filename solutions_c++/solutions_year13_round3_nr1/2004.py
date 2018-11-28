#include<iostream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<vector>
#include <algorithm> 
using namespace std;

long long int permute(string str, int i, int l,int n) 
{  int c=0,co=0, j=i;
   
   if((l-i+1)<n)
   return 0;
   
   for(int k=i+n; k<=l+1; k++)
   {   c=0;
       for(j=i; j<k; j++)
       { if(str[j]=='a' || str[j]=='e' ||str[j]=='i' || str[j]=='o' || str[j]=='u')
         { c=0;
         }
         else
         {  c++;
            if(c>=n)
            break;
         }
       }
     if(c>=n)
      co++;
   }
    /* for(j=i;j<=l;j++)
      cout<<str[j];
      cout<<"\n";
      */return permute(str,i+1,l,n)+co;
   
}

int main()
{
int t,k;
cin>>t;
for(k=0;k<t;k++)
{      
    int i,j,m,n;
    string str;//arr[101];
    bool flag=false;
    cin>>str>>n;
    int l=str.size()-1;
    long long int s=permute(str,0,l,n);
    
     cout<<"Case #"<<k+1<<": "<<s<<"\n";
}
  // system("pause");
}




