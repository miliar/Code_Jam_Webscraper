#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);


typedef long long LL;








int main()
{
    freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
    //freopen("in.txt","r",stdin);

    int a[12][12],T;
    int i,j,k,num,cs;
    scanf("%d",&T);

    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);


        vector<int> v[2],V;
        k=2;


        while(k--)
        {
            scanf("%d",&num);
            num--;
            for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
                if(i==num) v[k].push_back(a[i][j]);
            }
        }



        for(i=0;i<v[0].size();i++)
        for(j=0;j<v[1].size();j++)
        {
            if(v[0][i]==v[1][j])
            {
                V.push_back(v[0][i]);
            }
        }



        //for(i=0;i<V.size();i++) cout<<V[i]<<" ";
        //cout<<endl;

        if(V.size()==0)
        {
            printf("Volunteer cheated!\n");
            continue;
        }
        else if(V.size()>1)
        {
            printf("Bad magician!\n");
            continue;
        }
        else
        {
            printf("%d\n",V[0]);
            continue;
        }




    }
    return 0;
}
