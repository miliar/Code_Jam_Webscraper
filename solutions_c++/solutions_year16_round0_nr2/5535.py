#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<limits.h>
using namespace std;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int cases;
	scanf("%d",&cases);
	int count=0;
	while(cases--)
	{
		char s[109];
		int arr[109];
		scanf("%s",s);
		int n=strlen(s);
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-') { s[i]='0'; arr[i]=0;} 
			else { s[i]='1'; arr[i]=1;}
		}
		
		int ans=0;
		int n2=n;
		while(1)
		{
			int flag=1;
			
			for(int k=0;k<n;k++)
			{
				if(s[k] == '1') continue;
				else { flag=0;break;}
			}
			if(flag) break;

			if(n2-1 >= 0 && s[n2-1] == '1') { n2--;continue;}
			else {
				//s[n2-1] has '0'
				++ans;
				int tmp=n2-1;
				int tmp2=tmp;
				if(s[0] == s[n2-1])
				{
					//swap and reverse
					for(int j=0;j < tmp; j++,tmp--)
					{
						if(s[j] == '0') s[j]='1'; else s[j]='0';
						if(s[tmp] == '0') s[tmp]='1'; else s[tmp]='0';
						swap(s[j],s[tmp]);
					}
					if((tmp2+1) % 2 == 1) {
						if(s[tmp2/2] == '0') s[tmp2/2] ='1'; else s[tmp2/2]='0';
					}
				} //s[0] is '1'
				else
				{
					while(s[0] != s[tmp]) tmp--;
					tmp2=tmp;
					for(int j=0;j < tmp; j++,tmp--)
					{
						if(s[j] == '0') s[j]='1'; else s[j]='0';
						if(s[tmp] == '0') s[tmp]='1'; else s[tmp]='0';
						swap(s[j],s[tmp]);
					}
					if((tmp2+1) % 2 == 1) {
						if(s[tmp2/2] == '0') s[tmp2/2] ='1'; else s[tmp2/2]='0';
					}
				}
			}

		}	
			printf("Case #%d: %d\n",++count,ans);
	}

	return 0;

}
