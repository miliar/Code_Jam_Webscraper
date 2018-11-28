#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
  //  boost1;boost2;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    lli t,k,ans;
    string str;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>str>>k;
        lli j=0;
        bool ch=0;
        ans=0;
        while(j<str.size()){
            if(str[j] != '-'){
               j++;
               continue;
            }
            if(j+k > str.size()){
                ch=1;
                break;
            }
            else{
              for(lli l=j;l<j+k;l++){
                 if(str[l] == '+'){
                    str[l] = '-';
                 }
                 else{
                    str[l] = '+';
                 }
              }
              ans+=1;
            }
        }

        if(ch == 1){
            cout << "Case #" << i<< ": IMPOSSIBLE"<<endl;
        }
        else{
            cout << "Case #" << i<< ": "<<ans<<endl;
        }
	}

	return 0;
}



