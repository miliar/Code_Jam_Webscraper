
#include<string.h>

#include<stdio.h>

#include<stdlib.h>

#include<ctype.h>

#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include<cstdlib>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <fstream>
#define INF     9999999
using namespace std;
double pp[30][1010][1010];
int main()
{
    ifstream cin("a.in");
    ofstream cout("out.out");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cout<<"Case #"<<tt<<": ";
        int n;
        int num=0;
        cin>>n;
        string s[n];
        string t[n];
        for(int i=0;i<n;i++){
            cin>>s[i];


        }
        bool flag=true;
        //int num=0;
        int lentgh=max(s[0].length(),s[1].length());
        int j=0;
        int i=0;
        for(;i<s[0].length();i++){
            if(s[0][i]==s[1][j]){j++;continue;}
            if(j>0)
                if(s[0][i]==s[1][j-1]){num++;continue;}
            if(i>0)
                if(s[0][i-1]==s[1][j]){j++;i--;num++;continue;}
            flag=false;
        }
        for(;j<s[1].length();j++){
            if(s[1][j]==s[0][s[0].length()-1]){num++;continue;}
            flag=false;
        }
        if(i<s[0].length())flag=false;
        if(flag==false)cout<<"Fegla Won"<<endl;
        else cout<<num<<endl;

    }



}
