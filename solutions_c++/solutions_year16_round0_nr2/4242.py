#include <iostream>
#include <cstring>

using namespace std;
std::string pan;
void fliptill(int i){
    int len =pan.length();
    while(i>=0){
        if(pan[i]=='+'){
                pan[i]='-';
            }
            else{
                pan[i]='+';
            }
        i--;

    }
}

int flip(int n){
    int j=0,i=pan.length();
    while(i>=j){
        if(pan[i]=='-'){
            fliptill(i);
                n++;
        }
        i--;
    }
    return n;
}
int optimise(int flag)
{   int len=pan.length(),pu=0,mi=0,i=0,j;
    char temp;
   /* while(i<= len){
        if(pan[i]=='+'){
            pu++;
        }
        if(pan[i]=='-'){
            mi++;
        }
        i++;
    }
    if(pu<mi){
       // std::cout<<"more -  "<<pu<<" "<<mi<<endl;
        i=0;
        while(i<= len){
            if(pan[i]=='+'){
                pan[i]='-';
            }
            else{
                pan[i]='+';
            }
            i++;
        }
        i=0;
        j=len;
        while(i<=len/2){
            temp=pan[i];
            pan[i]=pan[j];
            pan[j]=temp;
            i++;
            j--;
        }
        return 1;
    }*/
    i=0;
    pu=0;
    mi=0;
if(flag){
    while(pan[i]=='+'){
        pu++;
        i++;
    }
    i=len;
    while(pan[i-1] == '+'){
        mi++;
        i--;
    }
    if(pu>mi){
        i=0;
        j=len;
        while(i<=len/2){
            temp=pan[i];
            pan[i]=pan[j];
            pan[j]=temp;
            i++;
            j--;
        }
        return 1;
    }
    }
    return 0;
}
int main()
{
    int cs,n=0,m,q;
    std::cin>>cs;
    m=cs;
    std::string temp;
    while(cs>0){
        std::cin>>pan;
        temp=pan;
        n=0;
        n=optimise(0);
        n=flip(n);
        pan=temp;
        q=0;
        q=optimise(1);
        q=flip(q);
       if(q<n){
            n=q;
        }
        std::cout<<"Case #"<<m-cs+1<<": "<<n<<endl;
        cs--;
    }
    return 0;
}
