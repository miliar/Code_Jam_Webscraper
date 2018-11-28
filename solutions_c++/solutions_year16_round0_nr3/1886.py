//IN THE NAME OF ALLAH
//1395/01/21

#include <bits/stdc++.h>
#include <fstream>
#define mp make_pair
#define pb push_back
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");
typedef long long int ll;
typedef long double ld;
typedef pair < ll, ll > pii;
typedef vector < ll > vi;
typedef set < ll > si;
const ld pi=3.1415926535897932384626433832795028841971693993751;
const ll maxn=2*1e8+1,inf=1e9+1,del=1e9+7;
ll t,n,j,p2[33];
int main(){
    ios_base::sync_with_stdio(0);fin.tie(0);fout.tie(0);
    fin>>t>>n>>j;
    fout<<"Case #1: "<<endl;
    for(int i=1;i<31;i+=2){
        for(int k=2;k<32;k+=2){
            fout<<1;
            for(int t=1;t<31;t++){
                if(t==i || t==k)
                    fout<<1;
                else
                    fout<<0;
            }
            fout<<1<<" ";
            for(int i=3;i<=11;i++)
                fout<<i<<" ";
            fout<<endl;
            j--;
        }
    }
    for(int i=3;i<31;i+=2){
        for(int k=2;k<32;k+=2){
            for(int h=k+2;h<32;h+=2){
                fout<<11;
                for(int t=2;t<31;t++){
                    if(t==i || t==k || t==h)
                        fout<<1;
                    else
                        fout<<0;
                }
                fout<<1<<" ";
                for(int i=3;i<=11;i++)
                    fout<<i<<" ";
                fout<<endl;
                j--;
                if(!j)
                    return 0;
            }
        }
    }
    return 0;
}
