#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include <climits>
#include <vector>
#include <functional>
#include <cstring>
#include <list>
#include <fstream>
#include <map>
#include <cmath>
#include <cctype>
#include <fstream>
using namespace std;

typedef long long ll;

int main(){
    ofstream ofs("c_output");
    int t, n=1;
    cin >> t;
    while(t+1>n){
        ll bg, end, cnt=0;
        cin >> bg >> end;
//        cout << bg << end;
        for (ll i = bg; i <= end; ++i){
            bool sq=false, pa=false;
            //sq判定
            ll s;
            for (ll j = 1; j*j <=i ; ++j){
                if(j*j == i){
                    sq = true;
                    s=j;
                    //cout << "sq trueな数: " << i << endl;
                    break;
                }
            }
            //paの判定
            if(sq){
                ll p=i, l=1, l2=1, p2=s;
                    for(ll j=0;;j++){
                        if(p/10==0)
                            break;
                        p /= 10;
                        l++;
                    }
                    for(ll j=0;;j++){
                        if(p2/10==0)
                            break;
                        p2 /= 10;
                        l2++;
                    }
//                    cout << "sqrt: " << s << endl;
//                    cout << "sqrtの桁数: " << l2 << endl; 
//                cout << "桁数: " << l << " 数: " <<  i << endl;
                    if(l==1)
                        pa=true;
                    else if(l2==1 || s/10%10 == s%10){
                        if(l==3){
                            if(i/100 == i%10)//最大位の数字==1の位の数字
                                pa=true;
/*                    for (int j = 1; j <= l/2; ++j){
                      if((i/(10^j)%10) != (i/(10^(l-1-j))%10))
                      pa=false;
                      }
*/
                        }else if(l==2){
                            if(i/10 == i%10)
                                pa = true;
                        }
                    }
                if(sq && pa){
                    cnt++;
//                    cout <<"選択した数: "<< i << endl;
                }
            }
        }
        ofs << "Case #" << n << ": "<< cnt << endl;
        n++;
    }
	return 0;
}

