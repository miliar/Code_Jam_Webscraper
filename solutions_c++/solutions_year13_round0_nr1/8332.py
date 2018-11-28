//
//  main.cpp
//  codejam
//
//  Created by stormluke on 13-4-13.
//  Copyright (c) 2013年 stormluke. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{

    int n;
    char a[4][4];
    cin >> n;
    for(int cs=1; cs<=n; cs++) {
        cout << "Case #" << cs << ": ";
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                cin >> a[i][j];
            }
        }
        
        int flag = 0;
        int nc = 0;
        for(int i=0;i<4;i++) {
            char start = a[i][0];
            if(start != '.') {
                int count = 1;
                for(int j=1;j<4;j++) {
                    if(a[i][j] == start || a[i][j] == 'T') {
                        count++;
                    } else if(a[i][j] == ',') {
                        nc = 1;
                    }
                }
                if(count == 4) {
                    char won = (start == 'T'? a[i][3] : start);
                    cout << won << " won";
                    flag = 1;
                }
            } else {
                nc = 1;
            }
        }
        if(!flag) {
            for(int j=0;j<4;j++) {
                char start = a[0][j];
                if(start != '.') {
                    int count = 1;
                    for(int i=1;i<4;i++) {
                        if(a[i][j] == start || a[i][j] == 'T') {
                            count++;
                        } else if(a[i][j] == ',') {
                            nc = 1;
                        }
                    }
                    if(count == 4) {
                        char won = (start == 'T'? a[3][j] : start);
                        cout << won << " won";
                        flag = 1;
                    }
                } else {
                    nc = 1;
                }
            }
        }
        if(!flag) {
            int count = 1;
            char start = a[0][0];
            if(start != '.') {
                for(int i=1;i<4;i++) {
                    if(a[i][i] == start || a[i][i] == 'T') {
                        count ++;
                    } else if(a[i][i] == ',') {
                        nc = 1;
                    }
                }
                if(count == 4) {
                    char won = (start == 'T'? a[3][3] : start);
                    cout << won << " won";
                    flag = 1;
                }
            } else {
                nc = 1;
            }
        }
        if(!flag) {
            int count = 1;
            char start = a[0][3];
            if(start != '.') {
                for(int i=1;i<4;i++) {
                    if(a[i][3-i] == start || a[i][3-i] == 'T') {
                        count ++;
                    } else if(a[i][3-i] == ',') {
                        nc = 1;
                    }
                }
                if(count == 4) {
                    char won = (start == 'T'? a[3][0] : start);
                    cout << won << " won";
                    flag = 1;
                }
            } else {
                nc = 1;
            }
        }
        if(!flag) {
            if(!nc) {
                cout << "Draw";
            } else {
                cout << "Game has not completed";
            }
        }
        
        cout << endl;
    }
    return 0;
}

