#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <stdio.h>

using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

string pol(string ch,string s){
 int n=ch.size();
 int i=0;
 bool isGreater = false;
            for(int j = n - 1; i < n / 2; i++, j--){
                    ch[j] = ch[i];
            }
            for(int j = n/2; j < n ;j++){
                if(s[j] < ch[j]){
                    isGreater = true;
                    break;
                }else if(s[j] > ch[j]){
                    break;
                }
            }

            if(isGreater == false){
                if(n % 2 == 0) {
                    int k = 0;
                    while(k < n / 2){
                        ch[i + k]++;
                        ch[i - k - 1]++;
                        if(ch[i + k] <= '9') break;
                        else    {ch[i - k - 1] = ch[i + k] = '0';}
                        k++;
                    }
                }else{
                    int k = 0;
                    while(k <= n / 2){
                        if(k == 0)    ch[i]++;
                        else{ch[i - k]++; ch[i + k]++;}
                        if(ch[i - k] <= '9') break;
                        else    {ch[i - k] = ch[i + k] = '0';}
                        k++;
                    }
                }
            }


            if(ch[0] == '0'){
                ch[0] = '1';
                s = ch + '1';
            }else{
                s = ch;
            }
            return s;
       }

 bool cha(string s){
   int i,j;
   for(j=s.size()-1,i=0;i<s.size()/2;j--,i++){
    if(s[i]!=s[j])return 0;
                             }
      return 1;
      }

string mup(string s1,string s2){
   int x=0,mm=0,temp=0,i=0,j=0,k=0,T=0,n1=0,g=0,n2=0;

 mm=0;
 temp=0;
 int v[100000]={0};
for(i=s1.size()-1,k=0;i>=0;k++,i--){
                 n1=(int)(s1[i])-48;
                 mm=k;
                 for(j=s2.size()-1;j>=0;j--,k++){
                  n2=(int)(s2[j])-48;
                   x=n1*n2+temp;
                    v[k]=x%10+v[k];
                    temp=x/10;
                    temp+=v[k]/10;
                      v[k]=v[k]%10;
                    }
                     while(temp){
                     v[k]=temp%10;
                     temp/=10;
                     k++;

                                 }
                     g=k-1;
                     k=mm;
                                          }



s1="";
for(i=g;i>=0;i--)
s1+=(char)(v[i]|'0');
if(cha(s1))return s1;
 return "";

       }



  int main(){
      READ("input_codejame.txt") ;
      WRITE("output_codejame.txt") ;

   int t,i,j;
   long long num1;
   vector<long long>a;
   stringstream ss ;
   string s="0",SS;
  // while(cin>>SS){cout<<SS<<"\n";cout<<mup(SS,SS)<<"\n";}

   for(i=0;i<=12200;i++){
   s=pol(s,s);
   SS=mup(s,s);
   if(SS.size()!=0){
    ss<<SS ; ss >> num1 ; ss.clear() ;
    a.push_back(num1);
   }
    }

//cout<<a[a.size()-1]<<endl;

int Q , W , E , nt = 0;
long long A , B;


cin>>Q;
while(Q--){
    cin>>A>>B;
    W = lower_bound(a.begin() ,a.begin()+a.size() , A)-a.begin() ;
    E = upper_bound(a.begin() ,a.begin()+a.size() , B)-a.begin() ;
    cout<<"Case #"<<++nt<<": "<<E-W<<endl;
}



}
