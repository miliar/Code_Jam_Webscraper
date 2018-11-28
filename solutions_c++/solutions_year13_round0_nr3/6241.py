#include <stdio.h>
int arr[]={1,4,9,121,484};
int main()
{
    int t,a,b;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++)
    {
        scanf("%d%d",&a,&b);
        int count=0;
        for(int i=0;i<5;i++)
        {
            if(a<=arr[i]&&b>=arr[i])
                count++;
        }
        printf("Case #%d: %d\n",(cas+1),count);
    }
	return 0;
}
