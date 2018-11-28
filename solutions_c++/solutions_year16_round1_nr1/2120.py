typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair

using namespace std;
int main()
{
    ll t,i,l,w=1;
    string s,s1;
    scanf("%lld",&t);
    while(t--)
    {
        cin>>s;
        l=s.length();
        s1=s[0];
        for(i=1;i<l;i++)
        {
            if(s[i]>=s1[0])
            s1=s[i]+s1;
            else
            s1=s1+s[i];
        }
        cout<<"Case #"<<w++<<": "<<s1<<endl; 
    }
	return 0;
}