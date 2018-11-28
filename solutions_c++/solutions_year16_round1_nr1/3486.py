#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string input, output_pre, output_last;


int findLastBiggest(int n){
    int temp = 0;
    for (int i = 0; i < n; ++i){
        if (input[temp] <= input [i]){
            temp = i;
        }
    }
    return temp;
}

int main(){

    freopen ("large.in","r",stdin);
    freopen ("large.out","w",stdout);
    int T;
    scanf("%d\n", &T);

    for (int t = 1; t <= T; ++t){
        cin >> input;
        output_pre = output_last = "";
        int currentBiggest, lastBiggest = input.length();
        while (lastBiggest){
            currentBiggest = findLastBiggest(lastBiggest);
            if (currentBiggest < lastBiggest - 1){
                output_last = input.substr(currentBiggest + 1, lastBiggest - currentBiggest - 1) + output_last;
            }
            output_pre = output_pre + input[currentBiggest];
            lastBiggest = currentBiggest;
        }

        printf("Case #%d: ", t);
        cout << output_pre << output_last << endl;

    }
}
