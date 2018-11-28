#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("finalisa.txt","w",stdout);
   /* cout<<"i*i= "<<'i'*'i'<<endl;
    cout<<"j*j= "<<'j'*'j'<<endl;
    cout<<"k*k= "<<'k'*'k'<<endl;
    cout<<"i*j= "<<'i'*'j'<<endl;
    cout<<"i*k= "<<'i'*'k'<<endl;
    cout<<"j*k= "<<'j'*'k'<<endl;*/
    int i,T,l,x,res='1',qu=1,temp,req='i';
    string s,ss;
    char unuse;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        res='1';
        qu=1;
        req='i';
        s="";
        ss="";
        cin>>l>>x;
        for(int tem=0;tem<l;tem++)
        {
            cin>>unuse;
            ss+=unuse;
        }
        for(int k=0;k<x;k++)s+=ss;


        for(i=0;i<s.size() && req<='l';i++)
        {
            if(res=='1')
            {
                res=s[i];
                //cout<<i<<" "<<res<<endl;
                if(res==req && qu==1)
                {
                req=req+1;
                res='1';
                }
                continue;
            }
            else
            {
               if(res>s[i])qu*=-1;

                temp=res*s[i];
                //cout<<temp<<endl;
                if(temp==11025 || temp==11236 || temp==11449)
                {
                    res='1';
                    qu*=-1;
                }
                else if(temp==11130)
                {
                    res='k';
                }
                else if(temp==11235)
                {
                    qu*=-1;
                    res='j';
                }
                else if(temp==11342)
                {
                    res='i';
                }
                //cout<<i<<" "<<res<<endl;
                if(res==req && qu==1)
                {
                    req=req+1;
                    res='1';
                }
            }
        }
        for(i;i<s.size();i++)
        {
            if(res=='1')
            {
                res=s[i];
                //cout<<i<<" "<<res<<endl;
                continue;
            }
            else
            {
                if(res>s[i])qu*=-1;

                temp=res*s[i];
                //cout<<temp<<endl;
                if(temp==11025 || temp==11236 || temp==11449)
                {
                    res='1';
                    qu*=-1;
                }
                else if(temp==11130)
                {
                    res='k';
                }
                else if(temp==11235)
                {
                    qu*=-1;
                    res='j';
                }
                else if(temp==11342)
                {
                    res='i';
                }
            }            //cout<<i<<" "<<res<<endl;
        }

       // cout<<endl<<endl<<qu<<" "<<char(res)<<" "<<char(req)<<endl<<endl;
        if(qu==1 && res=='1' && req>='l')
        cout<<"Case #"<<t+1<<": "<<"YES"<<endl;
        else
        cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
    }
    return 0;
}
