#include <iostream>
#include <cstdio>

using namespace std;

int isin (int cards[], int num)
    {int i;
        for(i=0; i<4; i++)
            if(cards[i] == num)
            {return 1;}
    return 0;}

main()
    {int t, cards[4], aux, x, y, i, j, c, ans;

    cin>>t;

    for(c=1; c<=t; c++)
        {ans = 0;
        cin >> x;

        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                {if(i+1==x)
                    {scanf("%d", &cards[j]);}
                else
                    scanf("%*d");}

        cin >> y;

        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                {if(i+1==y)
                    {scanf("%d", &aux);
                    if(isin(cards, aux)==1 && ans != 0)
                        ans = -1;
                    else if(isin(cards, aux)==1)
                        ans = aux;}
                else
                    scanf("%*d");}

        cout<<"Case #" << c << ": ";
        if(ans == 0)
            cout<<  "Volunteer cheated!" << endl;
        if(ans < 0)
            cout<< "Bad magician!" << endl;
        if(ans > 0)
            cout<< ans << endl;}



        return 0;}
