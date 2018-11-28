#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int testcase;
    scanf("%d",&testcase);

    for (int caseId=1; caseId<=testcase; caseId++)
    {
        int i,j,val,count1=0,count2=0,count3=0,found=0,count0=0;
        char temp;
        int A[4][4];
        scanf("%c",&temp);
        printf("Case #%d: ",caseId);
        for(i=0; i<4; i++)
        {
            count1=0;
            count2=0;
            count3=0;
            for(j=0; j<4; j++)
            {
                scanf("%c",&temp);
                if(temp=='.')
                {
                    val=0;
                    count0++;
                }
                else if (temp=='X')
                {
                    val=1;
                    count1++;
                }
                else if (temp=='O')
                {
                    val=2;
                    count2++;
                }
                else if (temp=='T')
                {
                    val=3;
                    count3++;
                }
                A[i][j]=val;
            }
            scanf("%c",&temp);
            if(count1+count3==4)
            {
                found=1;
            }
            else if(count2+count3==4)
            {
                found=2;
            }
        }

        if(found==0)
        {
            for(i=0; found==0 && i<4; i++)
            {
                count1=0;
                count2=0;
                count3=0;
                for(j=0; j<4; j++)
                {
                    if(A[j][i]==1)
                    {
                        count1++;
                    }
                    else if(A[j][i]==2)
                    {
                        count2++;
                    }
                    else if(A[j][i]==3)
                    {
                        count3++;
                    }
                }
                if(count1+count3==4)
                {
                    found=1;
                }
                else if(count2+count3==4)
                {
                    found=2;
                }
            }
        }

        if(found==0)
        {
            count1=count2=count3=0;
            for(j=0; j<4; j++)
            {
                if(A[j][j]==1)
                {
                    count1++;
                }
                else if(A[j][j]==2)
                {
                    count2++;
                }
                else if(A[j][j]==3)
                {
                    count3++;
                }
            }
            if(count1+count3==4)
            {
                found=1;
            }
            else if(count2+count3==4)
            {
                found=2;
            }
        }

        if(found==0)
        {
            count1=count2=count3=0;

            for(i=0,j=3; i<4; j--,i++)
            {
                if(A[i][j]==1)
                {
                    count1++;
                }
                else if(A[i][j]==2)
                {
                    count2++;
                }
                else if(A[i][j]==3)
                {
                    count3++;
                }
            }
            if(count1+count3==4)
            {
                found=1;
            }
            else if(count2+count3==4)
            {
                found=2;
            }
        }

        if(found==1)
        {
            printf("X won\n");
        }
        else if(found==2)
        {
            printf("O won\n");
        }
        else if(count0>0)
        {
            printf("Game has not completed\n");
        }
        else
        {
            printf("Draw\n");
        }

    }
    return 0;
}
