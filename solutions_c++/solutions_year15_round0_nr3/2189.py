#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<map>
#include<cmath>
using namespace std;
const int N = 10000+10;
int presum[4][N];
int lassum[4][N];
map<char,int> mm;
char s[N];
int get(int a,int b)
{
    int fl = 1;
    if(a*b<0) fl=-1;
    if(a<0) a= -a;
    if(b<0) b= -b;
    if(a==1) return fl*b;
    if(b==1) return fl*a;
    if(a==2){
        if(b==2) return fl*(-1);
        if(b==3) return fl*(4);
        if(b==4) return fl*(-3);
    }
    if(a==3){
        if(b==2) return fl*(-4);
        if(b==3) return fl*(-1);
        if(b==4) return fl*(2);
    }
    if(a==4){
        if(b==2) return fl*(3);
        if(b==3) return fl*(-2);
        if(b==4) return fl*(-1);
    }
}
int main()
{
    //cout<<" oooo "<<get(1,2);
    freopen("C-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);
    mm.clear();
    mm['i']=2;mm['j']=3;mm['k']=4;mm['1']=1;
    int t,l,x,cas=0;
    cin>>t;
    while(t--){
        cin>>l>>x;
        scanf("%s",s+1);
        int len = strlen(s+1);
        for(int i=2;i<=x;i++){
            for(int j=1;j<=len;j++)
            s[(i-1)*len+j] = s[j];
        }
        len = len * x;
        int fl=10000, fll=-1;
        int ans = 1;
        for(int i=1;i<=len;i++){
            ans = get(ans,mm[s[i]]);
        }
        //cout<<"ans = "<<ans<<endl;
        printf("Case #%d: ",++cas);
        if(ans!=-1) {puts("NO");continue;}
        ans = 1;
        for(int i=1;i<=len;i++){
            ans = get(ans,mm[s[i]]);
            if(ans==2) {fl=i;break;}
        }
        ans = 1;
        for(int i=len;i>=1;i--){
            ans = get(mm[s[i]],ans);
            if(ans==4) {fll=i;break;}
        }
        //printf("hsh %d %d\n",fl,fll);
        if(fll > fl+1) puts("YES");
        else puts("NO");
    }
    return 0;
}
