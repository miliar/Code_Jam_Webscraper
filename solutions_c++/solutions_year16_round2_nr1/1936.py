#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <map>

#define ll long long int
#define pll pair<long long, long long>
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define getchar_unlocked getchar
#define F first
#define S second

using namespace std;

int getint();
long long getlint();

bool ispossible(map<char, int> m, string a);

int main() {
    int testcases ;
	scanf("%d", &testcases);
    for(int t = 1; t<=testcases;t++) {
        string a;
        cin>>a;
        map <char, int> m;
        for(int i=0;i<26;i++) {
            m['A'+i]=0;
        }
        int sz = (int) a.size();
        for(int i=0;i<sz;i++) {
            m[a[i]]++;
        }
        map <int, string> s;
        s[0] = "ZERO";
        s[1] = "ONE";
        s[2] = "TWO";
        s[3] = "THREE";
        s[4] = "FOUR";
        s[5] = "FIVE";
        s[6] = "SIX";
        s[7] = "SEVEN";
        s[8] = "EIGHT";
        s[9] = "NINE";
        vector <int> nums;
        while(ispossible(m, s[0])) {
        	nums.pb(0);
        	string as = s[0];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[6])) {
        	nums.pb(6);
        	string as = s[6];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[7])) {
        	nums.pb(7);
        	string as = s[7];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[5])) {
        	nums.pb(5);
        	string as = s[5];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[8])) {
        	nums.pb(8);
        	string as = s[8];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[2])) {
        	nums.pb(2);
        	string as = s[2];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[3])) {
        	nums.pb(3);
        	string as = s[3];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[4])) {
        	nums.pb(4);
        	string as = s[4];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[9])) {
        	nums.pb(9);
        	string as = s[9];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        while(ispossible(m, s[1])) {
        	nums.pb(1);
        	string as = s[1];
			for(int i=0;i<as.size();i++) {
				m[as[i]]--;
			}
        }
        sort(nums.begin(), nums.end());
        printf("Case #%d: ", t);
        for(int i=0;i<nums.size();i++) {
        	printf("%d", nums[i]);
        }
        printf("\n");
    }
	return 0;
}

bool ispossible(map<char, int> m, string a) {
	for(int i=0;i<a.size();i++) {
		if(m[a[i]]==0)
		return false;
	}
	return true;
}

int getint()
{
    int c,num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}

long long int getlint()
{
    int c;
    long long num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    long long int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}

