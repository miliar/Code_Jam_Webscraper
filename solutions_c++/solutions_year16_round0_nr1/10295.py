#include <iostream>
using namespace std;
int b[10];
void store(int a,int b[10])
{int x;
 while(a)
 {x=a%10;
  a=a/10;
  b[x]=1;
  }
}
int check(int b[10])
{for(int i=0;i<10;i++)
 {if(b[i]==0)
   return 0;
 }
return 1;
}
int main() {
	int t,n,i,a,k=0,flag=0;
	cin>>t;
	while(k<t)
	{cin>>n;
     for(i=0;i<10;i++)
      b[i]=0;	
     if(n==0)
     { cout<<"case #"<<k++<<": INSOMNIA"<<endl;
     }
	 else
    {for(i=0;;i++)
      {a=n*i;
	   store(a,b);
	   if(flag=check(b))
		break;
       }
	  cout<<"case #"<<k++<<": "<<a<<endl;
 	}
}
	   
	return 0;
}