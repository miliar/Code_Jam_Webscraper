#include<iostream>
#include<string.h>
#include<list>
#include<cmath>
#include<cstdio>
#include<fstream>
using namespace std;
struct X
{int count;
char c;
};
int main()
{
 freopen("A-small-attempt1.in","r",stdin);
  freopen("A.txt","w",stdout);
int T;
scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
	
	int N;
	scanf("%d",&N);
	char * A[N];
	for(int i=0;i<N;++i)
	{A[i]=new char [105];
	scanf("%s",A[i]);
	}
	
	list<X> B[N];
	for(int i=0; i<N;++i)
	{ int j=0;
	X temp;
	  int k= strlen(A[i]);
		while(j<k)
		{if(j==0)
			{temp.count =1;
			temp.c=A[i][j];
			
			B[i].push_back(temp);
			}
		else if(A[i][j]==B[i].back().c)
		{++B[i].back().count;
		}	
		else 
		{temp.count =1;
		temp.c=A[i][j];
		B[i].push_back(temp);
		}
		++j;
		}
	}

	int f=0;
	
   for(int i=1;i<N;++i)
   { list<X>:: iterator it0=B[0].begin();
     list<X>:: iterator iti=B[i].begin();
     while(it0!=B[0].end()&&iti!=B[i].end())
     {if(it0->c!=iti->c)
     	{f=1;
     	break;
 		}
     ++it0;
     ++iti;
     }
     if(it0!=B[0].end()||iti!=B[i].end())
     {f=1;
     }
     if(f==1)
      	break;
   }
    if(f==1)
	printf("Case #%d: Fegla won\n",t+1) ;
	if(f==0)
	{int sum=0;
	list<X> ::iterator it[N];
	for(int i=0;i<N;++i)
	{it[i]=B[i].begin();
	}
	while(it[0]!=B[0].end())
	{int av=0;
	for(int i=0;i<N;++i)
		{av+=it[i]->count;
		}
	av=av/N;
	for(int i=0;i<N;++i)
		{sum+=abs(it[i]->count-av);
		}	
	for(int i=0;i<N;++i)
		{++it[i];
		}	
	}
	printf("Case #%d: %d\n",t+1,sum);
	}

}
}
