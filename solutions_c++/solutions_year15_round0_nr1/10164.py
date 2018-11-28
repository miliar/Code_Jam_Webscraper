#include <iostream>
#include<stdio.h>
#include<cstring>
#include<string.h>
using namespace std;

int main() {
int t;int g;long int sum;string s;int y;
scanf("%d",&t);
y=t;
while(t--)
{cin>>g;
cin>>s;sum=0;
g=s[0]-'0';
for(int i=1;i<s.size();i++)
{if(g<i&&s[i]!='0')
{sum=sum+i-g;
g=i;


    
}
 g=g+(s[i]-'0')   ;
}
  printf("Case #%d: %ld\n",y-t,sum);  
    
}
	return 0;
}

