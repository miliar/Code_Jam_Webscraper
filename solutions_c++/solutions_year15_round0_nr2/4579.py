#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <queue>
#include <map>
#include <cstdlib>
#include <algorithm>
//ciao
#define ll long long
#define S(x) scanf("%d",&x)
#define Sf(x) scanf("%f",&x)
#define Slf(x) scanf("%lf",&x)
#define Sl(x) scanf("%lld",&x)
#define P(x)  printf("%d\n", x)
#define Pf(x)  printf("%f\n", x)
#define Plf(x)  printf("%lf\n", x)
#define Pl(x)  printf("%lld\n", x)
#define mem(x,i) memset(x,i,sizeof(x))
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,time,k,min,n,i,max,z,y,h;
    int a[10];
    vector<int>v;
    S(t);
    for (h = 1; h <= t;h++){
        S(n);
        for (i = 0; i < n; i++){
            S(a[i]);
        }
        if(n == 1){
            if(a[0] == 1){
                cout <<"Case #"<<h<<": "<<"1"<<endl;
                continue;
            }
            if(a[0] == 2){
                cout <<"Case #"<<h<<": "<<"2"<<endl;
                continue;
            }
            if(a[0] == 3){
                cout <<"Case #"<<h<<": "<<"3"<<endl;
                continue;
            }
            if(a[0] == 4){
                cout <<"Case #"<<h<<": "<<"3"<<endl;
                continue;
            }
            if(a[0] == 5){
                cout <<"Case #"<<h<<": "<<"4"<<endl;
                continue;
            }
            if(a[0] == 6){
                cout <<"Case #"<<h<<": "<<"4"<<endl;
                continue;
            }
            if(a[0] == 7){
                cout <<"Case #"<<h<<": "<<"5"<<endl;
                continue;
            }
            if(a[0] == 8){
                cout <<"Case #"<<h<<": "<<"5"<<endl;
                continue;
            }
            if(a[0] == 9){
                cout <<"Case #"<<h<<": "<<"5"<<endl;
                continue;
            }
        }
        for (i = 0; i < n; i++){
            v.push_back(a[i]);
        }
        k = v.size();
        sort(v.begin(),v.end());
        max = v[k-1];
        time = 0;
        min = 1000000;
        int m = 3;
        y = 0;
        while(y!=1){
            y = v[k-1];
            z = v[k-2];
            int tmp;
            tmp = __gcd(y,z);

            if(tmp != 1 && tmp != y){
                v.pop_back();
                v.push_back(tmp);
                v.push_back(y-tmp);
                sort(v.begin(),v.end());
            }
            else {
                v.pop_back();
                v.push_back(y/2);
                v.push_back(y - (y/2));
                sort(v.begin(),v.end());
            }
            if(time+y < min){
                min = time+y;
            }
           /* for (i = 0; i < v.size(); i++){
                    cout << v[i];
                }
                cout << " ";*/
            //cout << y<<" "<<z<<endl;
           // break;
         //  cout << min<<endl;
           k = v.size();
            time++;
        }
         v.clear();
        cout <<"Case #"<<h<<": "<<min<<endl;
    }
}
