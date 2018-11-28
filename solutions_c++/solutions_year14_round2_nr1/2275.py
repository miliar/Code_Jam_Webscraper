#include <iostream>
using namespace std;
#include<stdio.h>
#include<string.h>
#define getcx getchar_unlocked
inline void inp(long long int *n )//fast input function
{
*n=0;
int ch=getcx();int sign=1;
while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
while( ch >= '0' && ch <= '9' )
*n = (*n<<3)+(*n<<1) + ch-'0', ch=getcx();
//*n=*n*sign;
}

inline void out (long long int n)
{
    char buffer[sizeof(n) * 8 * 3 / 10 + 3];  // 3 digits per 10 bits + two extra and space for terminating zero. 
    int index = sizeof(buffer)-1;
    int end = index;
    buffer[index--] = 0;
    do {
       buffer[index--] = (n % 10) + '0';
       n /= 10;
    } while(n);
    puts(&buffer[index+1]);//puts has \n in its function.
}

int main()
{
	long long int p,t=0,i,j,n;
	inp(&p);
	while(t++<p)
	{
		char c[101][101],d[101][101],tempa,tempb;int count=0,q,w;
			inp(&n);
			
			for(i=0;i<n;i++)
		    scanf("%s",&c[i]);
		    i=0;j=0;
		    if(c[0][i]==c[1][j])
		    {
		   // d[0][j]=a[0][i];
		    //d[1][j]=a[1][i];
		    	i++,j++;
		    //	cout<<i;
		    
		    }
		    tempa=c[0][0];
		    tempb=c[1][0];
		    while(1)
		    {	if(c[0][i]=='\0' && c[1][j]=='\0')
		    break;
		    	
		    	else if(c[0][i]==c[1][j])
		    {//cout<<"yes";
		    	tempa=c[0][i];
		    tempb=c[1][j];
		    //d[0][j]=a[0][i];
		    //d[1][j]=a[1][i];
		    i++;j++;}
		    else if(c[0][i]==tempb)
		    {i++;count++;
		   
		    }
		     else if(c[1][j]==tempa)
		   {
		   	j++;count++;
		   }
		    else break;
		    
		    }
		    
		    //j+=2;
		    q=strlen(c[0]);
		    w=strlen(c[1]);
		    if(i==q && j==w )
		    printf("Case #%lld: %d\n",t,count);
		    else printf("Case #%lld: Fegla Won\n",t);
		    
		    
		  
//	printf("\n%s",c[1]);		
	}

	return 0;
}