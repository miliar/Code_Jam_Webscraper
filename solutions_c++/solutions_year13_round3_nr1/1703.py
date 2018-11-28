#include<iostream>
using namespace std; 
int main(){
    FILE *fp = fopen("AA.txt","w");
    int tc,cs=1,ans,n,c;
    string s;
    scanf("%d",&tc);
    while(tc--){
        ans=0;
        cin>>s;
        scanf("%d",&n);
        for(int i=0;i<s.length();i++)
            for(int j=i+n;j<=s.length();j++){
                c=0;
                for(int k=i;k<j;k++){
                    if(s[k]=='a' || s[k]=='e' || s[k]=='i'|| s[k]=='o' || s[k]=='u')
                        c=0;
                    else
                        c++;
                    if(c>=n){
                        ans++;
                        break;
                    }
                }
            }
 
        fprintf(fp,"Case #%d: %d\n",cs++,ans);
    }
    fclose(fp);
}
