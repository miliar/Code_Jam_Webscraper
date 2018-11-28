//
//
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//



#include<string>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        int n,r,p,s;
        cin>>n>>r>>p>>s;
        string st="";
        for(int i=0;i<p;i++)
            st+='P';
        for(int i=0;i<r;i++)
            st+='R';
        for(int i=0;i<s;i++)
            st+='S';
        bool flag=false;
        do
        {
            string tmp=st;
            while(tmp.size()>1)
            {
                bool ed=true;
                string temp="";
                for(int i=0;i<tmp.size();i+=2)
                {
                    if(tmp[i]==tmp[i+1])
                    {
                        ed=false;
                        break;
                    }
                    if((tmp[i]=='P'||tmp[i+1]=='P')&&(tmp[i]=='R'||tmp[i+1]=='R'))
                        temp+='P';
                    if((tmp[i]=='P'||tmp[i+1]=='P')&&(tmp[i]=='S'||tmp[i+1]=='S'))
                        temp+='S';
                    if((tmp[i]=='R'||tmp[i+1]=='R')&&(tmp[i]=='S'||tmp[i+1]=='S'))
                        temp+='R';
                }
                if(!ed)
                    break;
                tmp=temp;
            }
            if(tmp.size()==1)
            {
                cout<<st<<endl;
                flag=true;
                break;
            }
        }while(next_permutation(st.begin(),st.end()));
        if(!flag)
            cout<<"IMPOSSIBLE"<<endl;
        
    }
}