#include<bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	lld test,i,j,k,l,m,n;
    k=1;
	string str,str1;
	cin>>test;
	while(test--){

    pair<lld,lld> ans[26];
    cin>>n;

    lld sum=0;
    for(i=0;i<n;i++){
        ans[i].second=i;
        cin>>ans[i].first;
        sum+=ans[i].first;
    }

//cout<<sum<<endl;

    sort(ans,ans+n);
    reverse(ans,ans+n);
    cout<<"Case #"<<k<<": ";
    if(n==2){
        for(i=0;i<sum/2;i++){
            cout<<"BA ";
        }
        cout<<endl;
        k++;
        continue;
    }
    while(sum>2){
        m=ans[0].first;
        j=ans[0].second;
        ans[0].first-=1;
        sum-=1;
        cout<<(char)('A'+j)<<" ";
        sort(ans,ans+n);
        reverse(ans,ans+n);
    }
    cout<<(char)('A'+ans[0].second)<<(char)('A'+ans[1].second)<<endl;
    k++;
    }

    return 0;
}
