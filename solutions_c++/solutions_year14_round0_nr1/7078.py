#include <cstdio>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        int arr[2][4][4];
        int row[2];
        
        for(int i = 0; i < 2; ++i)
        {
            scanf("%d", row + i);
            for(int j = 0; j < 4; ++j)
                for(int k = 0; k < 4; ++k)
                    scanf("%d", arr[i][j] + k);
        }
        
        set<int> solns[2];
        for(int i = 0; i < 2; ++i)
            for(int j = 0; j < 4; ++j)
            solns[i].insert(arr[i][row[i] - 1][j]);
        
        vector<int> results;
        for(set<int>::iterator it = solns[0].begin(); it != solns[0].end(); ++it)
            if(solns[1].count(*it))
                results.push_back(*it);
        
        printf("Case #%d: ", t);
        if(results.empty())
        {
            /// None
            printf("Volunteer cheated!\n");
        }
        else if(results.size() == 1)
        {
            /// Just right
            printf("%d\n", results[0]);
        }
        else
        {
            /// Too many
            printf("Bad magician!\n");
        }
    }
    
    return 0;
}