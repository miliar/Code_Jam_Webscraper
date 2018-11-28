#include<iostream>
#include<queue>
using namespace std;

struct P{
    char c;
    int n;
};

bool operator<(P a, P b) {
    return a.n < b.n;
}

priority_queue< P > Q;

int A[500];

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        for(int i= 'A'; i<='Z'; i++)
            A[i]=0;
        int t = 0;
        int N;
        cin>>N;
        P p;
        for(int i=0; i<N; i++) {
            int x;
            cin>>x;
            t+=x;
            //A[i+'A'] = x;
            p.c = i + 'A';
            p.n = x;
            Q.push(p);
        }
        cout<<"Case #"<<tt<<": ";
        while(!Q.empty()) {

            p = Q.top();
           // if( (t%2 == 0 && t/2 < p.n) || (t%2==1 && t/2+1 <= p.n))
           //     cout<<"WRONG";
            Q.pop();
            p.n--;
            t--;
            cout<<p.c;
            if(p.n != 0) Q.push(p);

            if (Q.empty()) break;

            p = Q.top();
            if( t/2 >= p.n) {
                    cout<<" ";
                    continue;
            }
            Q.pop();
            p.n--;
            t--;
            cout<<p.c<<" ";
            if(p.n != 0) Q.push(p);
        }
        cout<<endl;
    }
    return 0;
}
