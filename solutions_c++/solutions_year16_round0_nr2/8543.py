#include <bits/stdc++.h>

#define fi(a,b,c) for(int a=b; a<=c; a++)
#define fd(a,b,c) for(int a=b; a>=a; a--)
#define pb push_back
#define mp make_pair
#define ft first
#define sc second

using namespace std;

string S;
int n;

int solve()
{
    int ans = 0;
    bool ok = 1;
    fi(i, 1, n) if (S[i-1] == '-') ok = 0;
    while (!ok)
    {
        ans ++;
        if (S[0] == '-')
        {
            int i;
            for (i = n; i > 0; i--)
                 if (S[i- 1] == '-') break;
        //    cout <<i<<endl;
            for (int j= 1; j * 2 <= i; j++)
                swap(S[j - 1], S[i- j]);
         //   cout <<"->"<<S<<endl;
            for (int j= 1; j<= i ; j++)
                if (S[j-1] == '+')
                    S[j-1] = '-'; else S[j-1] = '+';
        }
        else
        {
            for (int i = 1; i<= n && S[i-1]== '+'; i++)
            {
                S[i-1] = '-';
            }
        }

     //   cout <<S<<endl;
        ok = 1;
        fi(i, 1, n) if (S[i] == '-') ok = 0;
    }
    return ans;
}

int main()
{
  //  freopen("test.in", "r", stdin);
  //  freopen("test.out", "w", stdout);

    int tcase;
    cin >>tcase;


    fi(t, 1, tcase)
    {
        cin >> S;
        n = S.size();
      //  cout <<S<<endl;

        int kk = solve();
        printf("Case #%d: %d\n", t, kk);
    }
}

