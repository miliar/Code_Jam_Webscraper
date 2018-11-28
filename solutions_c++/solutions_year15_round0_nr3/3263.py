#include <bits/stdc++.h>
using namespace std;
#define I 2
#define J 3
#define K 4

int calc(int a,int b){
    int ans;
    int sign = (a>0)^(b>0)?-1:1;
    switch(abs(a)){
    case 1: ans=a*b;break;
    case I:
        switch(abs(b)){
            case 1: ans=a*b;break;
            case I: ans=-sign;break;
            case J: ans=sign*K;break;
            case K: ans=-sign*J;break;
        }
        break;
    case J:
        switch(abs(b)){
            case 1: ans=a*b;break;
            case I: ans=-sign*K;break;
            case J: ans=-sign;break;
            case K: ans=sign*I;break;
        }
        break;
    case K:
        switch(abs(b)){
            case 1: ans=a*b;break;
            case I: ans=sign*J;break;
            case J: ans=-sign*I;break;
            case K: ans=-sign;break;
        }
        break;
    }
    return ans;
}

char m[10000][10000]={0};
int main(){
#if 0
    string b[10]={"-K","-J","-I","-1","0","1","I","J","K"};
    string *s=&b[4];
    for(int i=1;i<5;i++){
    for(int j=1;j<5;j++){
        cout<<s[i]<<' '<<s[j]<<' '<<s[calc(i,j)]<<endl;
    }}
#endif
    int t;
    cin>>t;
    for(int z=0;z<t;z++){
        int l,k;
        char ss[10000];
        char s[10000];
        cin>>l>>k>>ss;
        for(int i=0;i<l;i++){
            s[i]=ss[i]-'i'+2;
            //cout<<(int)s[i]<<endl;
        }
        for(int i=0;i<l*k;i++){
            char pre;
            pre=m[i][0]=s[i%l];
            for(int j=i+1;j<l*k;j++){
                m[i][j-i]=calc(pre,s[j%l]);
                pre=m[i][j-i];
                //cout<<(int)pre<<endl;
            }
        }
        bool ans=false;
        for(int i=0;i<l*k-2;i++){
            if(m[0][i]==I){
                for(int j=i+1;j<l*k-1;j++){
                    if((m[i+1][j-i-1]==J)&&(m[j+1][l*k-1-j-1]==K)){
                        ans=true;
                        break;
                    }
                }
            }
            if(ans)break;
        }
        cout<<"Case #"<<z+1<<": "<<(ans?"YES":"NO")<<endl;
    }
    return 0;
}
/*
gets.to_i.times{|z|
  l,k=gets.split.map(&:to_i)
  s=gets.chomp.chars.map{|c|
    case c
    when ?i; I
    when ?j; J
    when ?k; K
    end
  }*k
  m=(0...l*k).map{|i|s[i+1...l*k].inject([s[i]]){|a,r|a+[calc(a[-1],r)]}}
  p "a"
  a=(0...l*k-2).any?{|i|m[0][i]==I&&(i+1...l*k-1).any?{|j|m[i+1][j-i-1]==J&&m[j+1][-1]==K}}
  puts "Case ##{z+1}: #{a ?"YES":"NO"}"
}
*/