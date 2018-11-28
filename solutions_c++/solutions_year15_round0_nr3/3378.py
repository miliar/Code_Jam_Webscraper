#include <iostream>
#define ll long long

static const ll MAX_SIZE = 10005;

// Now the prefix arrays.
// From i to end; bool means sign true = 1, false = -1
std::pair<char, bool> prefixes[MAX_SIZE][MAX_SIZE];
ll actualSize = 0;


std::pair<char, bool> multi(std::pair<char, bool> a, std::pair<char, bool> b)
{
    if (a.first == '1')
    {
        if (a.second == b.second)
        {
            return std::make_pair(b.first, true);
        }
        else
        {
            return std::make_pair(b.first, false);
        }
        
    }
    else if (a.first == 'i')
    {
        if (b.first == '1')
        {
            if (a.second == b.second)
            {
                return std::make_pair(a.first, true);
            }
            else
            {
                return std::make_pair(a.first, false);
            }
        }
        else if (b.first == 'i')
        {
            if (a.second == b.second)
            {
                return std::make_pair('1', false);
            }
            else
            {
                return std::make_pair('1', true);
            }
        }
        else if (b.first == 'j')
        {
            if (a.second == b.second)
            {
                return std::make_pair('k', true);
            }
            else
            {
                return std::make_pair('k', false);
            }
        }
        else if (b.first == 'k')
        {
            if (a.second == b.second)
            {
                return std::make_pair('j', false);
            }
            else
            {
                return std::make_pair('j', true);
            }
        }
    }
    else if (a.first == 'j')
    {
        if (b.first == '1')
        {
            if (a.second == b.second)
            {
                return std::make_pair(a.first, true);
            }
            else
            {
                return std::make_pair(a.first, false);
            }
        }
        else if (b.first == 'i')
        {
            if (a.second == b.second)
            {
                return std::make_pair('k', false);
            }
            else
            {
                return std::make_pair('k', true);
            }
        }
        else if (b.first == 'j')
        {
            if (a.second == b.second)
            {
                return std::make_pair('1', false);
            }
            else
            {
                return std::make_pair('1', true);
            }
        }
        else if (b.first == 'k')
        {
            if (a.second == b.second)
            {
                return std::make_pair('i', true);
            }
            else
            {
                return std::make_pair('i', false);
            }
        }
    }
    else if (a.first == 'k')
    {
        if (b.first == '1')
        {
            if (a.second == b.second)
            {
                return std::make_pair(a.first, true);
            }
            else
            {
                return std::make_pair(a.first, false);
            }
        }
        else if (b.first == 'i')
        {
            if (a.second == b.second)
            {
                return std::make_pair('j', true);
            }
            else
            {
                return std::make_pair('j', false);
            }
        }
        else if (b.first == 'j')
        {
            if (a.second == b.second)
            {
                return std::make_pair('i', false);
            }
            else
            {
                return std::make_pair('i', true);
            }
        }
        else if (b.first == 'k')
        {
            if (a.second == b.second)
            {
                return std::make_pair('1', false);
            }
            else
            {
                return std::make_pair('1', true);
            }
        }
    }
}

void countPrefixes(std::string s, ll start)
{
    prefixes[start][start] = std::make_pair(s[start], true);
    // Now multiply the rest
    for (ll i = start + 1; i < actualSize; i++)
    {
        prefixes[start][i] = multi(prefixes[start][i-1], std::make_pair(s[i], true));
    }
}

bool isijk()
{
    bool found = false;
    ll i = 0;
    ll j = 0;
    ll k = 0;
    while ((i < actualSize) && (!found))
    {
        if ((prefixes[0][i].first == 'i') && (prefixes[0][i].second))
        {
            j = i + 1;
            while ((j < actualSize) && (!found))
            {
                if ((prefixes[i + 1][j].first == 'j') && (prefixes[i + 1][j].second))
                {
                    // Now we now what is in the end. (k+1,end) prefix.
                    k = j + 1;
                    if ((prefixes[k][actualSize - 1].first == 'k') && (prefixes[k][actualSize - 1].second))
                    {
                        found = true;
                    }
                }
                j++;
            }
        }
        i++;
    }
    return found;
}

void printijk ()
{
    for (ll i = 0; i < actualSize; i++)
    {
        for (ll j = 0; j < actualSize; j++)
        {
            std::cout << prefixes[i][j].first << " " << prefixes[i][j].second << " ";
        }
        std::cout << std::endl;
    }
}


int main()
{
    ll tests;
    ll L, X;
    std::string fragment;
    std::string working;
    std::cin >> tests;
    for (ll i = 1; i <= tests; i++)
    {
        working = "";
        std::cin >> L >> X;
        actualSize = L * X;
        std::cin >> fragment;
        for (ll j = 0; j < X; j++)
        {
            working.append(fragment);
        }
        //std::cout << working << std::endl;
        for (ll j = 0; j < actualSize; j++)
        {
            countPrefixes (working, j);
        }
        //printijk ();
        if (isijk ())
        {
            std::cout << "Case #" << i << ": " << "YES" << std::endl;
        }
        else
        {
            std::cout << "Case #" << i << ": " << "NO" << std::endl;
        }
    }
}