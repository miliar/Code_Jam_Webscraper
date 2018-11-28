#include<bits/stdc++.h>
using namespace std;

int main()
{  int T, n, counter=0, i=0, end=0;
   bitset<101> S;
   char c[101];
   
   scanf("%d",&T);
   
   while(T)
   {  T--;
	  i++;
	  scanf("%s",c);
	  end =strlen(c);
	  for(int j=0;j<end ;j++)
	    if(c[j]=='+') S[j]=1;
	    else          S[j]=0;
	  if(end==1)
	    if(c[0]=='+') { printf("Case #%d: 0\n",i); continue; }
	    else          { printf("Case #%d: 1\n",i); continue; }
	  counter=0;	    
	  while(true)
	  {   for(n=0;n<end-1;n++)
		    if(S[n]^S[n+1]) break;
		  if(n!=end-1) for(int j=0;j<=n;j++) S[j]=!S[j];
		  else         {  if(!S[end-1]) counter++; break; }   
          counter++;
      }
      printf("Case #%d: %d\n",i,counter);	       
   }      	
}
