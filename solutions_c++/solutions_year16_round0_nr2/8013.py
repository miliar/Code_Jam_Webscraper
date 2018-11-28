#include <iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main() {
	int t,i=0, count =0;
	char a[100];
	int  b[100];
	scanf("%d",&t);
	while(i<t)
	{ scanf("%s",a);
	  count=0;
	  for(int j=0; j<strlen(a); j++)
	  {   if(a[j]==45)
	      b[j]=1;
	      else if(a[j]==43)
	      b[j]=0;
      }
      int k=0;
      for(int l=0; l<strlen(a); l++)
      { if(b[l]==1&&l!=0)
        { for(int d=0; d<l; d++)
          b[d]==0;
          count++;
        }
        if(b[l]==1)
        {  for(k=l; k<strlen(a); k++)
          { if(b[k]==0)
            break;
            if(b[k]==1)
            b[k]=0;
          }
          l=k-1;
          count++;
        }  }
       cout << "Case #" << i+1 << ": " << count<<endl;
	i++;
	}
}