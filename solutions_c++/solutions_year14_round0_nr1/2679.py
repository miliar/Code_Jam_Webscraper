// magic trick

#include <iostream>

using namespace std;

int main()
{
    unsigned int t;
    unsigned int T;
    
    cin>>T;

    for (t = 0; t < T; t++)
    {
        unsigned int i, j, tmp;
        unsigned int ans_row;
        unsigned int ans_card = 0;
        unsigned int cards[4];
        bool         is_bad = false;
        
        cin>>ans_row;
        
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
            {
                if ((i + 1) == ans_row)
                {
                    cin>>cards[j];
                }
                else
                {
                    cin>>tmp;
                }
            }
        }
        
        cin>>ans_row;
        
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
            {
                cin>>tmp;
                if (!is_bad &&
                    (tmp == cards[0] ||
                     tmp == cards[1] ||
                     tmp == cards[2] ||
                     tmp == cards[3]))
                {
                    if ((i + 1) == ans_row)
                    {
                        if (ans_card > 0)
                        {
                            is_bad = true;
                        }
                        else
                        {
                            ans_card = tmp;
                        }
                    }
                }
            }
        }
        
        cout<<"Case #"<<t+1<<": ";
        if (is_bad)
        {
            cout<<"Bad magician!"<<endl;
        }
        else if (ans_card > 0)
        {
            cout<<ans_card<<endl;
        }
        else
        {
            cout<<"Volunteer cheated!"<<endl;
        }
    }

    return 0;
}
