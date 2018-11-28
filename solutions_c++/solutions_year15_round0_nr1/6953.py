#include<iostream>
#include<fstream>
using namespace std;
int con(char x);
main(){
ifstream fin;
fin.open("input.in");
int t,sm,ps=0,f=0,fs[100],tp,j=0;
char a[1001];
for(int i=0;i<100;i++)
fs[i]=0;
fin>>t;
tp=t;
while(t--){
    fin>>sm;
    fin>>a;
    int s=0;
    ps=0;
    f=0;
    for(int i=0;a[i]!='\0';i++){
            if(a[i] == '0')
            {

            }
            else
            {
                if( ps >= s)
                {
                    ps=ps+con(a[i]);
                }
                else
                {
                    while(ps != s)
                    {
                        f++;
                        ps++;
                    }
                    if( ps >= s)
                    {
                        ps=ps+con(a[i]);
                    }

                }
            }
            s++;

    }
    fs[j]=f;
    j++;

}
ofstream fout("Output.txt");
for(int i=0;i<tp;i++)
//cout<<"Case #"<<i+1<<": "<<fs[i]<<endl;
fout<<"Case #"<<i+1<<": "<<fs[i]<<endl;
}
int con(char x){
        if(x == '1')
        return 1;

        if(x == '2')
        return 2;

        if(x == '3')
        return 3;

        if(x == '4')
        return 4;

        if(x == '5')
        return 5;

        if(x == '6')
        return 6;

        if(x == '7')
        return 7;

        if(x == '8')
        return 8;

        if(x == '9')
        return 9;
}

