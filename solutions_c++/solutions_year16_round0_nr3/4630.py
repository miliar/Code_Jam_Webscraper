#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    cout<<"Case #1:" <<endl;
    int N, J;
    int j_count = 0;
    cin >> N >> J;
    unsigned long long int pwrs[11][32];
    for(int i = 2; i <= 10; i++)
    {
        unsigned long long int r = 1;
        for(int j = 0; j < 32; j++)
        {
           pwrs[i][j] = r;
           r *= i;
          // cout<<pwrs[i][j] << " ";
        }
        //cout<<endl;
    }
    unsigned long long int num[33] = {0};
    num[N-1] = 1;
    num[0] = 1;
    while(1)
    {
        if(num [0] != 1)
            continue;
        vector <int> div(11,0);
        for(int i = 2; i <= 10; i++)
        {
            unsigned long long int temp = 0;
            for(int j = 0; j < N; j++)
            {
                temp += pwrs[i][j] * (num[N-1-j]);
                //numTemp = numTemp / 10;
                //cout << "i = " << i << "   temp = " <<temp << "   j = " << j << " pwrs[i][j] = "<< pwrs[i][j]<< endl;
            }
           // cout<<i<<": "<< temp << endl;
            if(temp % 2 == 0)
            {
                div[i] = 2;
              //  cout<<div[i]<<endl;
                continue;
            }
            for(int a = 3; a <= sqrt(temp); a+=2)
            {
                if(temp % a == 0)
                {
                    div[i] = a;
                //    cout<<div[i]<<endl;
                    break;
                }
            }
            if(div[i] == 0) break;
        }
        if(div[10] != 0)
        {

            for(int k = 0; k < N; k++)
                cout<<num[k];
            for(int b = 2; b <= 10; b++)
            {
                cout<< " " << div[b];
            }
            cout << endl;
            j_count ++;
            if(j_count == J)
                return 0;
        }
        int p = 1;
        int carry = 0;
        if(num[p] == 0)
        {
            num[p] = 1;
        }
        else
        {
            num[p] = 0;
            carry = 1;
            p++;
            while(carry != 0)
            {
                if(num[p] == 0)
                {
                    num[p] = 1;
                    break;
                }
                else num[p] = 0;
                p++;
            }
        }
    }


    return 0;
}
