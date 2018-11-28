// @AUTHOR ajay yadav//
#include<stdio.h>
inline void S(int *);
inline void S(int *a)
{
char c = 0;
while(c<33)
//c = fgetc_unlocked(stdin);
c = getc(stdin);
*a = 0;
while(c>33)
{
*a = *a*10 + c - '0';
//c = fgetc_unlocked(stdin);
c = getc(stdin);
}
}
int main()
{
  int t,z=1,fans,sans,first[5],second[5],waste;
  scanf("%d",&t);
  while(z<=t)
{
    printf("Case #%d: ",z);
    scanf("%d",&fans);
    for(int i=0;i<4;i++)
    {
            for(int j=0;j<4;j++)
            {
                if(i==(fans-1))
                scanf("%d",&first[j]);
                else
                    scanf("%d",&waste);
            }
    }
     scanf("%d",&sans);
    for(int i=0;i<4;i++)
    {
            for(int j=0;j<4;j++)
            {
                if(i==(sans-1))
                scanf("%d",&second[j]);
                else
                    scanf("%d",&waste);
            }
    }
    int counter=0,value=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        if(first[i]==second[j])
        {
            counter++;
            value=first[i];
        }
    }
    if(counter==0)
    {
        printf("Volunteer cheated!\n");
    }
    else
        if(counter==1)
    {
        printf("%d\n",value);
    }
    else
        printf("Bad magician!\n");
        z++;
}
return 0;
}
