#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	string str;
	lld test,n,i,j,k,a,b,c,t;
	cin>>test;
	for(t=1;t<=test;t++){
        cin>>n;
        if(n==0){
            cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int arr[11]={};
        a=0;
        i=1;
        j=n;
        while(a!=10){
            n=j*i;
            b=n;
            while(b>0){
                c=b%10;
                if(arr[c]==0){
                    arr[c]=1;
                    a++;
                }
                b=b/10;
            }
            i++;

        }
        cout<<"Case #"<<t<<": "<<n<<endl;
	}
    return 0;
}
