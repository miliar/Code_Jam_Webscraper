#include <vector>
#include <iostream>

#define enableFastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int

using namespace std;

int main(){
enableFastIO;
li t,n,tmp;
cin >> t;
inc(i,1,t)  {
    cin >> n;
    bool seen =false;
    int ans = 0;
    if (n >0){
        vector<bool> found(10,false);
        inc(j,1,100){
            tmp = j*n;
            while (tmp>0){
                found[tmp%10]=true;
                tmp/=10;
            }
            seen = true;
            for (bool b:found)
                seen = seen && b;
            if (seen){
                ans = j;
                break;
            }
        }
    }
    if (n>0 && seen)
        cout << "Case #" << i << ": " << ans*n << endl;
    else
        cout << "Case #" << i << ": INSOMNIA" << endl;
    }
}
