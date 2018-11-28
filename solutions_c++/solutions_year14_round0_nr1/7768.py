#include<bits/stdc++.h>

using namespace std;

const int max_size = 4;


int main()
{

    int cases;
    cin>>cases;
    for(int c = 1; c <= cases; c++)
    {
        unordered_set<int> cards;
        int answer;
        cin>>answer;
        for(int i = 1; i <= max_size; i++)
        {
            for(int j = 1; j <= max_size; j++)
            {
                int card;
                cin>>card;
                if(i == answer)
                {
                    cards.insert(card);
                }
            }
        }
        int search;
        cin>>search;
        int found = 0;
        int picked;
        for(int i = 1; i <= max_size; i++)
        {
            for(int j = 1; j <= max_size; j++)
            {
                int card;
                cin>>card;
                if(i == search)
                {
                    if(cards.find(card) != cards.end())
                    {
                        found++;
                        picked = card;
                    }
                }
            }
        }
        cout<<"Case #"<<c<<": ";
        if(found == 0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        if(found == 1)
        {
            cout<<picked<<endl;
        }
        if(found > 1)
        {
            cout<<"Bad magician!"<<endl;
        }

    }


return 0;
}
