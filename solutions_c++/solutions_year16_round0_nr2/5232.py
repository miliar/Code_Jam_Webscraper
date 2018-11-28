#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define fs first
#define sc second
typedef long long ll;
string rever(string  s , int j){
    int k = j;
    for(int i = 0 ;i<=j ;i++,j--)
        swap(s[i],s[j]);
    for(int i = 0 ;i<=k;i++){
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
        }
    return s;
}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    freopen ("file.out","w",stdout);
    freopen ("file.in","r",stdin);
    int t ;
    cin>>t;
    string s;
    for(int p = 1 ;p<=t;p++){
        cin>>s;
        int res = 0;
        for(int i = s.size()-1;i>=0;i--){
            if(s[i]=='-'){
                int ind = -1;
                for(int j = 0 ; j<i;j++,ind++)
                    if(s[j]=='-')
                        break;
                if(ind==-1)
                   s =rever(s,i);
                else{
                    s =rever(s,ind);
                    s =rever(s,i);
                    res++;

                }
                res++;
            }


        }
        cout<<"Case #"<<p<<": "<<res<<'\n';
    }




    return 0;

}


