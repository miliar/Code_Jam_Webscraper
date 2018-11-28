#include<cstdio>

using namespace std;

int main()
{
    int test,counter=0;
    scanf("%d",&test);
    while(counter<test)
    {
        int shymax,i,sum=0,current,temp;
	char arr[1001];
        scanf("%d %s",&shymax,arr);
        if(shymax)
        {
            current=arr[0]-'0';
            for(i=1;i<=shymax;i++)
            {
                temp=arr[i]-'0';
                if((current<i)&&(temp)) 
		{
			sum+=(i-current);
			current=temp+i;
		}	
		else current=current+temp;
            }
        }
        printf("Case #%d: %d\n",counter+1,sum);
        counter++;
    }
    return 0;
}
