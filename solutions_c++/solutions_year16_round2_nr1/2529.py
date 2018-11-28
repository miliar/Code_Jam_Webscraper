#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#define s(a) scanf("%d",&a);
#define s2(a,b) scanf("%d %d",&a,&b);
#define sc(a) cin >> a;
#define sp(b) cout << b << "\n";
#define p(a) printf("%d\n",a);
#define p2(a,b) printf("%d %d",a,b);
#define pm(a) printf("a\n");
#define test(t) while(t>0)
#define sl(a) a.length();
#define f(a,b,c) for(a=b;a<c;a++)
#define v(a,b) vector<a> b;
#define pb(a,b) a.push_back(b);
#define ll long long
#define max(a,b) (abs(a)>abs(b) ? abs(a):abs(b))
#define min(a,b) (abs(a)<abs(b) ? abs(a):abs(b))
#define diff(a,b) abs(a-b);
using namespace std;

using namespace std;
int main(){
	int t,n,i,j,x,l;
    string s;
    ll answer;
	s(x);
    t=x;
	test(t){
        
        cin >> s;
        l=sl(s);
        int another[10]={0};
        int array[27]={0};
        f(i,0,l){
            array[s[i]-'A']++;
        }
        if(array['Z'-'A']>0){
            another[0]=array['Z'-'A'];
            array['E'-'A'] -=array['Z'-'A'];
            array['R'-'A'] -=array['Z'-'A'];
            array['O'-'A'] -=array['Z'-'A'];
            array['Z'-'A']=0;

        }
          if(array['U'-'A']>0){
            another[4]=array['U'-'A'];
            array['F'-'A'] -=array['U'-'A'];
            array['O'-'A'] -=array['U'-'A'];
            array['R'-'A'] -=array['U'-'A'];
            array['U'-'A']=0;
            

        } 
         if(array['W'-'A']>0){
            another[2]=array['W'-'A'];
            array['T'-'A'] -=array['W'-'A'];
            array['O'-'A'] -=array['W'-'A'];
            array['W'-'A']=0;
            

        }  
        if(array['O'-'A']>0){
            another[1]=array['O'-'A'];
            array['N'-'A'] -=array['O'-'A'];
            array['E'-'A'] -=array['O'-'A'];
            

        } 
        if(array['R'-'A']>0){
            another[3]=array['R'-'A'];
            array['T'-'A'] -=array['R'-'A'];
            array['H'-'A'] -=array['R'-'A'];
            array['E'-'A'] -=(2*array['R'-'A']);
            

        }        
        if(array['X'-'A']>0){
            another[6]=array['X'-'A'];
            array['S'-'A'] -=array['X'-'A'];
            array['I'-'A'] -=array['X'-'A'];
            array['X'-'A']=0;

        } 
        if(array['F'-'A']>0){
            another[5]=array['F'-'A'];
            array['I'-'A'] -=array['F'-'A'];
            array['V'-'A'] -=array['F'-'A'];
            array['E'-'A'] -=array['F'-'A'];
            

        } 
        if(array['S'-'A']>0){
            another[7]=array['S'-'A'];
            array['E'-'A'] -=array['S'-'A'];
            array['V'-'A'] -=array['S'-'A'];
            array['E'-'A'] -=array['S'-'A'];
            array['N'-'A'] -=array['S'-'A'];
            

        }
        if(array['G'-'A']>0){
            another[8]=array['G'-'A'];
            array['I'-'A'] -=array['G'-'A'];
            array['H'-'A'] -=array['G'-'A'];
            array['T'-'A'] -=array['G'-'A'];
            array['E'-'A'] -=array['G'-'A'];
            

        }
         if(array['I'-'A']>0){
            another[9]=array['I'-'A'];
            array['N'-'A'] -=array['I'-'A'];
            array['E'-'A'] -=array['I'-'A'];
            array['N'-'A'] -=array['I'-'A'];
           
            

        }

              


        printf("Case #%d: ",x-t+1);
        f(i,0,10){
            if(another[i]>0){
                f(j,0,another[i]){
                    printf("%d",i);
                }
            }
        }
        printf("\n");
     
        t--;  
        }
        
    
}
