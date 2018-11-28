#include <bits/stdc++.h>
#define LL long long int
#define mod 1000000007
using namespace std;
int t,p=1,c=0;
string s;

int main(){
    std::ios_base::sync_with_stdio(false);
    ofstream outputFile("out.txt");
    cin>>t;
    while(t--){
        cin>>s;
        c=0;

        for(int i=s.length()-1;i>=0;i--){

            if(s[i]=='-'){
                for(int j=i;j>=0;j--){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            c++;
            }

        }


        cout<<"Case #"<<p<<": "<<c<<endl;
        outputFile<<"Case #"<<p<<": "<<c<<endl;
        p++;
    }

return 0;
}
