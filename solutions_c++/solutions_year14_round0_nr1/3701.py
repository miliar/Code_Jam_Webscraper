    #include<iostream>
    #include<cmath>
    #include<algorithm>
    #include<climits>
    #include<vector>
    #include<queue>
    #include<stack>
    #include<sstream>
    #include<bitset>
    #include<set>
    #include<deque>
    #include<cstdlib>
    #include<cstdio>
    #include<cstring>
    #include<string.h>
    #include<ctime>
    #include<map>
    #include<assert.h>
    using namespace std;
    typedef long long ll;
    typedef unsigned long long ULL;
    typedef long double LD;

    int main(){

        int t,r1,r2;
      // freopen("A-small-attempt0.txt","r",stdin);
       //freopen("out.txt","w",stdout);
        cin>>t;

        int a[4][4],b[4][4];
        int n=t;

        while(t--){

            cin>>r1;
            r1--;

            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    cin>>a[i][j];

            cin>>r2;
            r2--;


            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    cin>>b[i][j];

           int cnt=0,val;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(a[r1][i]==b[r2][j]){
                        cnt++;val=a[r1][i];
                    }
                }
            }
            if(cnt==0){
                cout<<"Case #"<<n-t<<": Volunteer cheated!"<<endl;
            }
            else if(cnt==1){
                cout<<"Case #"<<n-t<<": "<<val<<endl;
            }
            else{
                cout<<"Case #"<<n-t<<": Bad magician!"<<endl;
            }
        }
        return 0;
    }
