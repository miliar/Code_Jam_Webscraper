using namespace std;
#include <iostream>
#include <fstream.h>

int main() {
    ofstream outPutFile("output2.txt");
    int case_num, shy_max, shy_map;
    int* shy_arr;
    cin >> case_num;
    for(int i = 0; i < case_num; i++){
        cin >> shy_max;
        cin >> shy_map;
        shy_arr = new int[shy_max + 1];
        int acl = 0, need = 0;
        for(int j = 0; j <= shy_max; j++){
            shy_arr[shy_max - j] = (shy_map%10);
            shy_map /= 10;
        }
        for(int j = 1; j <= shy_max; j++) {
            acl += shy_arr[j - 1];
            if(acl < j){
                need += j - acl;
                acl = j;
            }
        }
        outPutFile << "Case #" << i + 1 << ": " << need << endl;
    }
    outPutFile.close();
    return 0;
}
