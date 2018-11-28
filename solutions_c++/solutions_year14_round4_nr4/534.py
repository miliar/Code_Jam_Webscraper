#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int T,N,M;
int B[]={1,4,16,64,256,1024,4096,16384,65536,262144};
string str[10];


int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>M>>N;
        for(int i=0;i<M;i++) cin>>str[i];
        int cnt=0,maxn=0;
        for(int i=0;i<B[M];i++)
        {
            vector<int> vec[5];
            bool cwj=true;
            for(int j=0;j<5;j++) vec[j].clear();
            int k=i;
            for(int j=0;j<M;j++)
            {
                int id=k%4;
                k=k/4;
                if(id>=N)
                {
                    cwj=false;
                    break;
                }
                vec[id].push_back(j);
            }
            for(int j=0;j<N;j++)
            {
                if(vec[j].size()==0)
                {
                    cwj=false;
                    break;
                }
            }
            if(!cwj) continue;
            int sn=0;
            map<string,int> H;
            for(int j=0;j<N;j++)
            {
                H.clear();
                sn++;
                for(int z=0;z<vec[j].size();z++)
                {
                    int tag=vec[j][z];
                    string tmp="";
                    for(int w=0;w<str[tag].length();w++)
                    {
                        tmp+=str[tag][w];
                        if(H[tmp]==0)
                        {
                            sn++;
                            H[tmp]=1;
                        }
                    }
                }
            }
            if(sn>maxn)
            {
                maxn=sn;
                cnt=1;
            }
            else
            {
                if(sn==maxn) cnt++;
            }
        }
        printf("Case #%d: %d %d\n",ca,maxn,cnt);
    }
    return 0;
}


