#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
     //ifstream cin("aa.txt");
       //ofstream cout("bb.txt");


         int  t , tt = 1;
         cin >> t;
         while(t--){
                 int ans , r , c , w;
                 cin >> r >> c >> w;
                   ans = ceil(c*1.0/w);
                    ans = ans*r;
                     ans = ans + w;
                     ans--;
                            cout << "Case #"<<tt++<<": "<<ans << endl;
         }
           return 0;
}

