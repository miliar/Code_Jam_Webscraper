#include <bits/stdc++.h>
#define mp make_pair
using namespace std;
int t,l,x,f=1,c=1,f1=1;
char cur,p;
string sub,s,ans;
map <pair<char,char> , char> m;
void assign(){
	m[mp('1','1')]='1';
	m[mp('1','i')]='i';
	m[mp('1','j')]='j';
	m[mp('1','k')]='k';
	m[mp('i','1')]='i';
	m[mp('i','i')]='2';
	m[mp('i','j')]='k';
	m[mp('i','k')]='J';
	m[mp('j','1')]='j';
	m[mp('j','i')]='K';
	m[mp('j','j')]='2';
    m[mp('j','k')]='i';
    m[mp('k','1')]='k';
    m[mp('k','i')]='j';
    m[mp('k','j')]='I';
    m[mp('k','k')]='2';
    m[mp('1','2')]='2';
    m[mp('2','1')]='2';
    m[mp('1','I')]='I';
    m[mp('I','1')]='I';
    m[mp('1','J')]='J';
    m[mp('J','1')]='J';
    m[mp('1','K')]='K';
    m[mp('K','1')]='K';
    m[mp('i','2')]='I';
    m[mp('2','i')]='I';
    m[mp('i','I')]='1';
    m[mp('I','i')]='1';
    m[mp('i','J')]='K';
    m[mp('J','i')]='k';
    m[mp('i','K')]='j';
    m[mp('K','i')]='J';
    m[mp('j','2')]='J';
    m[mp('2','j')]='J';
    m[mp('j','I')]='k';
    m[mp('I','j')]='K';
    m[mp('j','J')]='1';
    m[mp('J','j')]='1';
    m[mp('j','K')]='I';
    m[mp('K','j')]='i';
    m[mp('k','2')]='K';
    m[mp('2','k')]='K';
    m[mp('k','I')]='J';
    m[mp('I','k')]='j';
    m[mp('k','J')]='i';
    m[mp('J','k')]='I';
    m[mp('k','K')]='1';
    m[mp('K','k')]='1';
    m[mp('2','2')]='1';
    m[mp('2','I')]='i';
    m[mp('2','J')]='j';
    m[mp('2','K')]='k';
    m[mp('I','2')]='i';
    m[mp('I','I')]='2';
    m[mp('I','J')]='k';
    m[mp('I','K')]='J';
    m[mp('J','2')]='j';
    m[mp('J','I')]='K';
    m[mp('J','J')]='2';
    m[mp('J','K')]='i';
    m[mp('K','2')]='k';
    m[mp('K','I')]='j';
    m[mp('K','J')]='I';
    m[mp('K','K')]='2';


}
int main(){
    freopen("input1.in","r",stdin);
    freopen("output2.txt","w",stdout);
	assign();
     cin>>t;
     while(t--){s="";ans="ijk";f=1;f1=0;
     	cin>>l>>x;
         cin>>sub;
         while(x--){
         	s+=sub;
         }
        cur='1';
        for(int i=0;i<s.size();i++){//cout<<cur<<" ";
          cur=m[mp(cur,s[i])];
          if(ans[f1]==cur){
            if(f1==2){
            	if(i==s.size()-1)f1++;
            }
            else {f1++;cur='1';}
             }
          }

        if(f1==3){cout<<"Case #"<<c<<": "<<"YES\n";c++;}
        else {cout<<"Case #"<<c<<": "<<"NO\n";c++;}
        //cout<<" "<<l<<" "<<x<<" "<<s.size()<<" "<<sub<<'\n';
     }

	return 0;
}
