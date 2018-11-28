#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
    freopen("A-large.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int t, sm, cnt, k, atn, inv;
	string st;
	cin >> t;
	for(int i = 0 ; i < t ; i++)
	{
        cnt = 0;
        inv = 0;
        cin >> sm;
        cin >> st;
        for(int j = 0 ; j < st.size() ; j++)
        {
            k = ((int)st[j]) - 48;
            if(! (cnt >= j))
            {
                atn = j - cnt;
                cnt += atn;
                inv += atn;
            }
            cnt += k;
        }
        cout << "Case #" << i + 1 << ": " << inv << endl;
    }
    return 0;
}
