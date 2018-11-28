#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <climits>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
#include <map>
//#include<unordered_map>
#include <set>
using namespace std;


#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rev(j,n) for(int (i)=j;(i)>=(int)(n);--(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
#define vec vector
#define pii pair<int,int>
#define pis pair<int, string>
#define psi pair<string,int>
#define pli pair<lli,lli>
typedef vec<int> vi;
typedef vec<vi > vii;
typedef vec<pii > vpii;
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define modu 1000000007
#define endl "\n"
#define fir first
#define sec second


int main(){
    //int t;
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    ulli l,r,n,t,m,k;
    fin>>t;
    rep(i,t){
        fin>>n;
        fout<<"Case #"<<i+1<<": ";

        if(n==0){
            fout<<"INSOMNIA\n";
        }else{
            vector<bool> digits(10);
            rep(i,9)
                digits[i]=false;
            int counter =0,d,mul=1,sheep=n;
            ulli num2=n,num=n;
            while(counter<10){
                num2=n*mul;
                num = num2;
                while(num2){
                    d = num2%10;
                    if(digits[d]==false){
                        counter++;
                        digits[d]=true;
                    }
                    num2/=10;
                }
                mul++;
            }
            fout<<num<<endl;
        }

    }

    fin.close();
    fout.close();


    return 0;
}
