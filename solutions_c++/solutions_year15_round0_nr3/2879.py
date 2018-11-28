#include <bits/stdc++.h>
using namespace std;

int resolve(int a, int b){
    if (a==b and abs(b)!=1) return -1;
    if (a==-b and abs(b)!=1) return 1;
    if ((a==2 and b==3) or (a==-2 and b==-3)) return 4;
    if ((a==2 and b==4) or (a==-2 and b==-4)) return -3;
    if ((a==3 and b==2) or (a==-3 and b==-2)) return -4;
    if ((a==3 and b==4) or (a==-3 and b==-4)) return 2;
    if ((a==4 and b==2) or (a==-4 and b==-2)) return 3;
    if ((a==4 and b==3) or (a==-4 and b==-3)) return -2;

    if ((a==2 and b==-3) or (a==-2 and b==3)) return -4;
    if ((a==2 and b==-4) or (a==-2 and b==4)) return 3;
    if ((a==3 and b==-2) or (a==-3 and b==2)) return 4;
    if ((a==3 and b==-4) or (a==-3 and b==4)) return -2;
    if ((a==4 and b==-2) or (a==-4 and b==2)) return -3;
    if ((a==4 and b==-3) or (a==-4 and b==3)) return 2;
    return a*b;
}

int main(){
    freopen("Csmallin.txt","r",stdin);
    freopen("Csmallout.txt","w",stdout);
    int n;
    cin>>n;
    for (int i=0; i<n; i++){
        int x,l;
        string a,b;
        cin>>x>>l;
        cin>>a;
        b=a;
        for (int j=0; j<l-1; j++){
            a+=b;
        }
        if (a.length()<3){
            cout<<"Case #"<<i+1<<": NO"<<endl;
            continue;
        }
        int cur=1, searchfor=2;
        for (int j=0; j<a.length(); j++){
            if (a[j]=='j') cur=resolve(cur,3);
            if (a[j]=='i') cur=resolve(cur,2);
            if (a[j]=='k') cur=resolve(cur,4);
            if (cur==searchfor){
                if (searchfor<4){
                    searchfor++;
                    cur=1;
                }
            }
        }
        if (searchfor!=4 or cur!=4){
            cout<<"Case #"<<i+1<<": NO"<<endl;
            continue;
        }
        cout<<"Case #"<<i+1<<": YES"<<endl;
    }
    return 0;
}
