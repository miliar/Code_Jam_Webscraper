#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
        int t,i;
        scanf("%d",&t);
        for(i=1;i<=t;i++)
            {
             char s[101];
             scanf("%s",s);
             long long int counter=0;
             int n=strlen(s),m1=0,m2=0;
             int j=n-1,l=0;
             while(s[l]!='\0'){
                    if(s[l]=='+')
                    m1++;
                    if(s[l]=='-')
                        m2++;
                    l++;

             }
             if(m2==n)
             printf("Case #%d: 1\n",i);
             else if(m1==n)
             printf("Case #%d: 0\n",i);


             else {
                do{
                    while(s[j]!='-'){
                        j--;
                    }
                 if(j<0)
                    counter--;
                 if(s[0]!=s[j])
                    reverse(s,s+j+1);
                 else
                     {
                       for(int k=0;k<=j;k++){

                            if(s[k]=='+')
                                s[k]='-';
                            else s[k] = '+';
                        }
                      reverse(s,s+j+1);
                 }
                 counter++;
                }while(j>0);

              printf("Case #%d: %lld\n",i,counter);
           }
        }

return 0;
}
