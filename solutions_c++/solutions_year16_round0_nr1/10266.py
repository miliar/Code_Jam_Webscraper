#include <bits/stdc++.h>
#include <string>
#include<sstream>
#include <iostream>
#define INF 1000000010
#define FO(i,a,b) for (long long int (i) = (a); (i) < (b); (i)++)

using namespace std;

long long int T, N,M;
string s;
string ans="";
int main() {
    freopen ("A-large.in", "r", stdin);
    freopen ("A_final_large.out", "w", stdout);
    cin>>T;
    FO (_z,0,T) {
        printf ("Case #%d: ", _z+1);
        bool arr[10]={};
        bool pp=false;
        cin>>N;
        M=N;
        int ii=1;
        while(!pp){
            if(N==0) break;
            N=M*ii;
          std::ostringstream os ;
          os << N ;
          s =os.str();
          char ss;
        FO(_y,0,s.length())  {
            ss= s[_y];
        arr[atoi(&ss)]=true;
         }
        FO (_x,0,10) {
            if(arr[_x]) {
            pp=true;
            continue;
            }
            else{
            pp=false;
            break;
            }
        }
       // cout<<"\n";
        // FO (_v,0,10) {
        //    cout<<arr[_v]<<" ";
       // }

        ii++;
        }
        if(N==0) printf ("INSOMNIA\n");
        else cout<<N<<"\n";
    }
    return 0;
}
