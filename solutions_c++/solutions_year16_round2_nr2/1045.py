#include<bits/stdc++.h>
using namespace std;

string s1,s2;
vector<int>pos;
string t1,t2;
int diff;
int res1,res2;
int L;

int eval(string x)
{
      int ret=0;
      for(int i=0; i<x.size(); i++){
           ret*=10;
           ret+=(x[i]-'0');
      }
      return ret;
}

void recur(int x)
{
     if(x==pos.size()){
           //cout<<t1<<" "<<t2<<endl;
           int v1 = eval(t1);
           int v2 = eval(t2);
           int d = abs(v1-v2);
           if(d<diff || (d==diff && v1<res1) || (d==diff && v1==res1 && v2<res2)){
                 diff = d;
                 res1=v1;
                 res2=v2;
           }
           return;
     }

     for(int i=0; i<=9; i++){
          if(pos[x]<L)
             t1[pos[x]]=(char)(i+'0');
          else
             t2[pos[x]-L]=(char)(i+'0');
          recur(x+1);
     }
}

void print(int x)
{
     string str = "";
     while(x>0){
         str += (char)((x%10)+'0');
         x/=10;
     }
     while(str.size()<L){
         str+='0';
     }
     for(int i=L-1; i>=0; i--)
         printf("%c",str[i]);
}
int main()
{
      int T,i,j,it;
      freopen("B-small-attempt2.in","r",stdin);
      freopen("01.out","w",stdout);
      scanf("%d",&T);

      for(it=1; it<=T; it++)
      {
            cin>>s1>>s2;
            L = s1.size();

            pos.clear();
            for(i=0; i<L; i++)
                if(s1[i]=='?')
                    pos.push_back(i);
            for(i=0; i<L; i++)
                if(s2[i]=='?')
                    pos.push_back(i+L);
            t1 = s1;
            t2 = s2;
            diff = 100000;
            res1=res2=0;
            recur(0);
            printf("Case #%d: ",it);
            print(res1);
            printf(" ");
            print(res2);
            puts("");
      }
       return 0;
}
