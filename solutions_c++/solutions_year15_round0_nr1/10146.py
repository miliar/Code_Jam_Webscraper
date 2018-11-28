#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
int main()
{
        int n,max,sum,audience[1000]={},ans[100]={};
        string str;
        char chr;

        cin >> n;

        for(int i=0; i<n; i++){
                cin >> max;
                cin >> str;
                sum = 0;
                for(int j=0; j<=max; j++){
                        chr = str[j];
                        if(sum < j && atoi(&chr) != 0){
                                ans[i] += j - sum;
                                sum += j - sum;
                        }
                        sum += atoi(&chr);
                }
        }

        for (int i=0; i<n; i++){
                cout << "Case #" << i+1 << ": " << ans[i]       << endl;
        }
}