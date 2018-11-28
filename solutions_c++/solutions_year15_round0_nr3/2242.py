#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

char res[200][200];
vector<long long> pos_i,pos_k;

char neg(char a)
{
     if(a=='a')
      return 'b';
     if(a=='b')
      return 'a';
     if(a>'k')
      a-=3;
     else
      a+=3;
     return a;
}

char mul(char a,char b)
{
     if(a=='a')
      return b;
     else if(b=='a')
      return a;
     if(res[a][b]==0)
      return neg(res[b][a]);
     return res[a][b];
}

char inv(char a)
{
     if(a=='a' || a=='b')
      return a;
     
     return mul(a,mul(a,a));
}
     
/*
a=1
b=-1
i=i
j=j
k=k
l=-i
m=-j
n=-k
*/
void set_res()
{
     memset(res,0,sizeof(res));
     res['b']['b']='a';
     res['b']['i']=res['i']['b']='l';
     res['b']['j']=res['j']['b']='m';
     res['b']['k']=res['k']['b']='n';
     res['b']['l']=res['l']['b']='i';
     res['b']['m']=res['m']['b']='j';
     res['b']['n']=res['n']['b']='k';
     res['i']['i']='b';
     res['i']['j']='k';
     res['i']['k']='m';
     res['i']['l']=res['l']['i']='a';
     res['i']['m']='n';
     res['i']['n']='j';
     res['j']['j']='b';
     res['j']['k']='i';
     res['j']['l']='k';
     res['j']['m']=res['m']['j']='a';
     res['j']['n']='l';
     res['k']['k']='b';
     res['k']['l']='m';
     res['k']['m']='i';
     res['k']['n']=res['n']['k']='a';
     res['l']['l']='b';
     res['l']['m']='k';
     res['l']['n']='m';
     res['m']['m']='b';
     res['m']['n']='i';
     res['n']['n']='b';
}
     
int main()
{
    int i,j,t;
    string s;
    ios::sync_with_stdio(false);
    freopen("C_in_large.txt","r",stdin);
    freopen("C_out_large.txt","w",stdout);
    set_res();
    
    cin>>t;
    int sv=t;
    
    while(t--)
    {
              long long l,x;
              cin>>l>>x;
              cin>>s;
              /*l=10002;
              x=1ll;
              s.clear();
              for(i=0;i<10002;i++)
               s+='i';
              */
              s=s+s+s+s;
              
              char tot='a';
              for(i=0;i<l;i++)
               tot=mul(tot,s[i]);
              
              char rem1;
              if(x%4==0)
               rem1=1;
              else if(x%4==1)
               rem1=tot;
              else if(x%4==2)
               rem1=mul(tot,tot);
              else
               rem1=inv(tot);
              
              //cout<<tot<<endl;
              
              char val1='a';
              bool ans=false;
              
              
              if(rem1=='b')
              {
                           pos_i.clear();
                           for(i=0;i<min(4ll,x)*l;i++)
                           {
                                           val1=mul(val1,s[i]);
                                           
                                           if(val1=='i')
                                            pos_i.push_back(i);
                           }
                           
                           val1='a';
                           pos_k.clear();
                           for(i=min(4ll,x)*l-1;i>=0;i--)
                           {
                                              val1=mul(s[i],val1);
                                              
                                              if(val1=='k')
                                               pos_k.push_back(min(4ll,x)*l-1-i);
                           }
                           
                           //reverse(pos_k.begin(),pos_k.end());
                           j=0;
                           for(i=0;i<int(pos_i.size());i++)
                           {
                                                           for(j;j<int(pos_k.size());j++)
                                                           {
                                                                                         if(pos_i[i]<x*l-pos_k[j]-2)
                                                                                         {
                                                                                                                ans=true;
                                                                                                                break;
                                                                                         }
                                                           }
                                                           if(ans)
                                                            break;
                           }
                                                        
              }
             
              if(ans)
               cout<<"Case #"<<sv-t<<": YES"<<endl;
              else
               cout<<"Case #"<<sv-t<<": NO"<<endl;
    }
              
    
    //system("pause");
    return 0;
}
