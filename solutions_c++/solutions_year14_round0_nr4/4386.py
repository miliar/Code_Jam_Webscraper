//
//  main.cpp
//  codejam
//
//  Created by shitian ni on 14-4-12.
//  Copyright (c) 2014年 shitian ni. All rights reserved.
//

#include <iostream>
#include<algorithm>
#include <vector>
using namespace std;
int main()
{
    int i,t;
    freopen("/Users/saintni/Documents/c++/codejam/codejam/D-large.in","r",stdin);
    freopen("/Users/saintni/Documents/c++/codejam/codejam/output.txt","w",stdout);
    scanf("%d¥n",&i);
    
    for(t=1;t<=i;t++)
    {
        cout<<"Case #"<<t<<": ";
        int N;
        scanf("%d",&N);
        double naomi[N];
        double ken[N];
        for(int i=0;i<N;i++)
            scanf("%lf",&naomi[i]);
        for(int i=0;i<N;i++)
            scanf("%lf",&ken[i]);
        long war=0;
        long dwar=0;
        std::vector<double> nao (naomi, naomi+N);
        std::vector<double> ke (ken, ken+N);
        std::sort (nao.begin(), nao.begin()+N);
        std::sort (ke.begin(), ke.begin()+N);
        
        std::vector<double>::iterator k_from=ke.begin();
        std::vector<double>::iterator tem_k=ke.begin();
        for (std::vector<double>::iterator n=nao.begin(); n!=nao.end(); ++n){
            
            for (k_from=tem_k; k_from!=ke.end(); ++k_from){
                if(*n>*k_from){
                    war++;
                    tem_k=k_from+1;
                    break;
                }
            }
        }
        int tem=0;//double tem1=0;
        std::vector<double>::iterator n_from=nao.begin();
        std::vector<double>::iterator tem_n=nao.begin();
        for (std::vector<double>::iterator k=ke.begin(); k!=ke.end(); ++k){
            
            for (n_from=tem_n; n_from!=nao.end(); ++n_from){
                if(*k>*n_from){
                    tem++;
                    tem_n=n_from+1;
                    break;
                }
            }
        }
        dwar=N-tem;
        cout<<war<<" "<<dwar<<endl;
    }
    return 0;
}

