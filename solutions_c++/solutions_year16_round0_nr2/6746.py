#include <iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{int e=0;
freopen("a1.in","r",stdin);
freopen("a1.out","w",stdout);
    int t,m;
    cin>>t;
    for(int i=0;i<t;i++){
    m=0;
        string s,s1;

        cin>>s;
        cout<<"Case #"<<i+1<<": ";
        int len=s.length();
        back:e=0;
        for(int h=0;h<=len-1;h++){
            if(s.at(h)=='+'){

            }
            else{
            e=1;
            }
        }

if(len>1&&e==1){
  int r=0;

            for(int h=len-1;h>=0;h--)
{
               if(s.at(h)=='+'){
              len=len-1;
              }
              else{
              break;}
}r=0;
            for(int h=0;h<len-1;h++){
              if(s.at(h)=='+'){
              r++;
              }
              else{
              break;
              }
            }
            if(r>1){
            for(int h=0;h<r;h++){
                s1=s1+'-';
                }
  s.replace(s.begin(),s.begin()+r,s1);
  s1="";
  m++;
            }

         if(s.at(len-1)=='-'&&s.at(0)=='-'){
            for(int j=len-1;j>=0;j--){
                if(s.at(j)=='-'){
                        s1=s1+"+";

                }
                else if(s.at(j)=='+'){
                    s1=s1+"-";
                }
            }   m++;
               s.replace(s.begin(),s.begin()+len,s1);
               s1="";


                  for(int f=0;f<len-1;f++){
                    if(s.at(f)!='+'){
                    goto back;
                    }
    }
        }
        else if(s.at(len-1)=='-'&&s.at(0)=='+'&&len!=2){
            for(int j=len-1;j>=0;j--){

                if(s.at(j)=='+')
                {
                for(int l=j;l>=0;l--){
                if(s.at(l)=='-'){
                        s1=s1+"+";
                }
                else if(s.at(l)=='+'){
                    s1=s1+"-";
                }
            }
                s.replace(s.begin(),s.begin()+j+1,s1);
               s1="";         m++;    break;
                }

                    } for(int f=0;f<len-1;f++){
                    if(s.at(f)!='+'){
                            goto back;
                        }
            }
        }


        else if(s.at(0)=='+'&&s.at(1)=='-'){
                s1=s1+'+'+'+';
                 s.replace(s.begin(),s.begin()+2,s1);
                    m=m+2;
            }}
            else if(s.at(0)=='-'){m++;}
        cout<<m<<endl;
        }
    return 0;
}


