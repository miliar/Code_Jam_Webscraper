#include<iostream>
#include<cstdio>
#include<cmath>
#include<fstream>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","right",stdin);
    freopen("output.txt","w",stdout);
    int temp;
    bool flag = false;
    int test;
    cin >> test;
    for(int loop1=1; loop1<=test; loop1++) {
        double c,f,x, right, left;
        cin >> c >> f >> x;
        temp += int(c + f + x);
        right = 2.0;
        left = x;
        temp += (int)(right * left);
        double tim = 0.0, ans = x/right;
        while(left>=c) {
            flag = (tim >= (c/right));
            tim = tim + c/right;
            right += f;
            left -= c;
            temp += left;
            double temp1 = tim + x/right;
            if(temp1 < ans) {
                ans = temp1;
            }
            temp = ans;
        }
        tim = tim + x/right;
        if(floor(tim-ans)<0) {
            ans = tim;
        }
        temp = ans;
        cout << "Case #" << loop1 << ": ";
        printf("%.7lf\n",ans);
    }
}
