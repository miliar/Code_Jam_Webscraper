#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,test,i,cases=0,flag,mod,j;
    long long multiple,temp;
    bool a[11];
    ofstream fout;
    ifstream fin;
    fin.open("input.txt");
    fout.open("output.txt");
    fin>>test;
    while(test--){
        fin>>n;
        for(i=0;i<10;i++)
        a[i]=0;
        multiple=n;
        flag=0;
        j=2;
        if(n==0)
            fout<<"Case #"<<++cases<<": INSOMNIA\n";
        else{

            while(1){
                temp=multiple;
                while(temp!=0){
                  mod=temp%10;
                  a[mod]=1;
                  temp/=10;
                }
                for(i=0;i<10;i++){
                    if(a[i]==1)
                        flag=1;
                    else{
                        flag=0;
                        break;
                    }
                }
                if(flag==1)
                    break;
                multiple=n*j;
                j++;
            }
            fout<<"Case #"<<++cases<<": "<<multiple<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
