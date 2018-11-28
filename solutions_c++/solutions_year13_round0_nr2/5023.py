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

 
    
bool f;
int main()
{
ifstream fin;
ofstream fout;
fin.open("input1.txt");
fout.open("output.txt");
int t,n,m;
fin>>t;
int cas=0;
while(t--){cas++;
         fin>>n>>m;
         int arr[n][m];
         for(int i=0;i<n;i++)
         for(int j=0;j<m;j++)
         fin>>arr[i][j];
         vector<int>v1;
         vector<int>v2;
         for(int i=0;i<n;i++){set<int>s;
         for(int j=0;j<m;j++){
                 s.insert(arr[i][j]);
                 
                 }
                 v1.push_back(s.size());
                 s.clear();  
                 }
         for(int i=0;i<m;i++){set<int>s;
         for(int j=0;j<n;j++){
                 s.insert(arr[j][i]);
                 
                 }
                 v2.push_back(s.size());
                 s.clear();  
                 }   
                 int flag=0;
           for(int i=0;i<n;i++){
                   for(int j=0;j<m;j++){
                          if(arr[i][j]==1){
                            if(v1[i]==2 && v2[j]==2)
                            {flag=1;goto xy;}               
                                           
                                           } 
                           
                           }
                           }
                           xy:
                                           if(flag==0)
                                           fout<<"Case #"<<cas<<": "<<"YES"<<endl;
                                           else
                                           fout<<"Case #"<<cas<<": "<<"NO"<<endl;
           }
 //system("pause");
    return 0;

}


