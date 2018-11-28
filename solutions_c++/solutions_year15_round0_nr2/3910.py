#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int solve_pancakes(priority_queue<int>& s)
{
    int maximum = s.top();
    if(maximum <= 3)
        return maximum;

    s.pop();
    int value = maximum;
    {
        priority_queue<int> copie(s);
        copie.push(maximum-3);
        copie.push(3);
        value = std::min(value, solve_pancakes(copie)+1);
    }
    {
        priority_queue<int> copie(s);
        copie.push(maximum>>1);
        if((maximum&1)==0)
            copie.push(maximum>>1);
        else copie.push((maximum>>1)+1);
        value = std::min(value, solve_pancakes(copie)+1);
    }
    return value;
}

char table_gauche[8][3] = {
    {'l', 'k', 'n'}, // i*
    {'o', 'l', 'i'}, // j*
    {'j', 'm', 'l'}, // k*
    {'m', 'n', 'o'}, // (-1)*
    {'p', 'o', 'j'}, // (-i)*
    {'k', 'p', 'm'}, // (-j)*
    {'n', 'i', 'p'},
    {'i','j','k'} // 1*
};

char inverses[8] = {'m', 'n', 'o', 'l', 'i', 'j', 'k', 'p'};

void partial_products(const string& s, string& result)
{
    result += s[0];
    for(unsigned int i = 1; i<s.length(); i++)
    {
        result += table_gauche[result[i-1]-0x69][s[i]-0x69];
    }
}

int main()
{
    int T;

    cin >> T;
    for(int tt = 1; tt<= T; tt++)
    {
        /* Pancakes */
        int D,k;
        priority_queue<int> plates;
        cin >> D;
        for(int i = 0; i < D; i++)
        {
            cin >> k;
            plates.push(k);
        }

        cout << "Case #" << tt << ": " << solve_pancakes(plates) << endl;

        /* Dijkstra */
        /*int L,X;
        bool found = false;
        cin >> L >> X;
        string input, expanded, partial_prods;
        vector<int> m1,m2;
        cin >> input;

        for(int i = 0; i < X; i++)
            expanded += input;

        partial_products(expanded, partial_prods);
        for(int ind1 = 0; ind1 < expanded.length(); ind1++)
        {
            for(int ind2 = ind1+1; ind2 < expanded.length(); ind2++)
            {
                if(partial_prods[ind1] == 'i' && partial_prods[ind2] == 'k' && partial_prods[expanded.length()-1]=='l')
                {
                    found = true;
                    break;
                }
            }
            if(found) break;
        }
        cout << "Case #" << tt << ": " << (found?"YES":"NO") << endl;*/
    }
    return 0;
}
