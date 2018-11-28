#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

double a[1009], b[1009];

int main()
{
   //freopen("1.txt", "r", stdin);
    //freopen("2.txt", "w", stdout);
    int cases, n;
    cin >> cases;
    for (int t = 1; t <= cases; t++)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        for (int i = 0; i < n; i++)
            cin >> b[i];
        sort(a, a+n);
        sort(b, b+n);
        int war = 0;
        int de_war = 0;
        int i = n-1;
        int j = n-1;
        while(j >= 0)
        {
            if (a[i] > b[j]) 
            {
                i--;
                war++;
            }
            else
            {
                i--;
                j--;
            };
        }

        i = j = 0;
        while(i < n)
        {
            if (a[i] > b[j])
            {
                i++;
                j++;
                de_war++;
            }
            else i++;
        }
        cout << "case #" << t << ": " << de_war << " " << war << endl;
        
    }
    return 0;
}
