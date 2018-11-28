#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int k=1; k<=T; k++)
    {
        int N;
        cin >> N;
        vector<int> m(N);
        for(int i=0; i<N; i++)
            cin >> m[i];
        int s1 = 0;
        for(int i=0; i<N-1; i++)
        {
            if(m[i+1]<m[i]) s1 += m[i]-m[i+1];
        }
        int s2 = 0;
        int mx = 0;
        for(int i=0; i<N-1; i++)
        {
            if(m[i]-m[i+1]>mx) mx = m[i]-m[i+1];
        }
        for(int i=0; i<N-1; i++)
            s2 += min(mx,m[i]);
        cout << "Case #" << k << ": " << s1 << " " << s2 << endl;
    }
    return 0;
}
