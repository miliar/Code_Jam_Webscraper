#include<stdio.h>
bool check(bool * tab)
{
    for (int i =0;i<10;i++)
	if(!tab[i]) return false;
    return true;
}
int main()
{
    int zes;
    scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	int n;scanf("%d",&n);
	bool tab[10]={};
	for (int i=1;i<1000;i++)
	{
	    int val = n*i;
	    do
	    {
		tab[val%10]=1;
	    }while(val/=10);
	    if(check(tab))
	    {
		printf("Case #%d: %d\n",z+1,n*i);
		break;
	    }
	}
	if(check(tab)) continue;
	printf("Case #%d: INSOMNIA\n",z+1);
    }
}
