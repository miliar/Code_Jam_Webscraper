#include<bits/stdc++.h>
using namespace std;

char str[1005];
deque<char>coll;

int main()
{
//	freopen("A-large.in", "r" , stdin);
//freopen ("outputnewnewlarge.out","w",stdout);

	
	int T,i,j,len;
	deque<char>::iterator it;
	scanf("%d",&T);
	
	for(i=1;i<=T;i++)
		{
			scanf("%s",str);
			len=strlen(str);
			coll.push_back(str[0]);
			for(j=1;j<=len-1;j++)
				{
					if(str[j]>=*coll.begin())
						coll.push_front(str[j]);
					else
						coll.push_back(str[j]);	
				}
			
			printf("Case #%d: ",i);
			for(it=coll.begin();it!=coll.end();it++)
				printf("%c",*it);	
				
				printf("\n");		
			coll.clear();
		}
	
	
//	fclose(stdout);
	
	
	return(0);
}






