#include <bits/stdc++.h>
using namespace std;
int T,J,K,lim=14,cnt;
int arr[15];
long long power(long long x,int y){long long res=1;for(int k=0;k<y;k++)res*=x;return res;}
bool isnotprime(long long x){for(int k=2;k<1e4;k++)if(x%k==0)return true;return false;}
long long returndiv(long long x){for(int k=2;k<1e4;k++)if(x%k==0)return k;return 0;}
long long base2(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(2,i+1); numri+=1;numri+=power(2,15);return numri;}
long long base3(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(3,i+1); numri+=1;numri+=power(3,15);return numri;}
long long base4(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(4,i+1); numri+=1;numri+=power(4,15);return numri;}
long long base5(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(5,i+1); numri+=1;numri+=power(5,15);return numri;}
long long base6(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(6,i+1); numri+=1;numri+=power(6,15);return numri;}
long long base7(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(7,i+1); numri+=1;numri+=power(7,15);return numri;}
long long base8(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(8,i+1); numri+=1;numri+=power(8,15);return numri;}
long long base9(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(9,i+1); numri+=1;numri+=power(9,15);return numri;}
long long base10(){long long numri=0;for(int i=0;i<=13;i++)numri+=arr[i]*power(10,i+1); numri+=1;numri+=power(10,15);return numri;}
void rec(int ind)
{
    if(ind==lim)
    {if(isnotprime(base2())&&
       isnotprime(base3())&&
           isnotprime(base4())&&
              isnotprime(base5())&&
                 isnotprime(base6())&&
                    isnotprime(base7())&&
                       isnotprime(base8())&&
                        isnotprime(base9()) &&
                            isnotprime(base10()))
        if(cnt<50){
                cout<<1;
        for(int j=13;j>=0;j--)
            cout<<arr[j];
        cout<<1;
        cout<<" ";
        cout<<returndiv(base2())<<" "<<returndiv(base3())<<" "<<returndiv(base4())<<" "<<returndiv(base5())<<" "<<returndiv(base6())<<" "<<returndiv(base7())<<" "<<returndiv(base8())<<" "<<returndiv(base9())<<" "<<returndiv(base10())<<"\n";
        cnt++;
        }

        return;}
    arr[ind]=1;
    rec(ind+1);
    arr[ind]=0;
    rec(ind+1);

}
int main()
{
   freopen("output.out","w",stdout);
cin>>T;
int kot1,kot2;
cin>>kot1>>kot2;
cout<<"Case #1:\n";
rec(0);



    return 0;
}
