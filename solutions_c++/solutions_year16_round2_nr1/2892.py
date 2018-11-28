#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
    // string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
        // "ZERO", "TWO", "FOUR", "SIX", "EIGHT"
        // "ONE", "THREE", "FIVE", "SEVEN"
        // "NINE"
    int cts;
    scanf("%d", &cts);

    char special_char[] = {'Z', 'W', 'U', 'X', 'G'};
    int  special_numb[] = { 0,   2,   4,   6,   8};
    string special_remove[] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT"};

    char special_char2[] = {'O', 'T', 'F', 'S'};
    int  special_numb2[] = { 1,   3,   5,  7};
    string special_remove2[] = {"ONE", "THREE", "FIVE", "SEVEN"};

    getchar();
    for(int ct = 1; ct <= cts; ++ct)
    {
        int count[30] = {0};

        vector<int> ans;

        char c;
        while(c = getchar(), c != '\n')
        {
            string remove;
            for(int i = 0; i < 5; ++i)
            {
                if(c == special_char[i])
                {
                    ans.push_back(special_numb[i]);
                    remove = special_remove[i];
                }
            }
            count[c - 'A']++;

            for(auto remove_c: remove) count[remove_c - 'A']--;
        }

        for(int j = 0; j < 26; ++j)
        {
            if(count[j] == 0) continue;

            c = 'A' + j;
            for(int i = 0; i < 4; ++i)
            {
                string remove;
                int amount = 1;

                if(c == special_char2[i])
                {
                    for(int k = 0; k < count[c - 'A']; ++k)
                        ans.push_back(special_numb2[i]);
                    amount = count[c - 'A'];
                    remove = special_remove2[i];
                }

                for(auto remove_c: remove) count[remove_c - 'A']-=amount;
            }
        }

        if(count['I' - 'A'])
        {
            for(int k = 0; k < count['I' - 'A']; ++k)
                ans.push_back(9);
        }

        sort(ans.begin(), ans.end());

        printf("Case #%d: ", ct);
        for(auto a: ans) printf("%d", a);
        printf("\n");
    }

    return 0;
}
