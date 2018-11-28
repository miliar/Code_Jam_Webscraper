#include<bits/stdc++.h>
using namespace std;

int main()
{
        long long int a,b,total,i,j,k;           
        string c;
        cin>>a;
        k=1;
            while(k<a+1){
            cin>>c;
            if(c.length()==1)
            {if(c[0]=='+')
              cout<<"Case #"<<k<<": 0"<<endl;
              else
              cout<<"Case #"<<k<<": 1"<<endl;

            }
            else{
               b=c.length();
               total=0;
               while(1){
                   for(i=b-1;i>=0;i--){
                   if(c[i]=='-')break;
                   }
                   j=i;

                  if(j<0){cout<<"Case #"<<k<<": "<<total<<endl;break;}
                  total++;
                  for(i=0;i<=j;i++)if(c[i]=='+')c[i]='-';else c[i]='+';
              }

            }
              k++;
            }
return 0;
}

