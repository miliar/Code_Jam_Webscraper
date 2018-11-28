#include<fstream>

using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("a.out");

int main(){
    int n;
    cin>>n;
    char s[1500];
    for(int cas=1;cas<=n;cas++){
        int m;
        cout<<"Case #"<<cas<<": ";
        cin>>m>>s;
        int sum=s[0]-'0',ans=0;
        for(int i=1;i<=m;i++){
            if(sum<i){
                ans+=i-sum;
                sum+=i-sum;
            }
            sum+=s[i]-'0';
        }
        cout<<ans<<endl;
    }
    return 0;
}
