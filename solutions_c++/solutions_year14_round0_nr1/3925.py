#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int A[4][4], B[4][4], cnt, i, n, j, k, a, b, c, m,p=0;

    cin >> n;
    while(n--) {
            p++;
            cnt=0;
        cin >> i;
        i--;
        for(j = 0; j < 4; j++) {
                for(k = 0; k < 4; k++) {
                    cin >> A[j][k];
                }
        }
        cin >> a;
        a--;
        for(b = 0; b < 4; b++) {
                for(c = 0;c < 4;c++) {
                    cin >> B[b][c];
                }
        }
        for(k = 0;k < 4; k++) {
        for(j = 0;j < 4; j++) {
            if(A[i][k] == B[a][j]) {
                cnt++;
                m = A[i][k];
            }
        }
        }
        if(cnt == 1) {
            cout <<"Case #"<<p<<": "<< m<<endl;
        } else if(cnt == 0) {
            cout <<"Case #"<<p<<": Volunteer cheated!" << endl;
        } else {
            cout <<"Case #"<<p<<": Bad magician!"<< endl;
        }

    }
    return 0;
}
    /*for(n = 0; n < m; n++) {
        cin >> A[n];
        if(A[n] == 3/4) {
            i++;
        }
        if(A[n] == 1/4) {
            j++;
        }
        if(A[n] == 1/2) {
            k++;
        }
    }
    if(i == j) {
        cnt = cnt * (--i);
    } else if(i < j) {

    }



    return 0;
}*/
