using namespace std;
#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>

 
int main(){
    int tc,cs=1,ans,n,c;
    string s;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tc);
    while(tc--){
        ans=0;
        cin>>s;
        scanf("%d",&n);
        for(int i=0;i<s.length();i++)
            for(int j=i+n;j<=s.length();j++){
                c=0;
                for(int k=i;k<j;k++){
                    //cout<<s[k]<<" ";
                    if(s[k]=='a' || s[k]=='e' || s[k]=='i'|| s[k]=='o' || s[k]=='u')
                        c=0;
                    else
                        c++;
                    if(c>=n){
                        ans++;
                        break;
                    }
                }
                //cout<<endl;
            }
 
        printf("Case #%d: %d\n",cs++,ans);
    }
}
