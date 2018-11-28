#include <cstdio>
#include <cstdlib>

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    
    for(int c = 1; c <= cases ; c++)
    {
        int first, second, firstarr[4][4],tmp, ansnum = 0, ans;
        scanf("%d",&first);
        first--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
                scanf("%d",&firstarr[i][j]);
        
        scanf("%d",&second);
        second--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
            {
                scanf("%d",&tmp);
                if(i==second)
                {
                    for(int k = 0 ; k < 4 ; k++)
                    {
                        if(firstarr[first][k]==tmp)
                        {
                            ansnum++;
                            ans = tmp;
                        }
                        if(ansnum>1)
                            break;
                    }
                }
            }
        if(ansnum<1) printf("Case #%d: Volunteer cheated!\n",c);
        else if(ansnum>1) printf("Case #%d: Bad magician!\n",c);
        else printf("Case #%d: %d\n",c,ans);
    }
}