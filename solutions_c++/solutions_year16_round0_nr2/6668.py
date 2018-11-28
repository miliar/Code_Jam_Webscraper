#include<bits/stdc++.h>
using namespace std;

int main(){
        long long int t,n,sum,i,j,k;
        string s1;
        cin>>t;k=1;
            while(k<=t){
            cin>>s1;
            if(s1.length()==1)
            {if(s1[0]=='+')
              cout<<"Case #"<<k<<": 0"<<endl;
              else
              cout<<"Case #"<<k<<": 1"<<endl;

            }
            else{
                n=s1.length();sum=0;
               while(1){
                   for(i=n-1;i>=0;i--){
                   if(s1[i]=='-')break;
                   }
                   j=i;

                  if(j<0){cout<<"Case #"<<k<<": "<<sum<<endl;break;}
                  sum++;
                  for(i=0;i<=j;i++)if(s1[i]=='+')s1[i]='-';else s1[i]='+';
              }

            }
              k++;
            }
return 0;
}


