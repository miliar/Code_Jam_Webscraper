#include<stdio.h>

#include<map>
using namespace std;
map<pair<int,int> , int> m; 


char Data[10001];
char DataI[10001];


int main()
{
	freopen ("D:\\Input.txt","rb",stdin);
	freopen ("D:\\Output1.txt","wb",stdout);
	pair<int,int> p;
	m.insert(make_pair(make_pair(-1,1),-1));
	m.insert(make_pair(make_pair(-1,2),-2));
	m.insert(make_pair(make_pair(-1,3),-3));
	m.insert(make_pair(make_pair(-1,4),-4));
	m.insert(make_pair(make_pair(1,1),1));
	m.insert(make_pair(make_pair(1,2),2));
	m.insert(make_pair(make_pair(1,3),3));
	m.insert(make_pair(make_pair(1,4),4));
	m.insert(make_pair(make_pair(2,1),2));
	m.insert(make_pair(make_pair(2,2),-1));
	m.insert(make_pair(make_pair(2,3),4));
	m.insert(make_pair(make_pair(2,4),-3));
	m.insert(make_pair(make_pair(-2,1),-2));
	m.insert(make_pair(make_pair(-2,2),1));
	m.insert(make_pair(make_pair(-2,3),-4));
	m.insert(make_pair(make_pair(-2,4),3));
	m.insert(make_pair(make_pair(3,1),3));
	m.insert(make_pair(make_pair(3,2),-4));
	m.insert(make_pair(make_pair(3,3),-1));
	m.insert(make_pair(make_pair(3,4),2));
	m.insert(make_pair(make_pair(-3,1),-3));
	m.insert(make_pair(make_pair(-3,2),4));
	m.insert(make_pair(make_pair(-3,3),1));
	m.insert(make_pair(make_pair(-3,4),-2));
	m.insert(make_pair(make_pair(4,1),4));
	m.insert(make_pair(make_pair(4,2),3));
	m.insert(make_pair(make_pair(4,3),-2));
	m.insert(make_pair(make_pair(4,4),-1));
	m.insert(make_pair(make_pair(-4,1),-4));
	m.insert(make_pair(make_pair(-4,2),-3));
	m.insert(make_pair(make_pair(-4,3),2));
	m.insert(make_pair(make_pair(-4,4),1));


	int T,L,X;
	char c;
	scanf("%d",&T);
	int val = 1;
	for(int i=1;i<=T;i++)
	{
		scanf("%d %d",&L,&X);
		scanf("%c",&c);		
		scanf("%c",&c);		
		val = 1;
		bool iFound = false;
		bool jFound = false;
		bool kFound = false;
		bool jjFound = false;
		bool iiFound = false;
		for(int j=0;j<L;j++)
		{
			scanf("%c",&c);
			if(c == 'i')
			{
				val = m[make_pair(val,2)];
				iFound = true;
			}
			else if(c == 'j')
			{
				val = m[make_pair(val,3)];
				jFound = true;
			}
			else if(c == 'k')
			{				
				val = m[make_pair(val,4)];
				kFound = true;
			}

			if(val==2)
			{
				iiFound = true;				
			}
			else if( val == 4 && iiFound)
			{
				jjFound = true;
			}
		}
		int FinalVal = 0;
		if((!iFound&&!jFound) || (!iFound&&!kFound)|| (!kFound&&!jFound))
		{
			printf("Case #%d: NO\n",i);
			continue;
		}

		if(val == 1)
		{
			printf("Case #%d: NO\n",i);
			continue;
		}
		else if(val == -1) 
		{
			if(X%2==0)
			{
				printf("Case #%d: NO\n",i);
				continue;
			}
			FinalVal = -1;
		}
		else
		{
			if(X%4==0 || X%2)
			{
				printf("Case #%d: NO\n",i);
				continue;
			}
			else
			{
				int x = X/2;
				if(x%2==0)
				{
					printf("Case #%d: NO\n",i);
					continue;
				}
			}
			FinalVal = -1;
		}		
		if(FinalVal == -1)
		{
			if(jjFound)
				printf("Case #%d: YES\n",i);
			else if(X>2)
				printf("Case #%d: YES\n",i);
			else
				printf("Case #%d: NO\n",i);
		}
		else
		{
			printf("Case #%d: NO\n",i);
		}
	}	
	return 0;
}