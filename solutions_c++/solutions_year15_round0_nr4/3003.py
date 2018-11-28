#include<cstdio>

using namespace std;

int main()
{
    int test,counter=0;
    scanf("%d",&test);
    while(counter<test)
    {
	int x,r,c,flag=0;
        scanf("%d%d%d",&x,&r,&c);
	if(x==1) flag=1;
	else if(x==2) { if((r%2==0)||(c%2==0)) flag=1; }
	else if(x==3)
		{ if( ( (r==2) && (c==3) ) || ( (r==3) && (c!=1) ) || ( (r==4) && (c==3) ) ) flag=1; }
	else if(x==4) 
		{ if ( ((r==3)&&(c==4)) || ((r==4)&& ((c==3)||(c==4)) )) flag=1; }
        if(flag) printf("Case #%d: GABRIEL\n",counter+1);
	else printf("Case #%d: RICHARD\n",counter+1);
        counter++;
    }
    return 0;
}
