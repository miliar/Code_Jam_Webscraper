/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;
#include "../bidhan.h"

#define inf (1<<28)
#define eps 1e-9

#define mx 10010

bool used[mx];

int main(){
    read("in.txt");
    rite("out.txt");
    ios_base::sync_with_stdio(0);
    int TEST;
    cin>>TEST;
    while( TEST-- ){
        int n,x;
        cin>>n>>x;
        vi vec;
        si ase;
        rep(i,n){
            int temp;
            cin>>temp;
            vec.pb(temp);
            ase.ins(i);
        }
        sort(all(vec),greater<int>());
        int cnt=0;
        mem(used,0);
        COUT_TEST;
        rep(i,sz(vec)){
            if(used[i]) continue;
            //cout<<vec[i]<<endl;
            si :: iterator it=ase.upper_bound(i);
            while(it!=ase.end()) {
                //cout<<"--"<<vec[*it]<<endl;
                if(vec[*it]+vec[i]>x){
                    it++;
                    continue;
                }
                used[*it]=true;
                ase.erase(it);
                break;
            }
            cnt++;

        }
        cout<<cnt<<endl;
        //return 0;
    }
    PRINT_TIME;
    return 0;
}
