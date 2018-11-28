#include<stdio.h>
#include<string.h>

int main()
{
    int t,a[17],b[17],row1,row2,counter,same,i,j,cas=1;

    freopen("E:\\Codejam\\A.in","r",stdin);
    freopen("E:\\Codejam\\A.out","w",stdout);
    scanf("%ld",&t);
    
    while(t--)
    {
        scanf("%ld",&row1);
        for(i=0; i<16; i++)
            scanf("%ld",&a[i]);
            
        scanf("%ld",&row2);
        for(i=0; i<16; i++)
            scanf("%ld",&b[i]);
        
        counter=0;    
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                if(a[(row1-1)*4+i]==b[(row2-1)*4+j])    
                {
                    same=a[(row1-1)*4+i];
                    counter++;
                    break;
                }
                    
            }
        }
    
        if(counter==1)
            printf("Case #%ld: %ld\n",cas++,same);
        else if(counter>1)    
            printf("Case #%ld: Bad magician!\n",cas++);
        else
            printf("Case #%ld: Volunteer cheated!\n",cas++);
    }
    return 0;
}
