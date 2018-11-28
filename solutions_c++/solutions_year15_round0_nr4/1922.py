#include <bits/stdc++.h>
using namespace std;
/*for x<=5
if(x!=6&&x>(max(r,c))||min(r,c)<x-1){
print richard
if (r*c divisible by x
print doosra banda
except richard
ye for x<=5
for x>=7 , priint richard always
*/
int main()
{
    int test,x,r,c;
    cin>>test;
    for (int i = 0; i < t; i++) {
        cin>>x>>r>>c;
        if(min(r,c)<x-1){
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
        else if((r*c)%x==0){
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
    }

return 0;
}
