#include <iostream>
#include <cstdio>
using namespace std;
int main()
{

    int test, cases=1;
    cin>>test;
    while(test--)
    {
        int ans1, ans2;
        int mat1[5][5], mat2[5][5];

        cin>>ans1;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
                cin>>mat1[i][j];
        }
        cin>>ans2;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
                cin>>mat2[i][j];
        }
        int count=0, save;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                if(mat1[ans1][i]==mat2[ans2][j])
                {
                    save=mat1[ans1][i];
                    count++;
                }
            }
        }
        if(count==0)
        {
            printf("Case #%d: Volunteer cheated!\n",cases++);
        }
        else if(count==1)
        {
            printf("Case #%d: %d\n",cases++,save);
        }
        else
            printf("Case #%d: Bad magician!\n",cases++);
    }

}
