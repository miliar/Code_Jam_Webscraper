#include <iostream>

using namespace std;

int main()
{
    int n_cases;
    cin >> n_cases;
    for(int i=1; i<=n_cases; i++)
    {
        int s_max;
        string s_distr;         //shyness distribution
        cin >> s_max;
        int n_clapping(0);         //number of people clapping at current iteration
        int n_to_invite(0);
        cin >> s_distr;
        for(int j=0; j<=s_max; j++)
        {
            int n_curr_s = s_distr[j] - '0';
            //cout << "n_curr_s:" << n_curr_s << endl;

            if(n_curr_s==0)
                continue;

            int n_missing(j-n_clapping);

            if(n_missing > 0)
            {
                n_to_invite += n_missing;
                n_clapping += n_missing;
            }

            n_clapping += n_curr_s;
        }
        cout << "Case #" << i << ": " << n_to_invite << endl;
    }
}
