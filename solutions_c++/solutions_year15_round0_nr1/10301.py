#include <bits/stdc++.h>
using namespace std;
int cases,caseno=1,n;
int a[10000];
char s[10000];

int main()
{
    //freopen ("input.in","r",stdin);
    //freopen ("output.out","w",stdout);
    cin>>cases;
    //cout<<"cases:"<<cases<<endl;
    while(cases--){
        int ans=0;
        cin>>n;
        getchar();
        cin>>s;
        //cout<<"string:"<<s<<endl;
        a[0]=s[0]-'0';
        for(int i=1;i<=n;i++){
            a[i]=a[i-1]+s[i]-'0';
            if(a[i-1]<i){
                ans+=i-a[i-1];
                //cout<<"for"<<i<<" "<<i-a[i-1]<<endl;
                a[i]+=i-a[i-1];
            }
        }
        cout<<"Case #"<<caseno++<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
