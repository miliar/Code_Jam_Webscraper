#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","rt",stdin);
	freopen("a.out","wt",stdout);
    int N,c=0;
    char tab[4][4];
    cin>>N;
    bool ganar=false;
    string s;
    for(int i=0;i<N;i++){
            for(int y=0;y<4;y++)
                for(int yy=0;yy<4;yy++)
                    cin>>tab[y][yy];

        for(int ii=0;ii<4;ii++){
                if(tab[ii][0]==tab[ii][1] && tab[ii][0]==tab[ii][2] && tab[ii][0]==tab[ii][3])
                    if(tab[ii][0]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[ii][0]<<" won"<<endl;ganar=true;}

                if(tab[ii][0]==tab[ii][1] && tab[ii][0]==tab[ii][2] && tab[ii][3]=='T')
                    if(tab[ii][0]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[ii][0]<<" won"<<endl;ganar=true;}

               if(tab[ii][1]==tab[ii][2] && tab[ii][1]==tab[ii][3] && tab[ii][0]=='T')
                   if(tab[ii][1]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[ii][1]<<" won"<<endl;ganar=true;}
        }

        for(int k=0;k<4;k++){
                if(tab[0][k]==tab[1][k] && tab[0][k]==tab[2][k] && tab[0][k]==tab[3][k])
                    if(tab[0][k]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[0][k]<<" won"<<endl;ganar=true;}

                if(tab[0][k]==tab[1][k] && tab[0][k]==tab[2][k]&& tab[3][k]=='T')
                    if(tab[0][k]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[0][k]<<" won"<<endl;ganar=true;}

               if(tab[0][k]==tab[2][k] && tab[0][k]==tab[3][k] && tab[0][k]=='T')
                   if(tab[1][k]!='.'){
                        cout<<"Case #"<<i+1<<": "<<tab[1][k]<<" won"<<endl;ganar=true;}
        }

        if(tab[0][0]==tab[1][1] && tab[0][0]==tab[2][2] && tab[0][0]==tab[3][3])
            if(tab[0][0]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[0][0]<<" won"<<endl;ganar=true;}

        if(tab[0][0]==tab[1][1] && tab[0][0]==tab[2][2] && tab[3][3]=='T')
            if(tab[0][0]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[0][0]<<" won"<<endl;ganar=true;}

        if(tab[1][1]==tab[2][2] && tab[1][1]==tab[3][3] && tab[0][0]=='T')
            if(tab[1][1]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[1][1]<<" won"<<endl;ganar=true;}


         if(tab[0][3]==tab[1][2] && tab[0][3]==tab[2][1] && tab[0][3]==tab[3][0])
            if(tab[0][3]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[0][3]<<" won"<<endl;ganar=true;}

        if(tab[1][2]==tab[2][1] && tab[1][2]==tab[3][0] && tab[0][3]=='T')
            if(tab[1][2]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[1][2]<<" won"<<endl;ganar=true;}

        if(tab[3][0]=='T' && tab[2][1]==tab[1][2] && tab[2][1]==tab[0][3])
            if(tab[2][1]!='.'){
                cout<<"Case #"<<i+1<<": "<<tab[2][1]<<" won"<<endl;ganar=true;}

        if(ganar==false){
            for(int j=0;j<4;j++)
                for(int m=0;m<4;m++)
                    if(tab[j][m]=='.')c=1;

            if(c==1)cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
            else cout<<"Case #"<<i+1<<": Draw"<<endl;
        }

        getline(cin,s);
        ganar =false;
        c=0;
    }
    //cout<<tab[2][1];
    return 0;
}
