#include<iostream>
#include<fstream>



int main()
{
    int i,j,N,n,T;
    char ch[205];
    char c;
    std::ofstream out("1.out");
    std::ifstream inp("1.in");
    inp>>T;
    inp.getline(ch,200);
    for(int ii=0;ii<T;++ii){
        inp.getline(ch,200);
        j=0;
        c=ch[0];
        for(i=0;ch[i]!='\0';++i){
            if(ch[i]!=c){
                j++;
                c=ch[i];
            }
        }
        if(ch[0]=='+' && j%2==1)j++;
        if(ch[0]=='-' && j%2==0)j++;
        out<<"Case #"<<ii+1<<": "<<j<<"\n";
    }
    out.close();
    inp.close();
    return 0;
}
