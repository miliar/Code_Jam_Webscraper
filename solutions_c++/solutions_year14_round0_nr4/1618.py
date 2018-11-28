#include<fstream>
#include<algorithm>
#include<cstring>
using namespace std;
double s1[1000],s2[1000],s3[1000];
int n;
int main(){
    int t,i,j,k,ans,ans2;
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    in>>t;
    for(i=1;i<=t;i++){
        in>>n;
        for(j=0;j<n;j++)
            in>>s1[j];
        sort(s1,s1+n);
        for(j=0;j<n;j++)
            in>>s2[j];
        sort(s2,s2+n);
        memcpy(s3,s2,sizeof s2);
        ans=ans2=0;
        for(j=0;j<n;j++){
            for(k=0;k<n;k++){
                if(s1[j]>=s2[k]){
                    s2[k]=1;
                    ans++;
                    break;
                }
            }
        }
        for(j=0;j<n;j++){
            for(k=0;k<n;k++){
                if(s1[j]<s3[k]){
                    s3[k]=0;
                    ans2++;
                    break;
                }
            }
        }
        out<<"Case #"<<i<<": "<<ans<<" "<<(n-ans2)<<"\n";
    }
    return 0;
}
