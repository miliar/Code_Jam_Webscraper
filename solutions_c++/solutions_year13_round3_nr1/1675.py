#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<stack>
#include<queue>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<assert.h>
#include<math.h>
#include<climits>
#include <iomanip> //forsetw()
using namespace std;

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)

#define pi(a) printf("Value of " #a " is: %d\n",a);
#define pp(a) printf("Address of " #a " is: %p\n",a);
#define pstr(a) printf("String " #a " is: %s\n",a);

#define rep(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define gcd(a,b) __gcd(a,b)          //NOTE: Both the arguments should be of the same type.

int n;
int isConsonant(char c)
{
	if(c!='a' && c!='e' && c!='i' && c!='o' && c!='u')
		return 1;
	return 0;	  
}
int findAllSubstrings2(const char *s)
{
	int ans=0;
    while(*s)
    {
        int x=0;
        while(*(s + x))
        {
        	int c=0;
            for(int y = 0; y <= x; y++)
            {	 //std::cout << *(s + y);
            
            	if(isConsonant(*(s + y)))
            	{
            		c++;
            		if(c==n)
            		{
            			ans++;
            			break;
            		}		
            	}
            	else
            		c=0;	
            }
            x++;
        }
        s++;
    }
    return ans;
}

int main(int argc,char **argv)
{
	int t,i,x;
	char str[200];
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	gi(t);
	for(i=0;i<t;i++)
	{
		scanf("%s",str);
		scanf("%d",&n);
		
		printf("Case #%d: %d\n",i+1,findAllSubstrings2(str));	
	}
	
	return 0;
}

