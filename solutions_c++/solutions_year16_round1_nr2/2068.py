#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<queue>
using namespace std;


int main() {

    long long int n,k,l;
    cin>>n;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    for(long long int i=0;i<n;i++)
        {
        cin>>k;
        long long int c=2*k-1;
        c=c*k;
      long long int num[100000]={0};
        for(long long int k=0;k<c;k++)
        {
                cin>>l;
                num[l]++;
        }

        cout<<"Case #"<<i+1<<": ";
        for(long long int k=0;k<=3000;k++)
        {
            if(num[k]%2!=0 && num[k]!=0)
                cout<<k<<" ";

        }
        cout<<"\n";

    }



    return 0;
}
