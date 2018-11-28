#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    // The number of test cases
    uint64_t T;
    cin >> T;

    // Hold the values of the blocks
    double naomi_blocks[1000][2];
    double ken_blocks[1000][2];

    // Container for the deceitful war!!
    vector <double> deceit_naomi;
    vector <double> deceit_ken;
    deceit_naomi.reserve(1000);
    deceit_ken.reserve(1000);

    // The scores
    uint64_t ken_score;
    uint64_t naomi_score;
    uint64_t deceit_ken_score;
    uint64_t deceit_naomi_score;

    // The number of blocks
    uint64_t N;

    for(uint64_t i=0; i<T; ++i)
    {
        naomi_score = 0;
        ken_score = 0;
        deceit_naomi_score = 0;
        deceit_ken_score = 0;
        deceit_ken.clear();
        deceit_naomi.clear();

        cin >> N;

        for(uint64_t j=0; j<N; ++j)
        {
            cin >> naomi_blocks[j][0];
            deceit_naomi.push_back(naomi_blocks[j][0]);
            naomi_blocks[j][1] = 0;
        }

        for(uint64_t j=0; j<N; ++j)
        {
            cin >> ken_blocks[j][0];
            deceit_ken.push_back(ken_blocks[j][0]);
            ken_blocks[j][1] = 0;
        }

        double minimal_diff;
        uint64_t pos;

        // Play the war!!
        for(uint64_t j=0; j<N; ++j)
        {
            minimal_diff = -1;
            for(uint64_t k=0; k<N; ++k)
            {
                if(ken_blocks[k][0] > naomi_blocks[j][0] && ken_blocks[k][1] == 0)
                {
                    if(minimal_diff == -1)
                    {
                        minimal_diff = ken_blocks[k][0] - naomi_blocks[j][0];
                        pos = k;
                    }
                    else
                    {
                        if(minimal_diff > ken_blocks[k][0] - naomi_blocks[j][0])
                        {
                            minimal_diff = ken_blocks[k][0] - naomi_blocks[j][0];
                            pos = k;
                        }
                    }
                }
            }
            if(minimal_diff != -1)
            {
                ken_blocks[pos][1] = 1;
                ken_score++;
            }
            else
            {
                naomi_score++;
            }
        }

        // Play the deceitful war!!
        // Sort Naomi's blocks in decreasing order
        std::sort(deceit_naomi.rbegin(), deceit_naomi.rend());

        // Sort Ken's blocks in decreasing order
        std::sort(deceit_ken.rbegin(), deceit_ken.rend());

        for(uint64_t j=0, k=0; j<N ;j++)
        {
            if(deceit_ken[j] > deceit_naomi[k])
            {
                deceit_ken_score++;
            }
            else
            {
                deceit_naomi_score++;
                k++;
            }
        }

        // Print the results
        cout << "Case #" << (i+1) << ": " << deceit_naomi_score << " " <<  naomi_score << "\n";
    }

    return 0;
}
