#include<bits/stdc++.h>
using namespace std;





int main(){

int t,sm;
string s;

cin>>t;
int x=1;
while(t--){
            cin>>sm;
            cin>>s;
            int a[sm+1]={0};
            int audi=0,ans=0;

            for(int i=0;i<s.length();i++)
            {a[i]+=(int)(s[i]-48);}

            for(int i=1;i<s.length();i++)
            {audi+=a[i-1];
            if(i>audi)
            {ans+=i - audi;
            audi+=i-audi;}
            }

            cout<<"Case #"<<x<<": "<<ans<<endl;
            x++;
            }


}















