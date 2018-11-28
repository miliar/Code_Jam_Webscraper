#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;

int main()
{
    vector<char> cGroups;
    vector<char> cGroups2;
    vector<int> numbers;
    vector<int> numbers2;
    vector< vector<int> > appears;

    int n, t;
    char c;
    int result;

    scanf("%d", &t);

    for(int k = 1; k <= t; ++k)
    {

        scanf("%d", &n);
        
        scanf(" %c", &c);
        cGroups.push_back(c);
        numbers.push_back(0);
        while(c != '\n')
        {
            if(cGroups.back() != c)
            {
                cGroups.push_back(c);
                numbers.push_back(1);
            }
            else
            {
                numbers.back() += 1;
            }
            scanf("%c", &c);
        }

        appears.resize(n);
        for(int j = 0; j < numbers.size(); ++j)
        {
            appears[0].push_back(numbers[j]);
        }
        result = 0;

        for(int i=1; i < n; ++i)
        {
            scanf("%c", &c);
            cGroups2.push_back(c);
            numbers2.push_back(0);
            while(c != '\n')
            {
                if(cGroups2.back() != c)
                {
                    cGroups2.push_back(c);
                    numbers2.push_back(1);
                }
                else
                {
                    numbers2.back() += 1;
                }
                scanf("%c", &c);
            }

            if(cGroups.size() == cGroups2.size())
            {
                for(int j = cGroups.size() - 1; j >= 0; --j)
                    if(cGroups[j] != cGroups2[j])
                    {
                        result = -1;
                        break;
                    }
            }
            else
            {
                result = -1;
                break;
            }

            if(result == -1)
                break;


            for(int j = 0; j < numbers2.size(); ++j)
            {
                appears[i].push_back(numbers2[j]);
                numbers[j] += numbers2[j];
            }

            cGroups2.clear();
            numbers2.clear();
        }


        printf("Case #%d: ", k);
        for(int j = 0; j < numbers.size(); ++j)
        {
            numbers[j] /= n;
        }

        if(result != -1)
        {
            for(int j = 0; j < n; ++j)
            {
                for(int q = 0; q < numbers.size(); ++q)
                {
                    if(appears[j][q] > numbers[q])
                        result += appears[j][q] - numbers[q];
                    else
                        result += numbers[q] - appears[j][q];
                }
            }
            printf("%d\n", result);
        }
        else
            printf("Fegla won\n");
        cGroups2.clear();
        numbers2.clear();
        cGroups.clear();
        numbers.clear();
        appears.clear();

    }

    return 0;    
}
