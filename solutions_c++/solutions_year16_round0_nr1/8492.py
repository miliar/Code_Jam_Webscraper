#include <iostream>

using namespace std;

int nums[9];
int sleep(int m){
    while(m > 0){
        nums[m % 10] = 1;
        m /= 10;
    }
    return nums[0] * nums[1] * nums[2] * nums[3] * nums[4] * nums[5]
           * nums[6] * nums[7] * nums[8] * nums[9];
}

int main()
{
    int N, m, k;
    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> m;
        for(int j = 0; j <= 9; j++)
            nums[j] = 0;
        if(m == 0)
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        else{
            k = m;
            while(sleep(m) == 0)
                m += k;
            cout << "Case #" << i << ": " << m << endl;
        }
    }
    return 0;
}
