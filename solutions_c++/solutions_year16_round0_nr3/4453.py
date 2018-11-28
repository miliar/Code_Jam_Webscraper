#include<iostream>
#include<cstdlib>
using namespace std;
int A[51][20];
int fac[51][11];
long long int tobase(int wh, int b) {
    long long int cur = 1, num = 0;
    for(int i=0;i<16;i++) {
        num += cur*A[wh][i];
        cur *= b;
    }
    return num;
}

int getfac(long long int num) {
    for(long long int j = 2; j*j <= num; j++) {
        if(num%j==0) return j;
    }
    return -1;
}

int c = 0;
int gl=32768;
void getnext()
{
    while(1) {
        gl++;
        int tmp = gl;
        for(int i=0;i<16;i++)
        {
            A[c][i]=tmp%2;
            tmp/=2;
        }
        if(A[c][0] == 1 && A[c][15] == 1) {
            return;
        }
    }
}
int  main()
{
    int t;
    cin>>t;
    cout<<"Case #1:\n"; 
    while(c!=50) {
        getnext();
        int prime = 0;
        for(int i=2;i<=10;i++) {
            long long int num = tobase(c,i);
            int f = getfac(num);
            if(f==-1) {
                prime = 1;
                break;
            }
            fac[c][i] = f;
        }
        if(!prime) {
            c++;
        }
    }
    for(int i=0;i<50;i++) {
        for(int j=15;j>=0;j--) {
          cout<<A[i][j];
        }
        for(int j=2;j<=10;j++)
            cout<<" "<<fac[i][j];
        cout<<endl;
    }
    return 0;
}
