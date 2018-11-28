#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int x = 1;
    while (x <= t){
        int sm,cnt = 0;
        string str;
        cin >> sm;
        cin >> str;
        int sum = int(str[0]-'0');
        for(int i=1; i<sm+1; i++){
            if(int(str[i]-'0') != 0)
                if(sum < i){
                    cnt += i-sum;
                    sum += i-sum;
                }
            sum += int(str[i]-'0');
        }
        cout << "Case #" << x << ": " << cnt << endl;
        x++;
    }
    return 0;
}
