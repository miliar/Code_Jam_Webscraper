#include<string>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;
int main(int argc, char **argv)
{
    signed long long int i, j, k;
    signed long long int numCases;
    cin >> numCases;

    for(int cases = 0; cases < numCases; cases++){
        std::cout << "Case #" << cases+1 << ": ";

        signed long long int numItems;
        cin >> numItems;

        signed long long int array[10] = {0};
        signed long long int num, res, sub_res, div = 10;
        bool flag= true;
        for(i = 1; i <= numItems*100; i++)
        {
                flag  = true;
                res = sub_res = i * numItems;
                for(j=0; sub_res > 0; j++)
                {
                    num = sub_res%div;
                    sub_res =sub_res/div;
                    array[num] = 1;
                }
                for(k=0; k < 10; k++) {
                    if(array[k] != 1) {
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    break;
                }
        }
        if(flag && numItems != 0) {
            cout << res;
        }
        else {
            cout << "INSOMNIA";
        }
        std::cout << std::endl;
    }
    return 0;
}
