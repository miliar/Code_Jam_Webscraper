/*
 * =====================================================================================
 *
 *       Filename:  1.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2014/04/12 17时44分38秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int t;
    cin>>t;
    for (int ncase = 1; ncase <= t; ncase++) {
        int data[4][4];
        int firAns[4];
        int fi, se;
        cin>>fi;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>data[i][j];
                if (i + 1 == fi) {
                    firAns[j] = data[i][j];
                }
            }
        }
        cin>>se;
        int matched = 0;
        int matval = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>data[i][j];
                if (i + 1 == se) {
                    for (int k = 0; k < 4; k++) {
                        if (firAns[k] == data[i][j]) {
                            matched++;
                            matval = data[i][j];
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<ncase<<": ";
        switch (matched) {
            case 0:
                cout<<"Volunteer cheated!"<<endl;
                break;
            case 1:
                cout<<matval<<endl;
                break;
            default:
                cout<<"Bad magician!"<<endl;
                break;
        }
    }
    return 0;
}
