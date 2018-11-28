#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long int
#define ll long long int

#define max_n 1e6
#define segment_size 1001
#define MOD (1e9 + 7)


ll power(ll a,ll b,ll c){
	ll x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x = (x*y)%c;
            //x= mulmod(x,y,c);
        }
        y = (y*y)%c;
        //y = mulmod(y,y,c); // squaring the base
        b >>=1;
    }
    return x%c;
}
string convert_base( ll  S  , ll len ){
          string x;
          if(!S)
            x = '0';
          while(S){
            x += (S%2 + '0');
            S/=2;
          }
          reverse(x.begin(),x.end());
       string y ;
       y = '1';
       for( int i = 1 ;  i <= len - x.size() - 2 ; ++i )
              y += '0';
       y += x;
       y += '1';
       return y;
}
int main()
{
      ofstream cout("out.txt");
    int t;
    cin>>t;
    cout << "Case #1:"<<endl;
    vector<int > divisor;
        ll N , J;
        cin>>N>>J;
        for(int i=0;i< pow(10,6) && J ; i++){
            string S = convert_base( i , N );
            for(int base =2 ; base<=10;base++){
                for(int k=2;k<=100;k++){
                    ll rem =0;
                for(int j=S.size()-1 , l =0;j>=0;j-- , l++){
                    if(S[j]-'0'){
                        rem = (rem + power(base , l, k))%k;
                    }
                }

                if(rem==0){
                    divisor.push_back(k);
                    break;
                }
        }
            }
        if(divisor.size()==9){
                cout << S << " ";
        for(int I  = 0 ; I < divisor.size() ; ++I )
               cout << divisor[I] << " ";
        cout << endl;
              --J;
            }
        divisor.clear();
        }
    return 0;
}
