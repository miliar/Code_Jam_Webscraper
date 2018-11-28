//start of VMFP template version 1.4
#define Shubham using
#define VMFP namespace
#define IITBHU std
//#include<bits/stdc++.h>
//#include <stdio.h>
//#include <utility>
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
#include<stack> //empty() size() top() push() pop()
#include<queue> // empty() size() front() back() push() pop()
//#include<climits>
//#include<limits>
#include<sstream>
#include<algorithm>
#include<fstream>
#include<string>
#include<math.h>
#define large INT_MAX;
#define small INT_MIN;
#define FOR(a,b) for (int (a)=0;(a)<(b);(a)++)
//#define TC(t) while(t--)
#define SORT(a,i,j) sort(a+i,a+j+1); // sorting from integar post i to integar post j both inclusive
#define MIN(a,b) min(a,b);
#define MAX(a,b) max(a,b);
#define value(x) cerr << "The value of " << #x << " is " << x << endl
#define value2(x,y) cerr<<"value of "<<#x<<" is "<<x<<" and value of "<<#y<<" is "<<y<<endl;
#define value3(x,y,z) cerr<<"value of "<<#x<<" is "<<x<<" and value of "<<#y<<" is "<<y<<" and value of "<<#z<<" is "<<z<<endl;
#define lli long long int
#define line cout<<endl
#define vadd(vector,position,value) vector.insert(vector.begin()+position,value)
#define vremove(vector,position) vector.erase(vector.begin()+position)
#define vpush(vector,value) vector.push_back(value)
Shubham VMFP IITBHU;
inline string inttostring(lli a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int stringtoint(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}
inline string uppercase(string s){
  int n = s.length();
  FOR(i,n) if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
  return s;
}

inline string lowercase(string s){
  int n = s.length();
  FOR(i,n) if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
  return s;
}
//end of VMFP template version 1.4

int lengthofintegar(lli n){
    int result = 0;
    while(n){
        result++;
        n=n/10;
    }
    return result;
}

int main(){
    //cout.precision(15);
    ifstream ifile;
    ofstream ofile;
    ifile.open("input.in");
    ofile.open("outputfile.txt");
    int t;
    ifile>>t;
    for(int z1=1;z1<=t;z1++){
        int n;
        ifile>>n;
        if(n){
            bool result[10]={false};
            lli tmp;
            for(int prescount=1;prescount<INT_MAX;prescount++){
                tmp = prescount * n;
                string a = inttostring(tmp);
                for(int var1=0;var1<lengthofintegar(tmp);var1++){
                    result[a[var1]-'0']=true;
                }
                for(int i=0;i<10;i++){
                    if(result[i]==false){
                        goto somewhere1;
                    }
                }
                ofile<<"Case #"<<z1<<": "<<tmp<<endl;
                goto elsewhere1;
                somewhere1:;
            }
        }
        else{
            ofile<<"Case #"<<z1<<": "<<"INSOMNIA"<<endl;
        }
        elsewhere1:;
    }
    ifile.close();
    ofile.close();
    return 0;
}
