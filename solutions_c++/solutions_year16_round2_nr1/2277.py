#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef vector <int> vi;
typedef vector <long long> vill;
typedef pair<int,int> ii;
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfll(a) printf("%I64d\n",a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb(a) push_back(a)
#define fore(i,a,b) for(i=a;i<=b;i++)
#define MO 1000000007
const int MAX = 1e4 + 5;
int n;
int t,m1,i,j,x,y;
long c,c1,cost=0;
vector<int> visited;
int dfs(vector<vector<int> > a,int i,int coun){
    visited[i]=1;
    int j=a[i].size()-1;
    coun++;
    int k;
    fore(k,0,j){
        if(visited[a[i][k]]!=1){
           coun= dfs(a,a[i][k],coun);
        }

    }
    return coun;
}
int main()
{

        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        int t,k=1;
        cin>>t;
        while(t--){
            cout<<"case #"<<k<<": ";
            map<char,int> m;
            string temp;
            cin>>temp;
            int i;
            fore(i,0,temp.length()-1){
                if(temp[i]=='Z'){
                    m['Z']++;
                }
                if(temp[i]=='W'){
                    m['W']++;
                }
                if(temp[i]=='U'){
                    m['U']++;
                }
                if(temp[i]=='X'){
                    m['X']++;
                }
                if(temp[i]=='G'){
                    m['G']++;
                }
                if(temp[i]=='O'){
                    m['O']++;
                }
                if(temp[i]=='R'){
                    m['R']++;
                }
                if(temp[i]=='F'){
                    m['F']++;
                }
                if(temp[i]=='S'){
                    m['S']++;
                }

                if(temp[i]=='N'){
                    m['N']++;
                }
            }
            int no[10];
            no[0]=m['Z'];
            m['O']=m['O']-no[0];
            m['R']=m['R']-no[0];
            no[2]=m['W'];
            m['O']=m['O']-no[2];
            no[4]=m['U'];
            m['F']=m['F']-no[4];
            m['O']=m['O']-no[4];
            m['R']=m['R']-no[4];
            no[6]=m['X'];
            m['S']=m['S']-no[6];
            no[8]=m['G'];
            no[1]=m['O'];
            m['N']=m['N']-no[1];
            no[3]=m['R'];
            no[5]=m['F'];
            no[7]=m['S'];
            m['N']=m['N']-no[7];
            no[9]=m['N']/2;
            fore(i,0,9){
                fore(j,0,no[i]-1){
                    cout<<i;
                }
            }
            cout<<"\n";
            k++;



        }

        return 0;
}

