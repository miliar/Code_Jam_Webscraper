#include<cstdio>

using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t ,s ,x,y,ans;char c;
    scanf("%d",&t);
    for(int j=0;j<t;j++){
    	scanf("%d",&s);
    	scanf(" %c",&c);x=c-48;
    	ans=0;
    	for(int i=0;i<s;i++){
    		scanf("%c",&c);y=c-48;
    		if(x<i+1)
    			++ans,++x;
    		x+=y;
    	}
    	printf("Case #%d: %d\n",j+1,ans );
    }
    return 0;
}
