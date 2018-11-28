#include <string>
#include <iostream>

using namespace std;

void convert(string &x)
{
    for(size_t i=0; i<x.length(); i++) {
        switch(x[i]) {
        case 'i': x[i] = 2; break;
        case 'j': x[i] = 3; break;
        case 'k': x[i] = 4; break;
        default: x[i] = 0; break;
        }
    }
}

const int mul[][5] = {{0,0,0,0,0}, {0,1,2,3,4}, {0,2,-1,4,-3}, {0,3,-4,-1,2}, {0,4,3,-2,-1}};

int doMul(int x, int y)
{
    int sign = 1;
    if(x<0) {
        sign *= -1;
        x *= -1;
    }
    if(y<0) {
        sign *= -1;
        y *= -1;
    }
    return sign*mul[x][y];
}

int compute(const string &x)
{
    int res = 1;
    for(size_t i=0; i<x.length(); i++) {
        res = doMul(res, x[i]);
    }
    return res;
}

int main()
{
    int T;
    int Tcnt = 1;
    cin>>T;
    for(; T; T--,Tcnt++) {
        long long L, X;
        string sample;
        cin>>L>>X;
        cin>>sample;
        if(L*X<3) {
            cout<<"Case #"<<Tcnt<<": NO"<<endl;
            continue;
        }
        convert(sample);
        //X%=12;
        int unit = compute(sample);
        int finalRes = 1;
        for(int i=0; i<X; i++) {
            finalRes = doMul(finalRes, unit);
        }
        int res = 1;
        int answer = 0;
        for(long long i=0; i<L*X; i++) {
            res = doMul(res, sample[i%L]);
            if(res == 2) {
                int resOut = 1;
                for(long long j=L*X-1; j>i+1; j--) {
                    resOut = doMul(sample[j%L], resOut);
                    if(resOut == 4) {
                        for(int mid = -4; mid<=4; mid++) {
                            if(mid==0) {
                                continue;
                            }
                            if(doMul(doMul(2, mid), 4) == finalRes) {
                                if(mid == 3) {
                                    answer = 1;
                                }
                                break;
                            }
                        }
                    }
                    if(answer) break;
                }
            }
            if(answer) break;
        }
        if(answer) {
            cout<<"Case #"<<Tcnt<<": YES"<<endl;
        } else {
            cout<<"Case #"<<Tcnt<<": NO"<<endl;
        }
    }
    return 0;
}

