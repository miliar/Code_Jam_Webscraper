///This  code is created by Samar Singh Holkar
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include<list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)
#define sfd(x) scanf("%d",&x)
#define sfld(x) scanf("%lld",&x
#define pf printf

#define LL long long
#define ll long long
#define LD long double
#define ld long double
#define PB push_back
#define pb push_back
#define MP make_pair
#define mp make_pair
#define F first
#define S second

#define pii pair<int,int>
#define vi vector<int>
#define fr(i,n) for( int i=0; i<=n; i++)
#define frm(i,m,n) for(int i=m; i<=n; i++)
#define N 200000

struct SegmentTreeNode {
	int unmatchedOpenParans, unmatchedClosedParans;

	void assignLeaf(char paranthesis) {
		if (paranthesis == '(')
			unmatchedOpenParans = 1, unmatchedClosedParans = 0;
		else
			unmatchedOpenParans = 0, unmatchedClosedParans = 1;
	}

	void merge(SegmentTreeNode& left, SegmentTreeNode& right) {
		int newMatches = min(left.unmatchedOpenParans, right.unmatchedClosedParans);
		unmatchedOpenParans = right.unmatchedOpenParans + left.unmatchedOpenParans - newMatches;
		unmatchedClosedParans = left.unmatchedClosedParans + right.unmatchedClosedParans - newMatches;
	}

	bool getValue() {
		return unmatchedOpenParans == 0 && unmatchedClosedParans == 0;
	}
};

ll fast_pow(ll base, ll n,ll M)
{
    if(n==0)
       return 1;
    if(n==1)
    return base;
    long long halfn=fast_pow(base,n/2,M);
    if(n%2==0)
        return ( halfn * halfn ) % M;
    else
        return ( ( ( halfn * halfn ) % M ) * base ) % M;
}



ll findMMI_fermat(ll n,ll M)
{
    return fast_pow(n,M-2,M);
}

ll fact[100003];

ll factorial(){

    fact[0] = 1;

    for(int i=1;i<=100003;i++){

        fact[i] = (fact[i-1]*(i))%N;
    }
}

char chan_sign(char x){

    switch(x){

        case 'i':return 'a';

        case 'j':return 'b';

        case 'k':return 'c';

        case 'a':return 'i';

        case 'b':return 'j';

        case 'c':return 'k';

        case 'z':return '1';

        case '1':return 'z';

    }
}
bool isPos(char x){

    if(x=='a'||x=='b'||x=='c')return false;

    return true;
}
char neg(char x,char y){

    if(max(x,y)=='j')return 'k';

    if(min(x,y)=='i')return 'j';

    if(min(x,y)=='j')return 'i';
}
char cal(char x,char y){

    if(x==y)return 'z';

    char ans=neg(x,y);

    if(x=='i'&&y=='k')return chan_sign(ans);

    if(x=='j'&&y=='i')return chan_sign(ans);

    if(x=='k'&&y=='j')return chan_sign(ans);

    return ans;
}
char ab(char x){

    if(isPos(x))return x;

    return chan_sign(x);
}
char f(char x,char y){

    if(x=='1')return y;

    if(x=='z')return chan_sign(y);

    if(x==y)return 'z';


    bool sign=(isPos(x))^(isPos(y));

    char ans=cal(ab(x),ab(y));

    if(!sign){

        return ans;

    }

    return chan_sign(ans);
}
int main(){

    factorial();

    int t,p=0;

    cin>>t;

    while(t--){

        p++;

        ll n,x;

        cin>>n>>x;

        string temp;

        cin>>temp;

        //x%=4;
        string s="";

        n=n*x;

        while(x--){

            s.append(temp);

        }

        bool ans=false;

        if(x==0){

            ans=false;

        }else{

            char cur=s[0];

            int i=1;

            while(cur!='i'&&i<n){

                cur=f(cur,s[i]);

                //cout<<cur<<endl;
                i++;
            }

            if(i<n){

                cur=s[i];


                i++;

                while(cur!='j'&&i<n){

                    cur=f(cur,s[i]);

                    //cout<<cur<<endl;

                    i++;

                }

                if(i<n){

                    cur=s[i];



                    i++;

                    while(i<n){

                        cur=f(cur,s[i]);

                        //cout<<cur<<endl;

                        i++;

                    }

                    //cout<<cur<<endl;

                    if(cur=='k')ans=true;

                }

            }

        }

        if(ans)cout<<"Case #"<<p<<": YES";

        else{

            cout<<"Case #"<<p<<": NO";

        }

        cout<<endl;

    }


   /* char cur='1';

    while(1){

        char temp;

        cin>>temp;

        cur=f(cur,temp);

        cout<<cur<<endl;

    }*/



}
