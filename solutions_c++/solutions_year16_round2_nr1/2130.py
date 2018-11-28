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
	string str;
	cin>>test;
	while(test--){
	cin>>str;
       int arr[26]={};
       for(i=0;i<str.length();i++){
        arr[str[i]-'A']++;
       }
       int ans[10]={};
       ans[0]=arr[25];
       ans[2]=arr['W'-'A'];
       ans[4]=arr['U'-'A'];
       ans[6]=arr['X'-'A'];
       ans[8]=arr['G'-'A'];
       ans[1]=arr['O'-'A']-ans[2]-ans[4]-ans[0];
       ans[3]=arr['T'-'A']-ans[2]-ans[8];
       ans[5]=arr['F'-'A']-ans[4];
       ans[7]=arr['V'-'A']-ans[5];
       ans[9]=arr['I'-'A']-ans[5]-ans[8]-ans[6];
       cout<<"Case #"<<k<<": ";
       for(i=0;i<10;i++){
        for(j=0;j<ans[i];j++)
            cout<<i;
       }
    cout<<endl;
    k++;
    }

    return 0;
}
