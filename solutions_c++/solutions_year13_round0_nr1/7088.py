#include<iostream>
#include<vector>
#define N 8
#define L 4

using namespace std;

char A[N][N];

bool val(int i,int j){
    return i>=0&&i<4&&j>=0&&j<4;
}

char gan(char a,char b,char c,char d){
    vector<char> v;
    v.push_back(a);    
    v.push_back(b);
    v.push_back(c);
    v.push_back(d);
    sort(v.begin(),v.end());
    int ct0=0,ct1=0,ct2=0;
    for(int i=0;i<v.size();i++){
        if(v[i]=='X')ct0++;
        if(v[i]=='O')ct1++;
        if(v[i]=='T')ct2++;
    }
    if((ct2==1&&ct0==3)||(ct2==1&&ct1==3)||(ct0==4)||(ct1==4))return v[1];
    return '#';
}

int main(){
    int nc;
    cin>>nc;
    for(int caso=1;caso<=nc;caso++){
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)cin>>A[i][j];
        char res='#';
        //Vertical
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)if(val(i,j)&&val(i+1,j)&&val(i+2,j)&&val(i+3,j))if(res=='#')res=gan(A[i][j],A[i+1][j],A[i+2][j],A[i+3][j]);
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)if(val(i,j)&&val(i,j+1)&&val(i,j+2)&&val(i,j+3))if(res=='#')res=gan(A[i][j],A[i][j+1],A[i][j+2],A[i][j+3]);
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)if(val(i,j)&&val(i+1,j+1)&&val(i+2,j+2)&&val(i+3,j+3))if(res=='#')res=gan(A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]);
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)if(val(i,j)&&val(i-1,j+1)&&val(i-2,j+2)&&val(i-3,j+3))if(res=='#')res=gan(A[i][j],A[i-1][j+1],A[i-2][j+2],A[i-3][j+3]);
        int ct=0;
        for(int i=0;i<L;i++)for(int j=0;j<L;j++)if(A[i][j]=='.')ct++;
        /*cout<<ct<<endl;
        for(int i=0;i<L;i++){
            for(int j=0;j<L;j++)cout<<A[i][j];
            cout<<endl;
        }*/
        if(res!='#')cout<<"Case #"<<caso<<": "<<res<<" won"<<endl;
        else{
            if(ct==0)cout<<"Case #"<<caso<<": Draw"<<endl;
            else cout<<"Case #"<<caso<<": Game has not completed"<<endl;
        }
    }
}
