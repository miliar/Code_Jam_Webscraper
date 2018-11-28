#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<string.h>

#define ll long long int
using namespace std;

ll a[2000],arr[2000];

int ispalin(){
    int ct = 0,x,y;
    char st[20];
    for(ll i=1;i<1999;i++){
        sprintf(st,"%lld",a[i]);
        x = strlen(st);
        if(x == 1){
            arr[ct] = a[i];
            ct++;
        }
        else if(!(x%2)){
            y = 1;
            for(ll j=0;j<x/2;j++){
                if(st[j] != st[x-j-1]){
                    y = 0;
                    break;
                }
            }
            if(y == 1){
                arr[ct] = a[i];
                ct++;
            }
        }
        else{
            y = 1;
            for(ll j=0;j<x/2;j++){
                if(st[j] != st[x-j-1]){
                    y = 0;
                    break;
                }
            }
            if(y == 1){
                arr[ct] = a[i];
                ct++;
            }
        }
        
    }
    return ct;
}
int palin(){
    ll k,l,t,r,h;
    int ct =0;
    for(ll i=1;i<=9;i++){
        a[i] = i*i;
    }
    ct = 10;
    for(ll i=2;i<=6;i++){
        if(i%2 == 0){
              h = i/2;
              k = pow(10,h-1);
              l = pow(10,h);
              for(ll j=k;j<l;j++){
                  t = j;
                  r = j;
                  while(t!=0){
                      h = t%10;
                      r = r*10+h;
                      t = t/10;
                  }
                  a[ct] = r*r;
                  ct++;
              }
        }
        else{
            h = (i-1)/2;
            k = pow(10,h-1);
            l = pow(10,h);
            for(ll j=k;j<l;j++){
                for(ll lp=0;lp<10;lp++){
                     t = j;
                     r = j;
                     r = r*10+lp;
                  while(t!=0){
                      h = t%10;
                      r = r*10+h;
                      t = t/10;
                  }
                  a[ct] = r*r;
                  ct++;
                }
            }
        }
    }
    return ct;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
	freopen("out_c.txt","w",stdout);
	
	int t,A,B,p_ct,count=0;
    p_ct = palin();
    ll x,y;
    p_ct = ispalin();
    cin>>t;
    
	for(int i=1;i<=t;i++){
        count = 0;
        cin>>x>>y;
        for(int j=0;j<p_ct;j++){
            if(arr[j]>=x && arr[j]<=y)
            	count++;
        } 
        printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
