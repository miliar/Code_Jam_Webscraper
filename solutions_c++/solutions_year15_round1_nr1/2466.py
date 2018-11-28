#include <iostream>
#include <math.h>
#include <stdio.h>
#include <cstdlib>
using namespace std;

#define REP(i, a, b)\
    for(int i = (int)a; i<=(int)b ; i++)
int main()
{
    int t; cin>>t;
    int count = 0;
    while(t--){
        count++;
        int n;
        cin>>n;

        int A[n+1];
        int mx = 0;

        for(int i = 0; i < n; i++){
            cin>>A[i];

        }
        int ans1 = 0;
        for(int i = 0; i < n-1; i++){
            if(A[i+1]<A[i]){
                ans1+= A[i]-A[i+1];
                mx = max(mx, A[i]- A[i+1]);
            }
        }


        int ans2 = 0;
        for(int i = 0; i<n-1; i++){
            ans2+= A[i]<=mx? A[i]:mx;
        }

        cout<<"Case #"<<count<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}

