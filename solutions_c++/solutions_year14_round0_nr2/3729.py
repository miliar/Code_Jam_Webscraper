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
        int n=t;
        double C,F,X,time;

        while(t--){
            time=0;
            cin>>C>>F>>X;
            double a=X/2.0;
            double b=C/2.0+X/(F+2.0);
            int i=1;

            while(1){

               if(a==min(a,b)){
                  //ans=a;
                  break;
               }
               a=b;
               b=b-X/(i*F+2.0)+C/(i*F+2.0);
               i++;
               b=b+X/(i*F+2.0);

            }
            //cout<<a<<endl;
            cout<<"Case #"<<n-t<<": ";
            printf("%.7lf\n",a);
        }
        return 0;
    }
