#include <bits/stdc++.h>

#define F first
#define S second
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
//#define TIMER cout<<endl<<"Time Taken : "<<(double)(clock()-t1)/CLOCKS_PER_SEC<<" seconds."<<endl
#define FILE freopen("test.in", "r", stdin); freopen("test.out", "w", stdout)
typedef long long ll;
clock_t t1 = clock();
using namespace std;

bool num[10];
bool check(){
    for(int i=0; i<10; i++){
        if(num[i]==false) return true;
    }
    return false;
}
ll result(int n){
    if(n==0) return -1;
    string s;
    int len,temp,nn=n,k=n,steps=0;
    while(check()){
        s=to_string(nn);
        len=s.length();
        for(int i=0; i<len; i++){
            temp=s[i]-48;
            if(num[temp]==false) num[temp]=true;
        }
        nn=k+n;
        k=nn;
        steps++;
    }
    return steps*n;
}
int main(){
    std::ios::sync_with_stdio(false);
    //remember to reserve the vectors
    #ifdef FILE
		FILE;
	#endif
    int t,n;
    cin>>t;
    for(int i=0; i<t; i++){
        memset(num,false,sizeof(num));
        cin>>n;
        ll res=result(n);
        if(res==-1) cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
	#ifdef TIMER
		TIMER;
	#endif
    return 0;

}
/*
 *@author: Kunal Chaudhary
 */
