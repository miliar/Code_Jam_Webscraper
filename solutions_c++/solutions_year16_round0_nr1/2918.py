#include <fstream>
#include<iostream>
using namespace std;
int main(){
    int T, n,i,temp;
    int c,a[10],m=1,x,y;

    ofstream outputFile;
    outputFile.open("output.in");

    ifstream inputFile;
    inputFile.open("A-large.in");

    inputFile>>T;
    while(T--){
            c=0;
        inputFile>>n;
        if(n==0)
        {
            outputFile<<"Case #"<<m<<": "<<"INSOMNIA"<<endl;
        }
        else{
                for(i=0;i<10;i++)
                {
                    a[i]=-1;
                }
                x=n;y=n;
                for(i=1;c<10;i++)
                {
                    x=n*i;y=n*i;
                        while(x!=0)
                        {
                            temp=x%10;
                            x=x/10;
                            if(a[temp]==-1)
                            {
                                a[temp]=1;
                                c++;

                            }
                        }

                }
                outputFile<<"Case #"<<m<<": "<<y<<endl;
        }
        m++;
    }
    inputFile.close();
    outputFile.close();
    return 0;
}
