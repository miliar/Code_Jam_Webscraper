#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <limits>
#include <iomanip>

using namespace std;

long long vbn=0;
vector<string> vec;
void recsv(string str,vector<int> used, int N,int pos)
{
    if(pos==N)
    {
        int arr[300]={0};
        arr[str[0]]=1;
        int len=str.size();
        for(int i=1;i<len;++i)
        {
            if(arr[str[i]]==0)
            {
                arr[str[i]]=1;
            }
            else
            {
                if(str[i]!=str[i-1])
                    return;
            }
        }
        vbn++;
    }
    else
    {
        for(int i=0;i<N;++i)
        {
            if(used[i]==0)
            {

                vector<int> temp(N+1,0);
                string tempx;
                for(int j=0;j<N;++j)
                {
                    temp[j]=used[j];
                }
                temp[i]=1;
                tempx=str+vec[i];
                recsv(tempx,temp,N,pos+1);
            }
        }
    }
}


int main()
{
    int i,j,k,l,m,n;
    int T,M,N,K,t1,t2,t3,t4,t5;
    long long ans,out;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B_output.txt","w",stdout);
    cin>>T;
    for(t1=1;t1<=T;++t1)
    {
        cout<<"Case #"<<t1<<": ";
        cin>>N;
        string temp,sf,fg;
        vec.clear();
        for(i=0;i<N;++i)
        {
            cin>>temp;
            sf=temp[0];
            t2=temp.size();
            t2--;
            for(j=1;j<t2;++j)
            {
                if(temp[j]==temp[j-1])
                    ;
                else
                    sf+=temp[j];
            }
            sf+=temp[t2];
            //cout<<sf<<" ";
            vec.push_back(sf);
        }
        //cout<<endl;
        vector<int> used(N+1,0);
        vbn=0;
        recsv(string(""),used,N,0);
        cout<<vbn<<endl;
    }

    return 0;
}
