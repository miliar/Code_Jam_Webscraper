#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
    freopen("A2.in.txt", "r", stdin);
    freopen("A2.out.txt", "w", stdout);
    long test,cs=1;
    long ans,i,j,n;
    string s;
    scanf("%ld",&test);
    while(test--){
        scanf("%ld",&n);
        cin>>s;
        ans=0;
        long have = s[0]-'0';
        for(i=1;i<=n;i++){
            //cout<<have;
            if(have<i){
                ans=ans+(i-have);
                have=i;
            }
            have = have+(s[i]-'0');
            //cout<<" "<<ans<<endl;
        }
        printf("Case #%ld: %ld\n",cs++,ans);
    }
    return 0;
}

/*
Input:
4
4 11111
1 09
5 110011
0 1

Output:
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
*/
