#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <stack>
#include <queue>
#include <set>
#include<utility>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a>b?b:a
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define GCD(a,b)  { return (b==0)?a:GCD(b,a%b); }
#define LCM(a,b)  { return a*b/GCD(a,b);  }
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR_X(i,n,x) for(i=x;i<n;i++)
#define FORN(i,n) for(i=n;i>=0;i--)
#define FORN_X(i,n,x) for(i=n;i>=x;i--)

typedef long long int ll;
using namespace std;

int main(){
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
        int x,r,c;
        int flag = 1;
	    cin>>x>>r>>c;
	    switch(x)
	    {
	        case 1:break;
	        case 2:if(r==1&&c==1||r==1&&c==3||r==3&&c==1||r==3&&c==3)
	                    flag = 0;
                    break;
	        case 3:if(r==1||c==1)
	                    flag = 0;
	                else if(r==3||c==3)
	                    flag = 1;
	                else
	                    flag = 0;
	                    break;
	        case 4:
	                if(r==4&&c==4||r==4&&c==3||r==3&&c==4)
	                    flag = 1;
	                else
	                    flag = 0;
	    }
	    cout<<"Case #"<<t<<": ";
	    if(flag)
            cout<<"GABRIEL\n";
        else
            cout<<"RICHARD\n";
	}
}
