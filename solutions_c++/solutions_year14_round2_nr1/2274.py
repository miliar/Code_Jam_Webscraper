// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define p(n)                        printf("%d",n)
#define pc(n)                       printf("%c",n)
#define pl(n)                       printf("%lld",n)
#define pln(n)                      printf("%lld\n",n)
#define pf(n)                       printf("%lf",n)
#define ps(n)                       printf("%s",n)
#define pn(n)                       printf("%d\n",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<=b;i++)
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
//Header Files
#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<string.h>
#include<algorithm>
#include<map>

using namespace std;





inline string IntToString(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int StringToInt(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}

inline string GetString(void){
	char x[1000005];
	scanf("%s",x); string s = x;
	return s;
}

int TC,n;
int a,b,c,d,nChar;
string temp;

int main()
 {
 	freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
 	
 	int status;
 	string all = "abcdefghijklmnopqrstuvwxyz";
 	int counter,nChar,nway;
 	scanf("%d",&TC);
 	for(a = 0; a < TC; a++)
 	{
 		status = 0;
 		nway = 0;
 		scanf("%d",&n);
		int data1[26];
		int data2[26];
		
	
		for(b = 0; b < 26; b++)
		{
			data1[b] = 0;
			data2[b] = 0; 
		}
		  
		  
 		for(b = 0; b < n; b++)
 		{
 			temp = GetString();
 			nChar = temp.size();
			
			for(c = 0 ; c < nChar; c++)
			{
				counter = 0;
				for(d = 0; d < 26; d++)
				{
					if(b == 0)
					{
						if(temp[c] == all[d])
						{
							data1[d]++;
							break;
						}		
					}
				
					else
					{
						if(temp[c] == all[d])
						{
							data2[d]++;
							break;	
						}
				 			
					}
				}

			}	
		}
		
		
		
		for(b = 0 ; b < 26; b++)
		{
			if(data1[b] == 0 && data2[b] == 0) continue;
			else if(data1[b] == 0 && data2[b] > 0 ) 
			{
				status = 1;
				printf("Case #%d: Fegla Won\n",a+1);
				break;	
			}
			else if(data1[b] > 0 && data2[b] == 0 ) 
			{
				status = 1;
				printf("Case #%d: Fegla Won\n",a+1);
				break;	
			}
			else if(data1[b] > 0 && data2[b] > 0)
			{
				nway += abs(data1[b] - data2[b]);
			}
		}
		
		
		if(!status) printf("Case #%d: %d\n",a+1,nway);
 	}
 	
 	return 0;
 }

