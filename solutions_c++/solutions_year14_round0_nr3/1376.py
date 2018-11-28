#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<fstream>
using namespace std;
#define ISDEBUG 0
int main()
{
    fstream fin,fout;
//    fin.open("C-small-attempt8.in",ios::in);
//    fout.open("C-small-attempt8.out",ios::out);
    fin.open("C-large.in",ios::in);
    fout.open("C-large.out",ios::out);
    int T,r,c,m;
    fin>>T;
    #if ISDEBUG==0
    cout.rdbuf(fout.rdbuf());
    #endif
    for(int t=1;t<=T;++t)
    {
        fin>>r>>c>>m;
        cout<<"Case #"<<t<<":"<<endl;
        int l=r*c-m;
        #if ISDEBUG
        cout<<r<<' '<<c<<' '<<m<<' '<<l<<endl;
        #endif
        if(l==1)
        {
            cout<<'c';
            for(int i=1;i<c;++i)
                cout<<"*";
            cout<<endl;
            for(int i=1;i<r;++i)
            {
                for(int j=0;j<c;++j)
                    cout<<"*";
                cout<<"\n";
            }
            continue;
        }
        if(r==1)
        {
            if(l==1)
                cout<<"Impossible"<<endl;
            else
            {
                cout<<'c';
                for(int i=1;i<l;++i)
                    cout<<".";
                for(int i=0;i<m;++i)
                    cout<<"*";
                cout<<endl;
            }
        }
        else if(c==1)
        {
            if(l==1)
                cout<<"Impossible"<<endl;
            else
            {
                cout<<'c'<<endl;
                for(int i=1;i<l;++i)
                    cout<<'.'<<endl;
                for(int i=0;i<m;++i)
                    cout<<'*'<<endl;
            }
        }
        else
        {
            if(l<4)
                cout<<"Impossible"<<endl;
            else
                if(r==2)
                    if(l&1)
                        cout<<"Impossible"<<endl;
                    else
                    {
                        cout<<'c';
                        for(int i=l>>1;i>1;--i)
                            cout<<".";
                        for(int i=m>>1;i>0;--i)
                            cout<<"*";
                        cout<<endl;
                        for(int i=l>>1;i>0;--i)
                            cout<<".";
                        for(int i=m>>1;i>0;--i)
                            cout<<'*';
                        cout<<'\n';
                    }
                else if(c==2)
                    if(l&1)
                        cout<<"Impossible"<<endl;
                    else
                    {
                        cout<<"c."<<endl;
                        for(int i=l>>1;i>1;--i)
                            cout<<".."<<endl;
                        for(int i=m>>1;i>0;--i)
                            cout<<"**"<<endl;
                    }
                else
                    if(l&1&&l<9)
                        cout<<"Impossible"<<endl;
                    else
                    {
                        cout<<'c';
                        if(c<<1>l)
                        {
                            if(l&1)
                            {
                                int temp=(l-3)>>1;
                                for(int i=1;i<temp;++i)
                                    cout<<".";
                                for(int i=temp;i<c;++i)
                                    cout<<"*";
                                cout<<endl;
                                for(int i=0;i<temp;++i)
                                    cout<<".";
                                for(int i=temp+1;i<c;++i)
                                    cout<<"*";
                                cout<<"*\n";
                                cout<<"...";
                                for(int i=3;i<c;++i)
                                    cout<<"*";
                                cout<<endl;
                                for(int i=3;i<r;++i)
                                {
                                    for(int j=0;j<c;++j)
                                        cout<<'*';
                                    cout<<'\n';
                                }
                            }
                            else
                            {
                                for(int i=1;i<l>>1;++i)
                                    cout<<".";
                                for(int i=l>>1;i<c;++i)
                                    cout<<"*";
                                cout<<endl;
                                for(int i=0;i<l>>1;++i)
                                    cout<<".";
                                for(int i=l>>1;i<c;++i)
                                    cout<<'*';
                                cout<<'\n';
                                for(int i=2;i<r;++i)
                                {
                                    for(int j=0;j<c;++j)
                                        cout<<'*';
                                    cout<<'\n';
                                }
                            }
                        }
                        else
                        {
                            int temp=l/c;
                            if(l%c==1)
                            {
                                if(l/c==2)
                                {
                                    for(int i=2;i<c;++i)
                                        cout<<".";
                                    cout<<"*\n";
                                    for(int i=1;i<c;++i)
                                        cout<<".";
                                    cout<<"*\n";
                                    cout<<"...";
                                    for(int i=3;i<c;++i)
                                        cout<<"*";
                                    cout<<endl;
                                    for(int i=3;i<r;++i)
                                    {
                                        for(int j=0;j<c;++j)
                                            cout<<"*";
                                        cout<<"\n";
                                    }
                                }
                                else
                                {
                                    for(int i=1;i<c;++i)
                                        cout<<".";
                                    cout<<endl;
                                    for(int i=l/c;i>2;--i)
                                    {
                                        for(int j=0;j<c;++j)
                                            cout<<".";
                                        cout<<"\n";
                                    }
                                        for(int j=1;j<c;++j)
                                            cout<<".";
                                        cout<<"*\n";
                                    cout<<"..";
                                    for(int i=c-l%c;i>1;--i)
                                        cout<<"*";
                                    cout<<"\n";
                                    for(int i=l/c+1;i<r;++i)
                                    {
                                        for(int j=0;j<c;++j)
                                            cout<<"*";
                                        cout<<"\n";
                                    }
                                }
                            }
                            else
                            {
                                for(int i=1;i<c;++i)
                                    cout<<".";
                                cout<<endl;
                                for(int i=l/c;i>1;--i)
                                {
                                    for(int j=0;j<c;++j)
                                        cout<<".";
                                    cout<<"\n";
                                }
                                if(m)
                                {
                                    for(int i=l%c;i>0;--i)
                                        cout<<".";
                                    for(int i=c-l%c;i>0;--i)
                                        cout<<"*";
                                    cout<<"\n";
                                }
                                for(int i=l/c+1;i<r;++i)
                                {
                                    for(int j=0;j<c;++j)
                                        cout<<"*";
                                    cout<<"\n";
                                }
                            }
                        }
                    }
        }
//        system("PAUSE");
    }
    return 0;
}
