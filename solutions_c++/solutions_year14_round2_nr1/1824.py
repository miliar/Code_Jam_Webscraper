#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

string A, B;

int solve() {
    int n;
    cin>>n;
    cin>>A>>B;
    ///  minSize = min(Asize, Bsize), maxSize = max(Asize, Bsize),
    int Asize = A.size(), Bsize = B.size(), a=0, b=0, res = 0;

    if( (A[0] != B[0] ) or (A[Asize-1] != B[Bsize-1]) ) return -1;
  //  cout<<"moze sie da"<<endl;
    while( a<Asize and b<Bsize) {
        while(a<Asize and b<Bsize and A[a] == B[b] ) {
            a++; b++;
        }
    //    cout<<a<<" "<<b<<endl;
        if(a<Asize and b<Bsize and A[a] != B[b] ) {
            if(A[a-1] == B[b]) {
                res++;
                b++;
            }
            else if(A[a] == B[b-1]) {
                res++;
                a++;
            }
                else return -1;
        }
    }

    res += Asize-a + Bsize -b;

    return res;
}

int main(){
    ios_base::sync_with_stdio(0);
    int testy;
    cin>>testy;
    for(int i=1; i<=testy; ++i)
    {
        int ans = solve();
        cout<<"Case #"<<i<<": ";
        if(ans==-1) cout<<"Fegla Won";
        else cout<<ans;
        cout<<"\n";
    }
    return 0;
}
