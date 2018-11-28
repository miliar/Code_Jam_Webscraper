#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream myfile;
    ifstream inpfile;
    inpfile.open("A-large.in");
    myfile.open("prob1.txt");
    long long int t, counter = 1;
    inpfile >> t;
    while (t > 0)
    {
        long long int n;
        inpfile >> n;

        if (n == 0)
        {
            myfile << "Case #" << counter << ": INSOMNIA" << endl;
            counter++;
        }
        else
        {
            bool arr[10] = {false};
            long long int i = 2, f = 0, copyn = n, ans = n;
            while(1)
            {
                while (copyn > 0)
                {
                    if (arr[copyn % 10] == false)
                    {
                        arr[copyn % 10] = true;
                        f++;
                    }
                    copyn /= 10;
                }
                if (f == 10)
                    break;

                copyn = n * i;
                ans = copyn;
                i++;
            }
            myfile << "Case #" << counter << ": " << ans << endl;
            counter++;
        }
        t--;
    }
    return 0;
}
