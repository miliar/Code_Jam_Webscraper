#include <iostream>
#include <algorithm>

using namespace std;

int testy;
int n;
double tabn[1010];
double tabk[1010];
int lwk;
int pwk;
int ldk;
int pdk;
int wwynik;
int dwynik;

int main()
{
    ios_base::sync_with_stdio(0);

    cin >> testy;

    for(int i=1;i<=testy;i++)
    {
        cin >> n;

        for(int j=0;j<n;j++)
        {
            cin >> tabn[j];
        }
        for(int j=0;j<n;j++)
        {
            cin >> tabk[j];
        }

        sort(tabn,tabn+n);
        sort(tabk,tabk+n);

        lwk=0;
        pwk=n-1;
        wwynik=0;
        pdk=n-1;
        ldk=0;
        dwynik=0;

        for(int j=n-1;j>=0;j--)
        {
            if(tabn[j]>tabk[pwk])
            {
                wwynik++;
                lwk++;
            }
            else
            {
                pwk--;
            }
        }

        for(int j=0;j<n;j++)
        {
            if(tabn[j]>tabk[ldk])
            {
                dwynik++;
                ldk++;
            }
            else
            {
                pdk--;
            }
        }

        cout << "Case #" << i << ": " << dwynik << " " << wwynik << endl;
    }

    return 0;
}
