
#include <bits/stdc++.h>

using namespace std;

int arr [1000 + 10];


int main()
{

    //freopen ("file_name.X", "r", stdin);
freopen ("new.txt","w",stdout);

    int t; long long ans = 0 , bound = 0;
    long long sum = 0;
    string s , c;

    cin >> t;

    for(int i = 1; i <= t; i++){

        memset(arr , 0 , sizeof(arr));
        cin >> s >> c;

        for(int k = s.length() - 1, con = 1; k >= 0; k--){

            bound += (s[k] - '0') * con;
            con *= 10;
        }

        for(int j = 0 , k = 2; j <= bound; j++, k++){

            arr[j] = c[j] - '0';

            if(j > 0){

                if( j > sum && arr[j] != 0){
                    ans += j - sum;
                    sum += j - sum;
                }
            }
             sum += arr[j];
        }

        cout << "Case #" << i << ": " << ans << endl;
        sum = 0 , ans = 0 , bound = 0;


    }

    return 0;
}
