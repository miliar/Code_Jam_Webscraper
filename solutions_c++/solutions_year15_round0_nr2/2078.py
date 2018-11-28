#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void testcase_infinite_house(int t)
{
    int D;
    cin >> D;
    vector <int> Pancakes(D); int maxi=0; int answer=2100000000;
    for(int h=0; h<D; h++)
        {
            cin >> Pancakes[h];
            maxi=max(maxi,Pancakes[h]);
        }
    for(int k=1; k<=maxi; k++)
        {
            int c=0;
            for(int i=0; i<D; i++)
                {
                    int g=Pancakes[i];
                    while(g>k)
                        {
                            g=g-k;
                            c++;
                        }
                }
            answer=min(answer,c+k);
        }
    cout << "Case #" << t << ": " << answer <<endl;
}
int main ()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
        testcase_infinite_house(t);
    return 0;
}
