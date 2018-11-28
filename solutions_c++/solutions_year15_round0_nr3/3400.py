#include <bits/stdc++.h>
using namespace std;

long long int arr[1000005];
long long int mat[5][5] = {
    {
        0,0,0,0,0
    },
    {
        0,1,2,3,4
    },
    {
        0,2,-1,4,-3
    },
    {
        0,3,-4,-1,2
    },
    {
        0,4,3,-2,-1
    }
};

long long int mul(long long int a,long long int b) {

    long long int m;
    m = abs(a)/a;
    m = m*mat[abs(a)][abs(b)];
    return m;

}


int main() {

    long long int t,c,l,ln,x,y,i,j,k,sum,fi,fj,fk;

    cin >> t;
    for (c=1;c<=t;c++) {

		memset(arr,0,sizeof(arr));
		//char str[1000005],temp[10005],tmp[5];
		string str,temp;
        cin >> l >> x;
        cin >> temp;
//        gets(tmp);
//        gets(temp);
        ln = temp.length();

        for(i=0;i<x;i++) {
            str = str+temp;
        }

        for(i=0;i<ln*x;i++) {
            arr[i] = str[i] - 'i' + 2;
        }

        fi = fj = fk = sum = 0;
        y=1;
        for (i=0;i<ln*x;i++) {

            y = mul(y,arr[i]);

            if(y == 2 && (!fi) && (!fj) && (!fk)) {
                fi=1;
                y=1;
                sum = 1;
            }

            if(y == 3 && (fi) && (!fj) && (!fk)) {
                fj=1;
                y=1;
                sum = 10*sum+2;
            }

            if(y == 4 && (fi) && (fj) && (!fk) && i==x*ln-1) {
                fk = 1;
                sum = 10*sum + 3;
            }
        }

        if (fi == 1 && fj == 1 && fk == 1) {

            cout << "Case #" << c << ": YES" << endl;

        }
        else {

            cout << "Case #" << c << ": NO" << endl;

        }

    }
    return 0;
}
