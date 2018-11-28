#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

vector<int> get_draw()
{
    int row;
    cin >> row;
    
    vector<int> cards(16);
    for(auto& card : cards)
    {
        cin >> card;
    }
    
    vector<int> draw(4);
    copy(&cards[4*(row-1)], &cards[4*row], &draw[0]);
    sort(draw.begin(), draw.end());
    return draw;
}

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        auto first_draw = get_draw();
        auto second_draw = get_draw();
        vector<int> possibilities;
        set_intersection(first_draw.begin(), first_draw.end(), second_draw.begin(), second_draw.end(), back_inserter(possibilities));
        
        cout << "Case #"<< lp << ": ";
        if (possibilities.size() == 0)
        {
            cout << "Volunteer cheated!";
        }
        else if(possibilities.size() == 1)
        {
            cout << possibilities[0];
        }
        else
        {
            cout << "Bad magician!";
        }
        
        cout << "\n";
        
    }
    return 0;
}