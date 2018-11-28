#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    int t,pos,i=0,j,l,x,a[256][256]={0},tmp,cnt=0;
    char c[10001];
    a[ 1 ][1]= 1 ; a[ 1 ]['i']='i'; a[ 1 ]['j']='j'; a[ 1 ]['k']='k';
    a['i'][1]='i'; a['i']['i']='l'; a['i']['j']='k'; a['i']['k']='n';
    a['j'][1]='j'; a['j']['i']='o'; a['j']['j']='l'; a['j']['k']='i';
    a['k'][1]='k'; a['k']['i']='j'; a['k']['j']='m'; a['k']['k']='l';
    a['l'][1]='l'; a['l']['i']='m'; a['l']['j']='n'; a['l']['k']='o';
    a['m'][1]='m'; a['m']['i']= 1 ; a['m']['j']='o'; a['m']['k']='j';
    a['n'][1]='n'; a['n']['i']='k'; a['n']['j']= 1 ; a['n']['k']='m';
    a['o'][1]='o'; a['o']['i']='n'; a['o']['j']='i'; a['o']['k']= 1 ;
    for(cin>>t,i=0; i<t; i++)
    {
        cin>>l>>x; cin>>c; cnt=0; tmp=1; //cout<<(char)tmp;
        for(j=0;j<x;j++)
        {
            for(int k=0;k<l;k++)
            {
               if(cnt==0)
               {
                    if(tmp=='i') { cnt++; tmp=c[k];/*cout<<"cnt:"<<cnt<<"\n";*/} else tmp=a[tmp][c[k]];
               }
               else if(cnt==1)
               {
                    if(tmp=='j') { cnt++; tmp=c[k];/*cout<<"cnt:"<<cnt<<"\n";*/} else tmp=a[tmp][c[k]];
               }
               else tmp=a[tmp][c[k]];
               //cout<<(char)tmp;
            }
        }
        if(cnt==2 && tmp=='k') cout<<"Case #"<<i+1<<": YES"<<endl;
        else            cout<<"Case #"<<i+1<<": NO"<<endl;
    }
}
