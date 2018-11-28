#include <iostream>
#include<string.h>
using namespace std;

int main(void) {
	 freopen("B-large.in","r",stdin);
  freopen("outputgcj_l2.out","w",stdout);
	char s[105];char a; 
	int t,y,count;
	cin>>t;
	//scanf("%d",&t);
	y=1;
	while(y<=t)
	{
       cin>>s;
 		//scanf("%s",s);
	 int z=strlen(s);
	 
	 if(s[z-1]=='-')
	  count=1;
	 else  count=0;
	 
	  a=s[z-1];
	 
	for(int i=z-2;i>=0;i--)
	if(s[i]!=a)
	  {count++;a=s[i];}
	 cout<<"Case #"<<y<<": "<<count<<endl;
	//printf("Case #%d: %d\n",y,count);
	  y++;
	  
		
	}
	return 0;
}

