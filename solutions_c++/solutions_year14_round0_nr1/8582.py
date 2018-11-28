#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;

int cardsArray1[4][4];
int cardsArray2[4][4];

int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("out.txt","w",stdout);

    int T,ans1,ans2,temp,store,cardFound;
    cin>>T;
    for(int caseno=0;caseno<T;caseno++)
    {
        cin >> ans1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >> cardsArray1[i][j];
        cin >> ans2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >> cardsArray2[i][j];


        cardFound=0;
        for(int i=0;i<4;i++)
        {
            temp = cardsArray1[ans1-1][i];
            for(int j=0;j<4;j++)
            {
                if(temp == cardsArray2[ans2-1][j])
                {
                    store = temp;
                    cardFound++;
                }
            }
        }
        if(cardFound>=2)
        {
            printf("Case #%d: Bad magician!\n",caseno+1);
        }
        else if (cardFound==0)
        {
            printf("Case #%d: Volunteer cheated!\n",caseno+1);
        }
        else
        {
            printf("Case #%d: %d\n",caseno+1,store);
        }

    }

    return 0;
}
