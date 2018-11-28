#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std ;

int t , r , c , m , u=0 , flag[50][50] ;
char a[50][50] ;
#define pii pair<int,int>

bool f1()
{
  queue<pii> Q ;   
  for(int i=0 ; i<r ; i++) for(int j=0 ; j<c ; j++) if(a[i][j]=='.')      
  {
     a[i][j]='c' ; int x=1 ;
     memset(flag,0,sizeof(flag)) ;
     Q.push(pii(i,j)) ; flag[i][j]=1 ;
     
     while(!Q.empty())
     {
        int u=Q.front().first , v=Q.front().second , y=0 ;
        Q.pop() ;
        
        for(int k=-1 ; k<=1 && !y ; k++) for(int l=-1 ; l<=1 ; l++) 
        {
        	int d=u+k , e=v+l ; 
            if(d<0 || d>=r || e<0 || e>=c || flag[d][e] ) continue ;
             if(a[d][e]=='*') { y=1 ; break ;  }
        }
        if(y)  continue  ; 
        
        for(int k=-1 ; k<=1 && !y ; k++) for(int l=-1 ; l<=1 ; l++) 
        {
            int d=u+k , e=v+l ; 
            if(d<0 || d>=r || e<0 || e>=c || flag[d][e] ) continue ;
            Q.push(pii(d,e)) ; flag[d][e]=1 ;  x++ ;       
        }                        
     }
     
     if(x==m) return 1 ;
     a[i][j]='.' ;
  } 
 return 0 ; 
} 


bool f(int i , int j , int tot)
{
   if(j==c) i++ , j=0 ;  
   if(i==r)
   {
       if(f1()) return 1 ; 
     return 0 ; 
   }     
   
   if(tot>0) { a[i][j]='.' ; if(f(i,j+1,tot-1)) return 1 ; }  
   a[i][j]='*' ; if(f(i,j+1,tot)) return 1 ; 
 return 0 ;  
}

int main()  
{   
   //ifstream in("s.txt") ; ofstream out("a.txt") ;
   cin >> t ; 
   while(t--)
   {
      cin >> r >> c >> m ;  m=r*c-m ;
      cout << "Case #" << ++u << ":\n";
      
      if(m==1)
      { 
           for(int i=1 ; i<=r ; cout<<"\n",i++) for(int j=1 ; j<=c ; j++,m--) cout << (m>0?"c":"*") ;
        continue ;       
      }  
      
      if(r==1 || c==1)
      {
          int x=0 ;     
          for(int i=1 ; i<=r ; cout<<"\n",i++) for(int j=1 ; j<=c ; j++,m--)  
            if(!x) { cout << "c" ; x++ ; }   else  cout << (m>0?".":"*") ;
         continue ;        
      } 
      
      if(m<=3 )   {  cout << "Impossible\n" ; continue ; }
   
      if(c==2 && m%2==0)
      {
          int x=0 ;     
          for(int i=1 ; i<=r ; cout<<"\n",i++) for(int j=1 ; j<=c ; j++,m--)  
            if(!x) { cout << "c" ; x++ ; }   else  cout << (m>0?".":"*") ;
         continue ;        
      }
       
      if(r==2 && m%2==0)
      {
          int x=0 ;    
          for(int i=1 ; i<=r ; cout<<"\n",i++) for(int j=1 ; j<=c ; j++)  
            if(!x) { cout << "c" ; x++ ; }   else  cout << ((2*j<=m)?".":"*") ;
         continue ;       
      }

      if(m<=2*c && m%2==0) 
      {
          int x=0 ;    
          for(int i=1 ; i<=r ; cout<<"\n",i++) for(int j=1 ; j<=c ; j++)  
            if(!x) { cout << "c" ; x++ ; }   else  cout << ((i<=2 && 2*j<=m)?".":"*") ;
         continue ;   
      }
      
      if(f(0,0,m)) for(int i=0 ; i<r ; cout<<"\n",i++) for(int j=0 ; j<c ; j++) cout << a[i][j] ; 
      else cout << "Impossible\n" ;
   } 
   
      
 return 0 ;
}
