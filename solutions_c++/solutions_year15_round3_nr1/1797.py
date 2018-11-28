#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void testcase_battleship(int t)
{
    int r; int c; int w;
    cin >> r;
    cin >> c;
    cin >> w;
    if((c-w)%w==0)
        cout << "Case #" << t << ": " << w+(c-w)/w <<endl;
    else
        cout << "Case #" << t << ": " << w+(c-w)/w+1 <<endl;
}
int main ()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
        testcase_battleship(t);
    return 0;
}
