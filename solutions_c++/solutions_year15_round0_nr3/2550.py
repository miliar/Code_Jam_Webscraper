#include<iostream>

using namespace std;
const char *yes = "YES";
const char *no = "NO";

int main()
{
    int T;
    int neg[4][4] = {0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1};
    int mul[4][4] = {0,1,2,3,1,0,3,2,2,3,0,1,3,2,1,0};
    int arr[10010];
    char c;

    cin>>T;
    for(int i = 0; i < T; i++) {
        int L, X;
        int isNeg = 0;

        cin>>L>>X;

        for(int k = 0; k < L; k++) {
            cin>>c;
            arr[k] = c - 'h';
        }

        int req_res = 1;
        int res = 0;
        for(int j = 0; j < X; j++) {
            for(int k = 0; k < L; k++) {
                isNeg = isNeg ^ neg[res][arr[k]];
                res = mul[res][arr[k]];
                if((req_res == res) && !isNeg) {
                    res = 0;
                    switch(req_res) {
                        case 1:
                        case 2: req_res++;
                                break;
                        case 3: req_res = 0;
                                break;
                    }
                }
            }
        }

        const char *res_str = ((req_res==0) && (res==0) && !isNeg)? yes: no;

        cout<<"Case #"<<i+1<<": "<< res_str;
        if(i != T-1)
            cout<<endl;
    }

    return 0;
}
