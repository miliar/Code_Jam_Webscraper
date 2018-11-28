#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <limits.h>
#include <vector>
#include <list>
#define mod 1000000007
#define SIZE 2000
#define ll long long
#define INF LLONG_MAX
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

char str[SIZE];

int main() {
    //freopen("inp.txt","r",stdin);
	//freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int tc,i,n,j,k,temp_i;
    char ch,temp;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>str;
        n=strlen(str);
        list<char> ls;
        list<char>::iterator itr;
        ls.push_back(str[0]);
        for(i=1;i<n;i++){
            if(str[i]>=*ls.begin())
                ls.push_front(str[i]);
            else ls.push_back(str[i]);
        }
		cout<<"Case #"<<t<<": ";
		for(itr=ls.begin();itr!=ls.end();itr++)
            cout<<*itr;
        cout<<"\n";
	}
	return 0;
}
