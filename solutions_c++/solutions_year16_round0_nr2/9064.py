#include <bits/stdc++.h>

using namespace std;
bool IsHappy(string s){

 for(long long k=0;k<s.size();k++){
    if(s[k]!='+')
        return false;
 }
 return true;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    long long n;
    cin>>n;

    for(long long i=0;i<n;i++){
        string s;
        cin>>s;
        long long counter=0;
        //long long i=0;
        long long m;
        while(!IsHappy(s)){

            for( m=1;m<s.size();m++){
                if(s[m]!=s[m-1])break;
            }
          for(long long a=0;a<m;a++){
            s[a]=s[m];
          }
          if(m==s.size()){
            for(long long a=0;a<m;a++){
            s[a]='+';
          }
         // counter++;
          }
          counter++;
        }
        cout<<"Case #"<<i+1<<": "<<counter;
        if(i!=n-1)cout<<endl;
    }

     return 0;
    }
