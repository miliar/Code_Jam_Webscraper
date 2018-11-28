//__ hr1212 __//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mi;

#define si(a) scanf("%d",&a)
#define sii(a,b) scanf("%d %d",&a,&b)
#define siii(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define pi(a) printf("%d\n",a)
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define f(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b) for(i=a;i>=b;i--)
#define clr(x,a) memset(x,a,sizeof(x))
#define MAX 1000100
#define MOD 1000000007

int n,a[30];
map<char,int> m;

int main(){
    int r,k,i,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0,d;
    ll ans=0;string p;

    si(t);
    f(x,1,t+1){
        m.clear();
        si(n);
        f(i,0,n){
            si(a[i]);
            m[(i+'A')]=a[i];
        }
        printf("Case #%d: ",x);
        while(1){
            k=0;
            f(i,0,26){
                if(m[i+'A']!=0)
                    k=1;
            }
            if(!k){
                nl;
                break;
            }
            c=0;d=0;
            f(i,0,26){
                f(j,0,26){
                    c=0;
                    if(m[i+'A']>=1)
                        m[i+'A']-=1;
                    else
                        break;
                    if(m[j+'A']>=1)
                        m[j+'A']-=1;
                    else{
                        m[i+'A']+=1;
                        continue;
                    }
                    z=0;
                    for(map<char,int>::iterator it=m.begin();it!=m.end();it++){
                        z+=(it->second);
                    }
                    for(map<char,int>::iterator it=m.begin();it!=m.end();it++){
                        if((it->second)>z/2)
                            c=1;
                    }
                    if(!c){
                        cout<<(char)(i+'A')<<(char)(j+'A')<<" ";
                        d=1;
                        break;
                    }
                    else{
                        m[j+'A']+=1;
                        m[i+'A']+=1;
                    }
                }
                if(d)
                    break;
            }
            if(!d){

            f(i,0,26){
                    c=0;
                    if(m[i+'A']>=1)
                        m[i+'A']-=1;
                    else
                        continue;
                    z=0;
                    for(map<char,int>::iterator it=m.begin();it!=m.end();it++){
                        z+=(it->second);
                    }
                    for(map<char,int>::iterator it=m.begin();it!=m.end();it++){
                        if((it->second)>z/2)
                            c=1;
                    }
                    if(!c){
                        cout<<(char)(i+'A')<<" ";
                        d=1;
                        break;
                    }
                    else{
                        m[i+'A']+=1;
                    }
                }
            }

        }
    }

    return 0;
}
