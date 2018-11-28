#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdio.h>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <fstream>
using namespace std;
int check(string s1,string s2){
 if(s1.size()>s2.size())
 return 1;
 else if (s2.size()>s1.size())
 return 0;
 else if(s1.size()==s2.size()){
     if(s1>s2)
     return 1;
     else if(s2>s1)
     return 0;  
     else return 1;
      
      }   
      
}
int main()
{
    ifstream fin;
  fin.open("input1.txt");
    ofstream fout;
    fout.open("output.txt");
int t;fin>>t;
string s[48]={"1","4","9","121","484","10201","12321","14641","40804","44944","1002001","1234321","4008004","100020001","102030201","104060401","121242121","123454321","125686521","400080004","404090404","10000200001","10221412201","12102420121","12345654321","40000800004","1000002000001","1002003002001","1004006004001","1020304030201","1022325232201","1024348434201","1210024200121","1212225222121","1214428244121","1232346432321","1234567654321","4000008000004","4004009004004","100000020000001","100220141022001","102012040210201","102234363432201","121000242000121","121242363242121","123212464212321","123456787654321","400000080000004"};

string n,m;
     int cas=0;
while(t--){cas++;
         fin>>n>>m;
         int ans=0;
        int i,j;
        set<string>s1;
        for(int i=0;i<48;i++){
       
                
                if(check(s[i],n) && check(m,s[i]))
        {
                s1.insert(s[i]);
                }      
                }
                fout<<"Case #"<<cas<<": "<<s1.size()<<endl;
           s1.clear();
        }   
 //system("pause");
    return 0;

}


