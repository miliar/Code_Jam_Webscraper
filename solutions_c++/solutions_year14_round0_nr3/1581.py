#include <iostream>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctime>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

int main(){
    ofstream myfile;
    myfile.open("vats1.txt");
    int test,l=0;
    cin>>test;
    while(test--){
        l++;
        int r,c,m,i,j,mine;
        int f = 0;
        int mat[25][25];
        for(i=0;i<25;i++){
            for(j=0;j<25;j++){
                mat[i][j] = 1;
            }
        }
        cin>>r>>c>>mine;
        myfile<<"Case #"<<l<<":\n";
        m = r*c - mine;
        if(m<=0){
            f = 1;
            myfile<<"Impossible\n";
        }
        else if(m==1){
            mat[0][0]=2;
            m--;
        }
        else if(r==1){
            for(i=0;i<c;i++){
                if(m>0)
                    mat[0][i] = 0;
                m--;
            }
            mat[0][0] = 2;
        }
        else if(c==1){
            for(i=0;i<r;i++){
                if(m>0)
                    mat[i][0] = 0;
                m--;
            }
            mat[0][0] = 2;
        }
        else if(m==2||m==3||m==5||m==7){
            f = 1;
            myfile<<"Impossible\n";
        }
        else if(r==2||c==2){
            if(m%2!=0){
                f = 1;
                myfile<<"Impossible\n";
            }
            else if(r==2){
                int i1 = 0;
                int j1 = 0;
                while(m>0){
                    mat[i1][j1] = 0;
                    mat[i1+1][j1] = 0;
                    j1++;
                    m-=2;
                }
            }
            else if(c==2){
                int i1 = 0;
                int j1 = 0;
                while(m>0){
                    mat[i1][j1+1] = 0;
                    mat[i1][j1] = 0;
                    i1++;
                    m-=2;
                }
            }
        }
        else if(m%2==0){
            int i1=0,j1=0;
            while(m>0&&j1<=c-1){
                mat[i1][j1] = 0;
                mat[i1+1][j1] = 0;
                m-=2;
                j1++;
            }
            i1 = 2;
            j1 = 0;
            while(m>0&&i1<r){
                //cout<<i1<<" "<<j1<<"\n";
                if(j1<c&&j1+1<c){
                    //cout<<"hhk\n";
                    mat[i1][j1] = 0;
                    mat[i1][j1+1] = 0;
                    m-=2;
                    j1+=2;
                }
                else{
                    j1 = 0;
                    i1++;
                }
            }
            mat[0][0] = 2;
        }
        else {
            for(i=0;i<=2;i++){
                for(j=0;j<=2;j++){
                    mat[i][j] = 0;
                }
            }
            m-=9;
            int i1,j1;
            i1 = 0;
            j1 = 3;
            while(m>0&&j1<=c-1){
                mat[i1][j1] = 0;
                mat[i1+1][j1] = 0;
                m-=2;
                j1++;
            }
            i1 = 2;
            j1 = 3;
           while(m>0&&i1<r){
                if(j1>=c){
                        j1=0;
                        i1++;
                }
                if(j1<c&&j1+1<c){
                    mat[i1][j1] = 0;
                    mat[i1][j1+1] = 0;
                    m-=2;
                    j1+=2;
                }
                else{
                    j1 = 0;
                    i1++;
                }
            }
            mat[0][0] = 2;
        }
        if(f==1){
           //cout<<"Impossible\n";
        }
        else if(f==0){
            int x = 0;
            for(i=0;i<r;i++){
                for(j=0;j<c;j++){
                    if(mat[i][j]==0){
                        //cout<<".";
                    }
                    else if(mat[i][j]==1){
                        //cout<<"*";
                        x++;
                    }
                    else if(mat[i][j]==2){
                        //cout<<"c";
                    }
                }
                //cout<<"\n";
            }
            //cout<<x<<"\n";
            if(x>mine){
                int j1 = c-1;
                int i1 = 0;
                while(x!=mine){
                    if(mat[i1][j1]==1){
                        mat[i1][j1] = 0;
                        x--;
                    }
                    i1++;
                }
            }
            int co = 0;
            for(i=0;i<r;i++){
                if(mat[i][c-1]==1){
                    co++;
                }
            }
            int it1 = r-1;
            while(it1!=-1){
                if(co>0){
                    mat[it1][c-1] = 1;
                    co--;
                }
                else{
                    mat[it1][c-1] = 0;
                }
                it1--;
            }
            mat[0][0] = 2;
            for(i=0;i<r;i++){
                for(j=0;j<c;j++){
                    if(mat[i][j]==0){
                        myfile<<".";
                    }
                    else if(mat[i][j]==1){
                        myfile<<"*";
                        //x++;
                    }
                    else if(mat[i][j]==2){
                        myfile<<"c";
                    }
                }
                myfile<<"\n";
            }
            if(x==mine){
                //cout<<"YES!!\n";
            }
            else{
                //cout<<"NO!!!!!!!!!!!!!!!\n";
            }
        }
    }
    return 0;
}
