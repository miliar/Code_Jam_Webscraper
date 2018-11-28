#include <iostream>
//#include <conio.h>
#include <string.h>
#include <math.h>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int t, n, cnt = 0, subnum = 0;
	string s;
	cin >> t;
	//cout << t;
	for(int i = 0 ; i < t ; i++)
	{
        cin >> s >> n;
        //cout << s <<  "  " << n;
        subnum = 0;
        for(int j = 0 ; j < s.size() ; j++)
        {
            cnt = 0;
            if(s.size() - j < n)
            {
                break;
            }
            for(int k = j ; k < s.size() ; k++)
            {
                if(s[k] != 'a' && s[k] != 'o' && s[k] != 'u' && s[k] != 'i' && s[k] != 'e')
                {
                    //cout << "s[k]    " << s[k] << endl;
                    cnt++;
                    //cout << "cnt    " << cnt << endl;
                    if(cnt >= n)
                    {
                       subnum += s.size() - k;
                       //cout << "subnum    " << subnum << endl;
                       break;
                    }
                }
                else
                {
                    cnt = 0;
                    //cout << "cnt else    " << cnt << endl;
                }
            }
        }
        cout << "Case #" << i+1 <<": "<< subnum;
        if(i + 1 != t)
             cout <<endl;
    }
    /*int tc, r, t, r1, r2;
    double rs;
    /*cin >> tc;
    //for(int i = 0 ; i < tc ; i++)
    {
        cin >> r >> t;
        r1 = r + 8;//+2
        r2 = r + 9;//+2
        rs = (M_PI * r1 * r1) - (M_PI * r2 * r2);
        rs /= M_PI;
        cout << rs << endl;
    }*/
    /*double mn = 1.23445e-2;
    cout << mn << endl;
    double zz = 1.348e-3;
    cout << zz << endl;
    if(mn < zz)
        cout << "m" << endl;
    else
        cout << "mm" << endl;*/
    //getch();
    return 0;
}
