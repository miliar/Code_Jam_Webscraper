#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>


using namespace std;

int main()
{
    int T;
    int *Smax;
    int *ans;

    ifstream fptr("A-large.in");
    fptr>>T;
    Smax = new int[T];
    ans = new int[T];
    int **str = (int **)malloc(sizeof(int*)*T);

    for(int i=0;i<T;i++){
        ans[i]=0;
        fptr>>Smax[i];

        str[i]=(int *)malloc(sizeof(int)*Smax[i]*2);
        for(int j=0;j<=Smax[i];j++){
            //scanf("%1d",&str[i][j]);
            char fg;
            fptr>>fg;
            str[i][j]=fg-48;
            //cout<<str[i][j];
            //fptr>>str[i][j];
        }
    }

fptr.close();
ofstream of("output.txt");

    for(int i=0;i<T;i++){
        ans[i]=0;
        for(int j=1;j<=Smax[i];j++){
            int sum = 0;
            for(int k=0;k<j;k++){
                sum+=str[i][k];
            }
            if(sum<j){
                int aux = (j-sum);
                ans[i]+=aux;
                str[i][0]+=aux;
            }
        }
        //cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
        of<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
    }
    of.close();
    return 0;
}
