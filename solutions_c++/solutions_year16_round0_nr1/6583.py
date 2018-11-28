#include <bits/stdc++.h>
using namespace std;

int T, len;
long long int N, num, num_copy, dig, cont;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("out_A1_large.txt");
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N;
        if(N == 0){
            cout << "Case #" << t << ": " << "INSOMNIA" << "\n";
            continue;
        }
        vector<int> nums(13);
        cont = 1;
        num = N;
        while(nums[10] < 10){
            num = N*cont;
            num_copy = num;
            while(num > 0){
                dig = num%10;
                num /= 10;

                if(nums[dig] == 0){
                    nums[dig] = 1;
                    nums[10]++;
                }
            }
            cont++;
        }
        cout << "Case #" << t << ": " << num_copy << "\n";
    }
    return 0;
}

