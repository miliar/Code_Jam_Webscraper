#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <iomanip>
using namespace std;
#define ll         long long
#define ld         long double
#define pb         push_back
#define mp         make_pair
#define sz(x)      (int)(x.size())
#define lp(i,n)    for (int i=0; i<n ; ++i)
#define lp1(i,n)   for (i=1; i<=n; ++i)
#define lpa(i,a,b) for (i=a; i<=b; ++i)
#define lpd(i,n)   for (i=(n)-1; i>=0; --i)
#define lpd1(i,n)  for (i=n;     i>0 ; --i)
#define lpb(i,a,b) for (i=b; i>=a; --i)
#define amin(a,b)  a=min(a,b)
#define amax(a,b)  a=max(a,b)
#define all(s)     (s).begin(),(s).end()
#define fill(s,v)  memset(s,v,sizeof(s))
int main () {
    //freopen("input.txt", "r", stdin);         //freopen("output.txt", "w", stdout);
	freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.txt", "w", stdout);
	//freopen("A-large.in", "r", stdin);          freopen("A-large.out", "w", stdout);

    int ti=0,tn=1;  cin>>tn; //cout<<tn<<"\n";
    //cin.getline(ds,10);  //uncomment this to start reading string - dummy read

    while(ti++ < tn){
            printf("Case #%d: ",ti);
        //declarations:**************************************************
            char a[1001];
            int s[27] = {};
            int n,j =0,max=0,f=1,sm =0,c =0;

        //input:  *******************************************************
            cin>>n;
            lp(i,n){
                cin>>s[i];
                sm =sm+s[i];
            }
//cout<<sm<< " ";
        //Logic:  *******************************************************

            while(f){
                max = 26; f=0;
                lp(i,n){
                    if(s[max]<s[i]) { max = i; f=1;}
                }
                if(f) {
                    c++;
                    if(((sm-c) == 1)&&(sm != 2)){
                        a[j++] = ' '; //cout<<c<<" ";
                    }
                    else if((c%2)&&(c!=1)&&(sm!=c)) { a[j++] = ' ';}
                    a[j++] = 'A' + max;
                    s[max]--;

                }
            }







        //Output: *******************************************************
            lp(i,j){

                    printf("%c",a[i]);


            }

            printf("\n");
    }//end of one test case

    return 0;
}
