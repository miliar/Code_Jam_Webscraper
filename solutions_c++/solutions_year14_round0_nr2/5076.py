#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<iomanip>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<sstream>
#include<set>
#include<cstdio>
using namespace std;

typedef double D;
D c,f,x;

int main(){
    int t;
    //freopen("B-large.in","r",stdin);
    cin>>t;
    //freopen("A-small-attempt0.out","w",stdout);
    for(int ca=1;ca<=t;ca++){
        cin>>c>>f>>x;D p=2.0;
        D ans=x/2.0,pre=0;
        while(ans>c/p+x/(p+f)+pre){
            pre+=c/p;
            ans=pre+x/(p+f);p+=f;
        }
        printf("Case #%d: ",ca);
        printf("%.7lf\n",ans);
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
