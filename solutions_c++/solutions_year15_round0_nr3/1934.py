
#include<stdio.h>
#include<iostream>

// 1 -> 1 , i -> 2 , j -> 3 , k -> 4

int product_matrix[5][5]=
{
    {0,0, 0, 0, 0},
    {0,1, 2, 3, 4},
    {0,2,-1, 4,-3},
    {0,3,-4,-1, 2},
    {0,4, 3,-2,-1}
};

int product(int a,int b)
{
    int sign=1;
    if(a<0){
        sign*=-1;
        a=-a;
    }
    if(b<0){
        sign*=-1;
        b=-b;
    }
    return sign * product_matrix[a][b];
}

int main()
{
    int T,D,L,X;
    char c;
    int str[10000],prod,str_prod,total;
    bool res;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        res=false;
        scanf("%d %d",&L,&X);
        for(int j=0;j<L;j++){
            do{scanf("%c",&c);}while(c!='i' && c!='j' && c!= 'k');
            str[j]=c-'i'+2;
        }

        int res_l[9],res_r[9];
        for(int j=0;j<9;j++)
        {
            res_l[j]=-1;
            res_r[j]=-1;
        }
        prod=1;
        for(int j=0;j<L;j++)
        {
            prod=product(prod,str[j]);
            if(res_l[prod+4]==-1)
                res_l[prod+4]=j;
        }
        str_prod=prod;
        prod=1;
        for(int j=L-1;j>=0;j--)
        {
            prod=product(str[j],prod);
            if(res_r[prod+4]==-1)
                res_r[prod+4]=j;
        }
/*
        for(int j=0;j<9;j++)
            std::cout<<"res_l["<<j<<"]= "<<res_l[j]<<std::endl;
        for(int j=0;j<9;j++)
            std::cout<<"res_r["<<j<<"]= "<<res_r[j]<<std::endl;
*/
        total=1;
        for(int j=0;j< X%4;j++)
            total=product(total,str_prod);

//        std::cout<<"TOTAL"<<total<<std::endl;
        if(total== -1){
            int count=X-1,in_i=-1,in_j=-1,idivpl,kdivpl;
            for(int j=1;j<5;j++)
                if(product(str_prod,j)==2)
                    idivpl=j;
                else if(product(str_prod,j)==-2)
                    idivpl=-j;
            for(int j=1;j<5;j++)
                if(product(j,str_prod)==4)
                    kdivpl=j;
                else if(product(j,str_prod)==-4)
                    kdivpl=-j;

            if(res_l[4+2]!=-1){
                in_i=res_l[4+2];
            }else if(res_l[4+idivpl]!=-1){
                count-=1;
                in_i=res_l[4+idivpl];
            }else if(str_prod!=1 && res_l[4+-2]!=-1){
                count-=2;
                in_i=res_l[4+-2];
            }else if(str_prod!=1 && res_l[4+-idivpl]!=-1){
                count-=3;
                in_i=res_l[4+-idivpl];
            }
            if(count>=0 && in_i!=-1){
                if(res_r[4+4]!=-1){
                    in_j=res_r[4+4];
                }else if(res_r[4+kdivpl]!=-1){
                    count-=1;
                    in_j=res_r[4+kdivpl];
                }else if(str_prod!=1 && res_r[4+-4]!=-1){
                    count-=2;
                    in_j=res_r[4+-4];
                }else if(str_prod!=1 && res_r[4+-kdivpl]!=-1){
                    count-=3;
                    in_j=res_r[4+-kdivpl];
                }
                if((count==0 && in_i<in_j-1) || (count==1 && !(in_i==L-1 && in_j==0)) || count>1){
                    res=true;
                }
            }
        }

        printf("Case #%d: %s\n",i+1,res?"YES":"NO");
    }
    return 0;
}
