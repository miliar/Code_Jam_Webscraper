#include<iostream>
#include<fstream>

int mat[10];
bool isfinish()
{
    for(int i=0;i<10;++i){
        if(mat[i]==0)return false;
    }
    return true;
}
void zeromat()
{
    for(int i=0;i<10;++i)mat[i]=0;
}
void findthenumbers(long long s)
{
    long long i;
    for( ;s!=0; )
    {
        i=s/10;
        i=s-10*i;
        mat[i]=1;
        s/=10;
    }
}

int main()
{
    long long i,j,T,n,s;
    std::ofstream out("1.out");
    std::ifstream inp("1.in");
    inp>>T;
    for(int ii=0;ii<T;++ii){
        inp>>n;
        zeromat();
        if(n==0){
            out<<"Case #"<<ii+1<<": INSOMNIA\n";
            continue;
        }
        else{
            s=0;
            for( ; ; ){
                s+=n;
                findthenumbers(s);
                if(isfinish())break;
            }
            out<<"Case #"<<ii+1<<": "<<s<<"\n";
        }
    }
    out.close();
    inp.close();
    return 0;
}
