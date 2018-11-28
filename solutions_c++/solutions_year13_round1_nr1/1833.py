#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
    int t,q=1;
    cin >> t;
    while(t--){
        long long int i,j,k,l,m,n,c=0;
        cin >> j >> k;
        m=j;
        for(i=0;i<100000;i++){
            l=((m+1)*(m+1)-(m)*(m));
          //  cout << l << endl;
            if(l>k)
                break;
            else {
                c++;
                k=k-l;
                m=m+2;
            }
        }
        cout << "Case #" <<q << ": " << c << endl;
        q++;
    }
    return 0;
}
