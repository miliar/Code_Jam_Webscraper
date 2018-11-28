#include<cstdio>
using namespace std;

bool Y(const int&X,const int &C,const int& R )
{
    if(X==1) return true;
    else {
        if(R%X==0 || C%X==0){
            if(X==2) return true;
            else{
                if(X==3){
                    if(R!=1 && C!=1) return true;
                }
                else{
                    if(R>2 && C>2 ) return true;
                }
            }
        }
    }
    return false;
}

int main()
{
    int T,X,C,R;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d%d%d",&X,&C,&R);
        if(Y(X,C,R)){
            printf("Case #%d: %s\n",i,"GABRIEL");
        }
        else{
            printf("Case #%d: %s\n",i,"RICHARD");
        }
    }
    return 0;
}
