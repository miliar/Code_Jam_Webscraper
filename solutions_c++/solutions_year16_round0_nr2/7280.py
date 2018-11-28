/*#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;

    while(t--){
    	//yout code here


    }

    return 0;
}*/

#include <bits/stdc++.h>
#include <fstream>
using namespace std;
typedef long long int LL;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ifstream myfile;
    ofstream destfile;
    myfile.open ("B-large.in");
    destfile.open ("output.in");

    long long int t;
    myfile>>t;

   for(int i=1;i<=t;i++){
        string s;
        myfile>>s;
        LL len = s.length();
        LL ans=0;
        //cout<<s;
        if(s[0]=='-'){
            for(int i=0;i<len-1;i++){
                if(s[i]=='+' && s[i+1]=='-'){
                    ans+=2;
                }
            }
            ans++;
        }
        else{
            for(int i=0;i<len-1;i++){
                if(s[i]=='+' && s[i+1]=='-'){
                    ans+=2;
                }
            }
        }
        destfile<<"Case #"<<i<<": "<<ans<<"\n";
    }

    myfile.close();
    destfile.close();
    return 0;
}