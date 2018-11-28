#include<bits/stdc++.h>
using namespace std;
#define MAXN 200005
#define mod 1000000007
#define ll long long
#define ull unsigned long long

ull gcd(ull a,ull b){
	ull r;
	while(1){
		r=a%b;
		if(r==0) return b;
		a=b;
		b=r;
	}
	return r;
}
vector < pair <ll ,char > > vec;
pair <ll,char > p;
int  main(){ 
    ll n,t,k,f,test = 1,inp[MAXN];
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	cin>>t;
    
    while(t--){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>inp[i];
            p = make_pair(inp[i],i+'A');
            vec.push_back(p);
            //cout<<vec[i].first<<" "<<vec[i].second<<endl;
        }

        cout<<"Case #"<<test<<": ";
        while(1){
            ll m,sm,total,indm,indsm,num=0;
            m = vec[0].first;
            sm = 0;
            total = vec[0].first;
            indm = indsm = 0;
            if(vec[0].first) num++;
            for(int i=1;i<n;i++){
                if(vec[i].first>m) sm = m,m = vec[i].first,indsm = indm,indm = i;
                else if(vec[i].first>sm) sm = vec[i].first,indsm = i;
                if(vec[i].first) num++;
            }
            //cout<<indm<<" "<<indsm<<endl;
            if(m>1){
                if(total-sm>sm){
                    cout<<vec[indm].second<<vec[indm].second<<" ";
                    vec[indm].first-=2;
                }
                else{
                    cout<<vec[indm].second<<vec[indsm].second<<" ";
                    vec[indm].first-=1;
                    vec[indsm].first-=1;
                }
            }
            else if(m){
                if(num%2 == 0){
                    cout<<vec[indm].second<<vec[indsm].second<<" ";
                    vec[indm].first-=1;
                    vec[indsm].first-=1;
                } 
                else{
                    cout<<vec[indm].second<<" ";
                    vec[indm].first-=1;
                } 
            }
            else{
                break;
            }
        }
        cout<<endl;

        test++;
        vec.clear();
    }
    
    return 0;
}
