#include <cmath>
#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
#include <bitset>
#include <memory.h>
#include <functional>
#include <queue>
#include <fstream>
#include <ctime>
#include <deque>
#include <utility>
#include <stack>
#include <sstream>
#include <list>
#include <cctype> 
#include <numeric> 
#include <iomanip>
#include <assert.h>
using namespace std;

int main(){
    int n,j;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>n;
    for(j=1;j<=n;j++){
        int a[5],n,t[17]={0};
        int i,m;
        cin>>m;
        if(m==1) {cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=12;k++)cin>>n;}
        if(m==2) {for(int k=1;k<=4;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=8;k++)cin>>n;}
        if(m==3) {for(int k=1;k<=8;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=4;k++)cin>>n;}
        if(m==4) {for(int k=1;k<=12;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];}   
        for(i=1;i<=16;i++){
            if(a[1]==i) t[i]++;
            if(a[2]==i) t[i]++;
            if(a[3]==i) t[i]++;
            if(a[4]==i) t[i]++;
        }
        cin>>m;
        if(m==1) {cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=12;k++)cin>>n;}
        if(m==2) {for(int k=1;k<=4;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=8;k++)cin>>n;}
        if(m==3) {for(int k=1;k<=8;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];for(int k=1;k<=4;k++)cin>>n;}
        if(m==4) {for(int k=1;k<=12;k++)cin>>n;cin>>a[1]>>a[2]>>a[3]>>a[4];}     
        for(i=1;i<=16;i++){
            if(a[1]==i) t[i]++;
            if(a[2]==i) t[i]++;
            if(a[3]==i) t[i]++;
            if(a[4]==i) t[i]++;
        }
        int cnt=0,ans=-1;
        string anstext[2]={"Bad magician!","Volunteer cheated!"};
        for(i=1;i<=16;i++){
            
            if(t[i]==2){
            cnt++;
            if(cnt==1) {ans=i;}
            else {ans=-2;}
            }
        
        
        }
        cout<<"Case #"<<j<<": ";
        if(ans>0) {cout<<ans;}
        else if(ans==-1) {cout<<anstext[1];}
        else if(ans==-2) {cout<<anstext[0];}
        cout<<endl;
        
    }
    return 0;
}
   