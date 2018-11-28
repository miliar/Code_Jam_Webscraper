#include <iostream>
#include <string>
using namespace std;
void testcase_standing_ovation(int t)
{
    int S;
    cin >> S;
    int answer=0; int sume=0; string c;
    cin >> c;
    sume=sume+(c[0]-'0');
    for(int i=1; i<=S; i++)
        {
            if(sume<i)
                {
                    answer=answer+(i-sume);
                    sume=i;
                }
            sume=sume+(c[i]-'0');
        }
    cout << "Case #" << t << ": " << answer <<endl;
}
int main ()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
        testcase_standing_ovation(t);
    return 0;
}
