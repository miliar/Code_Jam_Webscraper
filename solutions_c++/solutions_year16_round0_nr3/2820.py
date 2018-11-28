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
	lld test,n,i,j,k,a,b,c,t,d,e,r,m;
	cin>>test;
	for(t=1;t<=test;t++){
        cin>>n>>j;
        a=(lld)ceil(pow(10,n-1))+1;
        lld z=(lld)ceil(pow(2,n-1))+1;
        b=0;
        cout<<"Case #"<<t<<":"<<endl;
        while(b<j){
            lld arr[11];
            lld f=0,f1;
            for(i=2;i<=10;i++){
                c=a;
                k=0;
                d=0;
                while(c>0){
                    r=c%10;
                    k=k+r*(lld)ceil(pow(i,d));
                    d++;
                    c=c/10;
                }
               // cout<<k<<endl;
                f1=0;
                for(m=2;m<=sqrt(k);m++){
                    if(k%m==0){
                        f1=1;
                        break;
                    }
                }
                if(f1==0){
                        f=1;
                    break;
                }
                else{
                    arr[i]=m;
                }
            }
            if(f==0){
                b++;
                cout<<a<<" ";
                for(i=2;i<=10;i++){
                    cout<<arr[i]<<" ";
                }
                cout<<endl;
            }
            //next number
            z+=2;
            e=z;
            lld nn=0;
            d=0;
            while(e>0){
                r=e%2;
                nn=nn+r*(lld)ceil(pow(10,d));
                d++;
                e=e/2;
             //   cout<<nn<<" ";
            }
            a=nn;
           // cout<<"next number"<<a<<endl;
        }

	}
    return 0;
}
