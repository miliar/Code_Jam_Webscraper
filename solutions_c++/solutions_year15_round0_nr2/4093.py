#include<bits/stdc++.h>
using namespace std;
struct data
{
 vector<int> in ;
};


int  d;
data Z ;

struct Comp
{
  bool operator()(const data& lhs, const data& rhs) const
  {
            if(lhs.in.size()!=rhs.in.size()) return lhs.in.size() < rhs.in.size() ;

         for(int i =0  ;i<lhs.in.size();i++ ) if(lhs.in[i]!=rhs.in[i]) return lhs.in[i]<rhs.in[i] ;
         return 0;
  }
};

map<data,int,Comp> mp ;


int solve(data Y)
{
   if(mp.count(Y)) return mp[Y];
    int ans = Y.in[Y.in.size()-1] ;
    if(ans<4) return ans ;


for(int i = 0;i<=Y.in.size()-1;i++)
{
    if(Y.in[i]<=3) continue ;
     for(int j = 2;Y.in[i]-j>=j;j++)
     {
            Z = Y ;
        Z.in[i] = j ; Z.in.push_back(Y.in[i]-j);

        sort(Z.in.begin() , Z.in.end() ) ;

       ans = min( ans , 1 + solve(Z) ) ;

     }

}

mp[Y] = ans ;

return ans ;

}

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

int t ;

cin >> t ;

int testcase = 0 ;

while(t--)
{
testcase ++ ;
cin >> d;

data X ;
int x ;
for(int i = 0 ; i < d ; i++)
{    cin >> x ;
     X.in.push_back(x);

}

sort(X.in.begin(),X.in.end() ) ;

cout<<"Case #"<<testcase<<": ";
cout<<solve(X)<<endl;



}

return 0 ;

}
