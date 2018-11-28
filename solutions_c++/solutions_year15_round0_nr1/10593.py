#include <iostream>
#include<string>
#include<stdlib.h>
#include <cstdio>

using namespace std;

int main()
{

    freopen ("a.in","r",stdin);
    freopen ("a.out","w",stdout);
    int t;
    //int smax;
    scanf("%d",&t);
    for(int k=1;k<=t;k++){
        //printf("\nyo yo\n");
        string shystr;
        int smax;
        cin>>smax;
        cin>>shystr;
        int f = 0;
        int stand;

        //cout<<smax<<"\t"<<shystr<<endl;
        stand = shystr[0] - 48;
        int pc = stand;
        for(int i = 1;i <= smax; i++){
            int np;
            np = shystr[i] - 48;
            if(stand < i && np > 0 ){
                stand = i + np;
                //cout<<"f"<<f<<endl;
            }
            else{
                stand = stand + np;
            }
            //stand += np + (i - stand);
            //cout<<"s"<<stand<<endl;
            pc += np;
        }
        pc= stand - pc;
        //cout<<"f::\t"<<pc<<endl;

        printf("Case #%d: %d\n",k,pc);

    }



    fclose(stdout);
    return 0;
}
