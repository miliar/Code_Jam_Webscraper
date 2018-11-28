#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int t,smax;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++){
        scanf("%d",&smax);
        string shystr;
        cin>>shystr;

        int l = shystr.length();
        int stand = 0, reqd = 0;
        for(int i=0;i<l;i++){
            int x = shystr[i] - '0';
            if(x > 0){
                if(stand >= i){
                    stand += x;
                    //cout<<"st :"<<stand<<endl;
                }else{
                    reqd += i - stand;
                    stand += x + i - stand;
                    //cout<<"req :"<<reqd<<endl;
                }
            }
        }

        printf("Case #%d: %d\n",ti,reqd);
    }
}
