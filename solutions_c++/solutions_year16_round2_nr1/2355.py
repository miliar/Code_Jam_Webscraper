#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    long list[27];
    string str;
    int total;
    vector<int> v;

    for(int i = 0; i < n; i++){

        cin >> str;
        v.clear();
        for(int j = 0; j < 27; j++){
            list[j] = 0;
        }
        total = str.size();

        for(int j = 0; j < str.size(); j++){
            list[(int)(str[j]-'A'+1)]++;
        }
        while(total > 0){
            if(list[19] > 0 && list[9] > 0 && list[24] > 0){
                v.push_back(6);
                total -= 3;
                list[19]--;
                list[9]--;
                list[24]--;
            } else
            if(list[26] > 0 && list[5] > 0 && list[18] > 0 && list[15] > 0){
                v.push_back(0);
                total -= 4;
                list[26]--;
                list[5]--;
                list[18]--;
                list[15]--;
            }else
            if(list[9] > 0 && list[5] > 0 && list[7] > 0 && list[8] > 0 && list[20] > 0){
                v.push_back(8);
                total -= 5;
                list[9]--;
                list[5]--;
                list[7]--;
                list[8]--;
                list[20]--;
            }else
            if(list[20] > 0 && list[23] > 0 && list[15] > 0){
                v.push_back(2);
                total -= 3;
                list[20]--;
                list[23]--;
                list[15]--;
            }else
            if(list[6] > 0 && list[15] > 0 && list[21] > 0 && list[18] > 0){
                v.push_back(4);
                total -= 4;
                list[6]--;
                list[21]--;
                list[18]--;
                list[15]--;
            }else
            if(list[6] > 0 && list[9] > 0 && list[22] > 0 && list[5] > 0){
                v.push_back(5);
                total -= 4;
                list[6]--;
                list[5]--;
                list[22]--;
                list[9]--;
            }else
            if(list[19] > 0 && list[5] > 1 && list[22] > 0 && list[14] > 0){
                v.push_back(7);
                total -= 5;
                list[19]--;
                list[5]-=2;
                list[22]--;
                list[14]--;
            }else


            if(list[20] > 0 && list[8] > 0 && list[18] > 0 && list[5] > 1){
                v.push_back(3);
                total -= 5;
                list[20]--;
                list[5]-=2;
                list[18]--;
                list[8]--;
            }else





            if(list[14] > 1 && list[9] > 0 && list[5] > 0){
                v.push_back(9);
                total -= 4;
                list[14]-=2;
                list[5]--;
                list[9]--;

            }else
            if(list[15] > 0 && list[14] > 0 && list[5] > 0){
                v.push_back(1);
                total -= 3;
                list[15]--;
                list[5]--;
                list[14]--;
            }

        }

        sort(v.begin(),v.end());
        cout << "Case #" << i+1 << ": ";
        for(int j = 0; j < v.size(); j++){
            cout << v[j];
        }
        cout << endl;
    }
    return 0;
}
