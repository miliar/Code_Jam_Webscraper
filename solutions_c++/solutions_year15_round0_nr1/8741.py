#include <bits/stdc++.h>

using namespace std;

int main()
{

FILE *fp1 , *fp2;
   //fp1 = freopen("A-small-attempt0.in", "r", stdin);
   //fp2=freopen("output-small.txt" , "w" , stdout);

   fp1 = freopen("A-large.in", "r", stdin);
   fp2=freopen("output-large.txt" , "w" , stdout);

    int t , S , sum , ans;
    string st;
    cin>>t;

    for(int T=1 ; T<=t ; T++){
       cin>>S>>st;

       sum=0;
       ans=0;
       for(int i=0 ; i<st.length() ; i++){
           if(sum >=i){
             sum+=((int)st[i])-48;
           }else{
              ans+=(i-sum);
              sum=i+(((int)st[i])-48);
           }
       }
       cout<<"Case #"<<T<<": "<<ans<<endl;
    }

   fclose(fp1);
   fclose(fp2);

    return 0;
}
