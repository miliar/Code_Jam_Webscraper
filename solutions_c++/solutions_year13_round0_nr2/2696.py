#include<iostream>
#include<istream>
#include<vector>
#include<string>
#include<bitset>
#include<algorithm>
#include<sstream>
#include<map>
#include<set>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdio>
using namespace std;
void printMatrix(vector< vector<int> > mat){
     for(int i=0;i<mat.size();++i){
                       for(int j=0;j<mat[i].size();++j){
                               cout<<mat[i][j]<<" ";
                        }
                        cout<<endl;
     }
}
bool check(vector<int> x, int value){
     int i=0;
     for(i=0;i<x.size();++i)
             if(value!=x[i])break;
     if(i==x.size())return true;
     return false;
}
int main()
{
    int t;
    cin>>t;
   
    for(int k=0;k<t;++k){
            int n,m;
            cin>>n>>m;
            vector< vector<int> > rowMatrix;
            vector< vector<int> > finalMatrix;
            for(int i=0;i<n;++i){
                        vector<int>r(m,2);
                        /*for(int j=0;j<m;++j){
                              r.push_back(2);
                        }*/
                        finalMatrix.push_back(r);
            }
           // cout<<" *****final matrix***************  "<<endl;
            //printMatrix(finalMatrix);
            for(int i=0;i<n;++i){
                        vector<int>row;
                        for(int j=0;j<m;++j){
                                int x;
                                cin>>x;
                                row.push_back(x);
                        }
                        rowMatrix.push_back(row);
            }
           // cout<<" *****row matrix***************  "<<endl;
            //printMatrix(rowMatrix);
            vector< vector<int> > colMatrix;
       
            for(int i=0;i<m;++i){
                     vector<int>col;
                     for(int j=0;j<n;++j){
                             col.push_back(rowMatrix[j][i]);
                     }
                     colMatrix.push_back(col);
            }
            for(int i=0;i<n;++i){

                    if(rowMatrix[i][0]==1){
                                                               vector<int>p=rowMatrix[i];
                                                               if(check(p,1)){
                                                                              for(int j=0;j<m;++j){
                                                                                      finalMatrix[i][j]=1;
                                                                              }
                                                               }
                                           }
            }
            for(int i=0;i<m;++i){

                    if(colMatrix[i][0]==1){
                                                               vector<int>p=colMatrix[i];
                                                               if(check(p,1)){
                                                                              for(int j=0;j<n;++j){
                                                                                      finalMatrix[j][i]=1;
                                                                              }
                                                               }
                                           }
            }
            cout<<"Case #"<<k+1<<": "<<((finalMatrix==rowMatrix)?"YES":"NO")<<endl;
            //cout<<"case: "<<k+1<<": "<<((finalMatrix==rowMatrix)?"YES":"NO")<<endl;
           // cout<<" *****col matrix***************  "<<endl;
            //printMatrix(colMatrix);
    }
        //cout<<"Case #"<<k+1<<": "<<count<<endl;
       
}
