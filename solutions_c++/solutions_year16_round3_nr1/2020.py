// By manrajsingh
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define d1(a)cout<<#a<<": "<<a<<"\n";
#define d2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<"\n";
#define d3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<"\n";
#define d4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<"\n";

ll a[1005];

int main() {
    int t,x=0;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>t;
    while(t--){
        x++;
        char ad = 'A';
        ll n;
        cin>>n;
        priority_queue<pair<int,char> >pq;
        for(int i=0;i<n;i++){
            cin>>a[i];
            char temp = ad+i;
            pq.push(make_pair(a[i],temp));
        }
        cout<<"Case #"<<x<<": ";
        int f = 0;
        pair<int,char> t2;
        while(!pq.empty()){
            pair<int,char> temp = pq.top();
            if(temp.first==1 && pq.size() == 3){
                pq.pop();cout<<temp.second<<" ";
                continue;
            }
            pq.pop();
            if(!pq.empty()){
                t2 = pq.top();
                pq.pop();
                f=1;
            }
            cout<<temp.second<<t2.second<<" ";
            if(f){
                temp.first=temp.first-1;
                t2.first=t2.first-1;
                if(temp.first>0){
                    pq.push(temp);
                }
                if(t2.first>0){
                    pq.push(t2);
                }
            }
            else{
                temp.first=temp.first-2;
                if(temp.first>0){
                    pq.push(temp);
                }
            }
        }
        cout<<"\n";
    }
	return 0;
}
