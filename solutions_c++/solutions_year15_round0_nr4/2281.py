#include<bits/stdc++.h>
using namespace std;
int main()
{

int t , x , r , c ;
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
cin >> t ;
int test = 0 ;int ans ;
while(t--)
{
test ++ ;

cin >> x >> r >> c ;

if(x==1) ans = 1 ;
else if(x==4)
{
    if(r<c) swap(r,c);
    if(r==4&&c>2) ans = 1 ;
    else ans = 0 ;

}

else if(x==2)
{
    if(((r&1)&&(c&1))) ans = 0 ;
    else ans = 1 ;
}
else{
        if(r==1||c==1)ans = 0;
        else if(r%3==0||c%3==0)ans = 1 ;
        else ans = 0;

}






cout<<"Case #"<<test<<": ";

if(ans==0) cout<<"RICHARD\n";
else cout << "GABRIEL\n" ;

}


    return 0;

}
