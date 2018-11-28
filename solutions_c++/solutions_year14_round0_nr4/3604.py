#include <fstream>
#include <algorithm>

using namespace std;

double N[1010], K[1010];
int test, tests, n, i, j, p;

int main()
{
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi >> tests;
    for(test = 1; test <= tests; test++)
    {
        fi >> n;
        for(i = 1; i <= n; i++)
            fi >> N[i];
        for(i = 1; i <= n; i++)
            fi >> K[i];
        //see war score
        sort(N+1, N+n+1);
        sort(K+1, K+n+1);

        int deceitful_war = 0;
        for(i = 1; i <= n; i++)
        {
            //starting from i
            int curr = 0;
            for(j = i; j <= n; j++)
                if(N[j] > K[j-i+1]) curr++;
            deceitful_war = max(deceitful_war, curr);
        }

        int war = 0;
        int n_tmp = n;
        for(i = 1; i <= n_tmp; i++)
        {
            //Naomi shows N[i]
            //Ken gets smallest card larger than it
            p = upper_bound(K+1, K+n+1, N[i])-K;
            if(p > n)
            {
                war++;
                p = 1;
            }
            for(j = p; j < n; j++)
                K[j] = K[j+1];
            n--;
            //now eliminate card
        }

        fo << "Case #" << test << ": " << deceitful_war << " " << war << "\n";
    }
    return 0;
}
