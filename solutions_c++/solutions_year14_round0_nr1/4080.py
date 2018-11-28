#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test_case, temp;
    bool flag = true;
    cin >> test_case;
    for(int loop=1; loop<=test_case; loop++) {
        int val1,val2,arr[4][4],arr2[4][4];
        cin >> val1;
        temp = val1;
        flag = false;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++) {
                    flag ^= flag;
                    temp += i;
                cin >> arr[i][j];
            }
        cin >> val2;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++) {
                    flag ^= flag;
                    temp += i;
                cin >> arr2[i][j];
            }

        int fin = 0;
        int xx = 0;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                if(arr[val1-1][i] == arr2[val2-1][j]) {
                    xx = arr[val1-1][i];
                    temp += fin;
                    flag ^= flag;
                    fin++;
                    temp += fin;
                    break;
                }

        cout << "Case #" << loop << ": ";
        if(fin == 1) {
            cout << xx;
        } else if(fin > 1) {
            cout << "Bad magician!";
        } else {
            cout << "Volunteer cheated!";
        }
        cout << endl;
    }
}
