#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("fractile_in.txt", "r", stdin);
    freopen("fractile_out.txt", "w", stdout);
	int t;
	cin >> t;
	int m=t;
	while(t--) {
        int k,c,s;
        cin >> k >> c >> s;
        if(k == s) {
		printf("Case #%d: ",m-t);
		for(int i=1;i<=s;i++)
            cout << i << " ";
        }
        else if (2*s <= k) {
           printf("Case #%d: IMPOSSIBLE", m-t);
        }
        else  {
            printf("Case #%d: ", m-t);
            for (int i = 2; i < 2 + s; i++)
                cout << i << " ";
            }
            cout << endl;
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
