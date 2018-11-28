#include <stdio.h>

int main()
{
    int test;
    
    scanf("%d",&test);
    
    int casos = 1;
    
    while(test--)
    {
        int vec[16];
        
        for(int i = 0; i < 16; i++)
            vec[i] = 0;
        
        int num = -1;
        
        for(int i = 0; i < 2; i++)
        {
            int r;
            scanf("%d",&r);
            r--;
            
            for(int x = 0; x < 4; x++)
            {
                for(int y = 0; y < 4; y++)
                {
                    int a;
                    scanf("%d",&a);
                    a--;
                    
                    if(r == x)
                    {
                        if(i)
                        {
                            if(vec[a])
                            {
                                if(num == -1)
                                    num = a + 1;
                                else
                                    num = 100;
                            }
                        }
                        else
                        {
                            vec[a] = 1;
                        }
                    }
                }
            }
        }
        
        if(num == 100)
            printf("Case #%d: Bad magician!\n",casos++);
        else if(num == -1)
            printf("Case #%d: Volunteer cheated!\n",casos++);
        else
            printf("Case #%d: %d\n",casos++, num);
    }
    
    return 0;
}