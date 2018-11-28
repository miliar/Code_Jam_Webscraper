#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<bitset>

using namespace std;

int main()
{
    freopen("d:\\Coding\\input.txt","r",stdin);
    freopen("d:\\Coding\\output.txt","w",stdout);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {

        double C,N,F,X,sum=0,t_i,sumi=0,res=INFINITY;

        cin>>C>>F>>X;
        int lim=(C-2)/F;
        for(int k=0;k<=100000;k++)
        {
            N=k;
            sum=0;

            if(k>0)
                sumi=sumi+(C/(2+(k-1)*F));
            sum=sum+sumi;


            t_i=sum+X/(2+N*F);

            res=min(res,t_i);






        }
        if(ii!=1)
            cout<<endl;

        cout<<"Case #"<<ii<<": ";
        printf("%.7f",res);



    }


    return 0;
}
