#include <bits/stdc++.h>

using namespace std;

int main(){freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int index=1;
    while(t--){
        int n,q;
        cin >> n >> q;
        cout << "Case #" << index << ":" << endl;
        for(int i=0;i<(1<<n);++i){
            if((i&(1<<0))==0){
                continue;
            }
            if((i &(1<<(n-1)))==0){
                continue;
            }
            int flag=0;
            long long int ans=0;
            string s="";
            vector<long long int> V;
             for(int k=0;k<n;++k){
                    if(i & (1<<k)){

                        s+="1";
                        }
                    else
                        s+="0";

                }
                reverse(s.begin(),s.end());
            for(long long int j=2;j<=10;++j){long long int f=1;
            ans=0;
                for(int k=0;k<n;++k){
                    if(i & (1<<k)){
                        ans+=f;

                        }


                    f=f*j;
                   // cout << f << " ";
                }
              //  cout << ans << endl;

             //   cout << ans << endl;
                for(long long int k=2;k<=sqrt(ans);++k){
                    if(ans%k==0 && (ans/k)!=1){
                       V.push_back(k);
                       break;
                    }
                }
            }
            if(V.size()==9){
                --q;
                cout << s << " ";
                for(int i=0;i<9;++i)
                    cout << V[i] << " ";
                cout << endl;
            }
            if(q==0){
                break;
            }


        }




    }
    return 0;
}
