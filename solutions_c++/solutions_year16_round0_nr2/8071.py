#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
using namespace std;
char a[111];
int len;
int ans;int now;
int vis[1111];
int getsize()
{
    int sizee=0;
    for(int i=0;i<=111;i++)
        if(a[i]!='\0') sizee++;
    return sizee;
}

void state()
{
    int st=0;
    for(int i=0;i<len;i++)
        if(a[i]=='+') st+=pow(2,len-i);
    vis[st]=1;
}



void revers(int n)
{
    int temp[111];
    for(int i=0;i<n;i++)
        temp[i]=a[n-i-1];
    for(int i=0;i<n;i++)
        if(temp[i]=='+') a[i]='-';
        else if(temp[i]=='-') a[i]='+';
}

bool check()
{
    int tmp=0;
    for(int i=0;i<111;i++)
        if(a[i]=='+') tmp++;
     //   cout<<tmp<<endl;
    if(tmp==len) return 1;
    else return 0;
}




int main()
{
    freopen("7.in","r",stdin);
    freopen("8.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
        ans=0;
        memset(a,0,sizeof(a));
        scanf("%s",&a);
        getchar();
        len=getsize();
        //revers(len);
        //cout<<a<<endl;
        vector<bool> pan;
		for ( int i=0;i<len;i++){
			if(a[i] == '+'){
				pan.push_back(true);
			} else if (a[i] == '-') {
				pan.push_back(false);
			}
		}
		bool solve=false;
		int l=pan.size();
		int ans=0;
		while(!solve)
        {
			int i=l-1;
			int j=0;
			while(i>-1&&pan[i])
				i--;

			if(i==-1)
            {
				solve = true;
				continue;
			}
			ans++;
			if(pan[0])
            {
				ans++;
				while(pan[j]&& j<l)
				{
					pan[j]=false;
					j++;
				}
				j = 0;
			}
			vector<bool> temp;
			for(int t=i; t>-1; t--){
				temp.push_back(!pan[t]);
			}
			for(int t=0; t<=i;t++){
				pan[t]=temp[t];
			}
		}
		printf("Case #%d: %d\n",ii,ans);
	}
    return 0;
}
