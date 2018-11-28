#include<iostream>
using namespace std;

long long calc(int N) {
    bool prs[10]={false};
    int cnt = 0;
    long long i=1;
    while(true) {
        long long tmp = i*N;
        while(tmp) {
            int l = tmp%10;
            if(prs[l]==false) {
                cnt++;
                if(cnt==10) {
                    return i*N; 
                }
                prs[l]=true;
            }
            tmp/=10;
        }
        i++;
    }
    return 0;
}

int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        int  N;
        cin>>N;
        //N = t;
        if(N==0)
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<t<<": "<<calc(N)<<endl;
    }
    return 0;
}
