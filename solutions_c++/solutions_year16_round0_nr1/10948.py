#include<bits/stdc++.h>
using namespace std;

int data[20] = {0};

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
	int T, N, last, x=0, r=0, p;
	cin >> T;
	for(int i=1; i<=T; i++) {
        cin >> N;
        memset(data, 0, sizeof(data));
        if(N==0) {
            cout << "Case #"<< i <<": " << "INSOMNIA" << endl;
            continue;
        }
        int j=1;
        int a=0;
            p=0;
        while(1) {
            x = N*j;
            while(x!=0) {
                r = x%10;
                data[r] = 1;
                x = x/10;
            }
            a = 0;
            p = 0;
            while(data[a++]) {
               p++;
            }
            if(p==10) {
                cout << "Case #"<< i <<": " << N*j << endl;
                break;
            }
            j++;
        }
	}

}




/**




#include<bits/stdc++.h>
using namespace std;
int k,n,i,a,arr[1005];
int main()
{
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>a;
		cout << arr[a] << " ";

//		k=max(k,arr[a]);
	}
	cout<<n-k;

}
*/


/**
#include <bits/stdc++.h>
using namespace std;

const int inf=1000000007;
long long int bigmod(int b,int p,int m)
{
    if(p==0) return 1;
    long long res=bigmod(b,p/2,m);
    res=(res*res)%m;
    if(p%2==1)
        res=(res*b)%m;
    return res;
}
int main()
{
    int b,p,m;
    while(cin>>b>>p>>m)
    {
        cout<<bigmod(b,p,m)<<endl;;
    }
    return 0;
}
*/
